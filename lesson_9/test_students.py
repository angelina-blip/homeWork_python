# test_students.py
import pytest
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Student

@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.rollback()  # отменяет изменения, сделанные в тесте
    session.close()

def test_add_student(db_session):
    # Создаем новый студент
    new_student = Student(
        user_id=999999,
        level='Beginner',
        education_form='Full-time',
        subject_id=1
    )
    db_session.add(new_student)
    db_session.commit()

    # Проверка, что студент добавлен
    retrieved = db_session.query(Student).filter_by(user_id=999999).first()
    assert retrieved is not None
    assert retrieved.user_id == 999999

    # Удаляем после теста
    db_session.delete(retrieved)
    db_session.commit()
    assert db_session.query(Student).filter_by(user_id=999999).first() is None

def test_update_student(db_session):
    # Создаем студента для теста
    student = Student(
        user_id=888888,
        level='Intermediate',
        education_form='Part-time',
        subject_id=2
    )
    db_session.add(student)
    db_session.commit()

    # Обновляем данные
    student.level = 'Advanced'
    db_session.commit()

    # Проверка обновления
    updated = db_session.query(Student).filter_by(user_id=888888).first()
    assert updated.level == 'Advanced'

    # Удаляем после теста
    db_session.delete(updated)
    db_session.commit()

def test_delete_student(db_session):
    # Создаем студента для теста
    student = Student(
        user_id=777777,
        level='Beginner',
        education_form='Online',
        subject_id=3
    )
    db_session.add(student)
    db_session.commit()

    # Удаляем
    db_session.delete(student)
    db_session.commit()

    # Проверка удаления
    deleted = db_session.query(Student).filter_by(user_id=777777).first()
    assert deleted is None
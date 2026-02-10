Документирование автоматизированных тестов для сайта и API Kinopoisk

Общая задача:
Этот проект содержит автоматизированные тесты для проверки сайта Kinopoisk и API сервиса. В тестах реализованы проверки интерфейса через Selenium и API через requests, что помогает убедиться в корректности работы сайта и связанного API сервиса.

Структура проекта

test/
│
├── tests/
│   ├── ui_tests/
│   │   ├── test_ui.py          # Тесты для интерфейса сайта (Selenium)
│   ├── api_tests/
│   │   ├── test_api.py         # Тесты для API запросов (requests)
│
├── config/
│   ├── env_config.py           # Конфигурация окружения, базовые URL и параметры
│   ├── test_data.py            # Тестовые данные и константы
│
└── README.md                     # Этот файл

Как запускать тесты
Предварительные требования: 
-Python 3.8+
-Установленные библиотеки:
pip install pytest allure-pytest selenium requests
Установленный драйвер Chrome

Подключите зависимости:
-selenium
-requests
-pytest
-allure-pytest

Запуск UI тестов
Чтобы запустить все UI тесты (используя Selenium и Chrome):
pytest -q --alluredir=allure-results tests/ui_tests/test_ui.py
Для более полного отчета Allure:
allure serve allure-results

Запуск API тестов
pytest -q --alluredir=allure-results tests/api_tests/test_api.py
Аналогично — просмотреть отчет:
allure serve allure-results
Дополнительные инструкции

Итоговый проект
Этот проект представляет собой комплексную проверку сайта и API Kinopoisk.

🔗 Перейти к финальной версии проекта (https://angelgreka.yonote.ru/share/71143ee4-9dec-4923-916a-f20831be68b3)


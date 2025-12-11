from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


WebDriverWait(driver, 20).until(
        lambda drv: len(drv.find_elements(By.TAG_NAME, "img")) >= 5
    )


WebDriverWait(driver, 20).until(
    lambda drv: all(
            drv.execute_script("return arguments[0].naturalWidth > 0", img)
            for img in drv.find_elements(By.TAG_NAME, "img")
        )
    )

images = driver.find_elements(By.TAG_NAME, "img")


third_image_src = images[3].get_attribute("src")
print("Src третьей картинки:", third_image_src)


driver.quit()
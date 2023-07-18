import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('chrome/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


@pytest.fixture()
def my_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('hkkjhk@jhg.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('123456789')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'
    # Нажимаем на кнопку "Мои питомцы"
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == 'Kdkjhdk'



import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Проверка соответствия количества питомцев в разделе "Мои питомцы" с цифрой указанной на странице.
def test_pets_num(my_pets):

    # Получаем питомцев и находим их количество.
    pets = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
    quantity_pets = len(pets)

    # Находим элемент содержащий количество питомцев на странице
    for r in pytest.driver.find_elements(By.LINK_TEXT, 'Питомцев:'):
        pets_stat = r.text

        # Проверяем колиство питомцев
        assert str(quantity_pets) in pets_stat

# Проверка питомцев на уникальность.
def test_uniq_pets(my_pets):

    # Получаем всех питомцев в разделе "Мои питомцы".
    pets = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))

    # Создаем список питомцев со всеми их атрибутами(тип и возраст).
    my_pets = []
    for pet in pets:
        my_pets.append(pet.text)
    # Проверяем питомцев на уникальность.
    for pet in my_pets:
        assert my_pets.count(pet) == 1, f"Питомец {pet[:-3]} не уникален"

# Проверка, что у всех питомцев есть имя, тип и возраст.
def test_names_type_age_pets(my_pets):

    # Получаем всех питомцев в разделе "Мои питомцы".
    pets = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))

    # Создаем список питомцев со всеми их атрибутами(тип и возраст).
    my_pets = []
    for pet in pets:
        my_pets.append(pet.text)

        # Проверяем, что у каждого питомца есть все 3 элемента(имя, тип и возраст)
        assert len(pet.text.split(' ')) == 3, f"У питомеца {pet.text} отсутствует один из параметров"

# Проверка имен питомцев на дубликаты.
def test_double_names_pets(my_pets):

    # Получаем имена всех питомцев в разделе "Мои питомцы".
    names = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))

    # Создаем список с именами питомцев
    my_names = []
    for name in names:
        my_names.append(name.text)

    # Проверяем имя питомца на уникальность.
    for name in my_names:
        assert my_names.count(name) == 1, f"Питомецев с именем {name} несколько"

# Проверка, что хотя бы у половины питомцев есть фото.
def test_photo(my_pets):

    #  Получаем атрибут, содержащий фото питомца.
    pets = WebDriverWait(pytest.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')))

    # Считаем количество питомцев, у которых атрибут с фото пуст.
    pets_no_photo = 0
    for pet in pets:
        if pet.get_attribute('src') == '':
            pets_no_photo += 1

    # Сравниваем количество питомцев без фото с половиной от общего числа.
    assert pets_no_photo <= int(len(pets) / 2)
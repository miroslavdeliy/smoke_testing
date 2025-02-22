from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Открытие окна браузера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920,1080)

#Ввод логина
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys("standard_user")
print('Введен логин')

#Вод пароля
password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print('Введен пароль')

#Нажатие на кнопку авторизации
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Нажата кнопка авторизации')

#Сохранение название 1-го товара
product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

#Сохранение цены 1-го товара
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

#Добавление 1-го товара в корзину
select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Продукт 1 добавлен в корзину')

#Сохранение название 2-го товара
product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_product_2 = product_2.text
print(value_product_2)

#Сохранение цены 2-го товара
price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

#Добавление 2-го товара в корзину
select_product_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print('Продукт 2 добавлен в корзину')

#Переход в корзину
cart = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
cart.click()
print("Переход в корзину")

#Проверка, что товар 1 в корзине
cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1, 'Ошибка! Название 1-го товара в корзине некорректно!'
print("Название 1-го товара в корзине корректно")

#Проверка, что цена товара 1 в корзине корректна
price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1, 'Ошибка! Цена товара 1 в корзине некорректна'
print('Цена товара 1 в корзине корректно')

#Проверка, что товар 2 в корзине
cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2, 'Ошибка! Название 2-го товара в корзине некорректно'
print("Название 2-го товара в корзине корректно")

#Проверка, что цена товара 2 в корзине корректна
price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2, 'Ошибка! Цена товара 2 в корзине некорретно'
print('Цена товара 2 в корзине корректно')

#Нажатие на кнопку Checkout
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print('Нажата кнопка checkout')

#Ввод в поле Имя
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Иван')
print('Введено имя')

#Ввод в поле Фамилия
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Иванов')
print('Введена фамилия')

#Ввод в поле Индекс
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys(16798)
print('Введен индекс')

#Нажание на кнопку continue
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Нажатие на кнопку Continue')

#Проверка, что название 1-го товара на итоговой странице корректно
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1, 'Ошибка! Название 1-го товара на итоговой странице некорректно!'
print('Название товара 1 на итоговой странице корректно!')

#Проверка, что цена 1-го товара на итоговой странице корректно
price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1, 'Ошибка! Цена товара 2 на итоговой странице некорректна'
print('Цена товара 1 на итоговой странице корректно')

#Проверка, что название 2-го товара на итоговой странице корректно
finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2, 'Ошибка! Название 2-го товара на итоговой странице некорректно!'
print('Название товара 2 на итоговой странице корректно!')

#Проверка, что цена 2-го товара на итоговой странице корректно
price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2, 'Ошибка! Цена товара 2 на итоговой странице некорректна'
print('Цена товара 2 на итоговой странице корректна')

#Суммирование цен
price_finish_product_1_without_sym = value_finish_price_product_1.lstrip('$')
price_finish_product_2_without_sym = value_finish_price_product_2.lstrip('$')
summary_price_float = float(price_finish_product_1_without_sym) + float(price_finish_product_2_without_sym)

#Проверка, что итоговая сумма совпадает с суммой цен товаров
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + "$" + str(summary_price_float)
print(item_total)
assert value_summary_price == item_total, 'Ошибка! Итоговая сумма некорректна'
print('Итоговая сумма корректна')

#Нажатие на кнопку finish
button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Нажата кнопка финиш")

#Проверка корретности информации о выполненом заказе
checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == 'Thank you for your order!'
print('Информация о выполнении заказа корректна')
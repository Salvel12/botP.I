import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

service = Service(GeckoDriverManager().install())


driver = webdriver.Firefox(service=service)
driver.maximize_window() 
driver.get("http://localhost:8080")



cambio1 = driver.window_handles

conocenos = driver.find_element(By.XPATH, '/html/body/main/div/div/a')
conocenos.click()
time.sleep(2)

cambio11 = driver.window_handles

nueva_ventana = len(cambio1) == len(cambio11)

if nueva_ventana:
    screenshot_path = "./inicio.png"
    driver.save_screenshot(screenshot_path)

entrar = driver.find_element(By.XPATH, '/html/body/main/div/div/a')
entrar.click()
time.sleep(1)

login = driver.find_element(By.XPATH, '/html/body/nav/div/a[3]')
login.click()
time.sleep(2)

correo = driver.find_element(By.XPATH, '//*[@id="email"]')
correo.click()
correo.send_keys('bot@gmail.com')

contraseña = driver.find_element(By.XPATH, '//*[@id="password"]')
contraseña.click()
contraseña.send_keys('123')

entrar = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
entrar.click()

screenshot_path = "./login.png"
driver.save_screenshot(screenshot_path)

time.sleep(2)

registro = driver.find_element(By.XPATH, '/html/body/nav/div/a[2]')
registro.click()


time.sleep(2)

datos = driver.find_element(By.XPATH, '//*[@id="id"]')
datos.click()
datos.send_keys(Keys.CONTROL + "a")
datos.send_keys(Keys.DELETE)
datos.send_keys('1001011100010')

datos = driver.find_element(By.XPATH, '//*[@id="name"]')
datos.click()

datos.send_keys('bot')

datos = driver.find_element(By.XPATH, '//*[@id="email_signup"]')
datos.click()

datos.send_keys('bot123@gmail.com')

datos = driver.find_element(By.XPATH, '//*[@id="password"]')
datos.click()

datos.send_keys('123')

datos = driver.find_element(By.XPATH, '//*[@id="contact_number"]')
datos.click()
datos.send_keys('3194588888')

datos = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
datos.click()

time.sleep(3)

screenshot_path = "./registro.png"
driver.save_screenshot(screenshot_path)






def borrar_y_escribir(campo_xpath, nuevo_texto):
    campo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, campo_xpath))
    )
    campo.click()
    campo.clear()
    campo.send_keys(nuevo_texto)

borrar_y_escribir('//*[@id="id"]', '1001011100010')
borrar_y_escribir('//*[@id="name"]', 'bot')
borrar_y_escribir('//*[@id="email_signup"]', 'bot123@elpoli.edu.co')
borrar_y_escribir('//*[@id="password"]', '123')
borrar_y_escribir('//*[@id="contact_number"]', '3194588888')

datos = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
datos.click()

time.sleep(3)

datos = driver.find_element(By.XPATH, '/html/body/nav/div/a[3]')
datos.click()


correo = driver.find_element(By.XPATH, '//*[@id="email"]')
correo.click()
correo.send_keys('bot123@elpoli.edu.co')

contraseña = driver.find_element(By.XPATH, '//*[@id="password"]')
contraseña.click()
contraseña.send_keys('123')

entrar = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
time.sleep(1)
entrar.click()



donar =driver.find_element(By.XPATH, '/html/body/nav/div[1]/a[3]')
donar.click()



donacion = driver.find_element(By.XPATH, '//*[@id="name"]')
donacion.click()
donacion.send_keys('gato')

donacion = driver.find_element(By.XPATH, '//*[@id="type"]')
donacion.click()
donacion.send_keys(Keys.ARROW_DOWN)
donacion.send_keys(Keys.ARROW_DOWN)
donacion.send_keys(Keys.ARROW_DOWN)
donacion.send_keys(Keys.ENTER)

donacion = driver.find_element(By.XPATH, '//*[@id="amount"]')
donacion.click()
donacion.send_keys('3')

donacion = driver.find_element(By.XPATH, '//*[@id="description"]')
donacion.click()
donacion.send_keys('es un gato')

screenshot_path = "./donacion.png"
driver.save_screenshot(screenshot_path)

time.sleep(2)

donacion = driver.find_element(By.XPATH, '/html/body/main/form/button')
donacion.click()

solicitar = driver.find_element(By.XPATH, '/html/body/nav/div[1]/a[2]')
solicitar.click()

time.sleep(3)

screenshot_path = "./solicitar.png"
driver.save_screenshot(screenshot_path)

driver.quit()
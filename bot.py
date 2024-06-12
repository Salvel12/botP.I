# Se importan librerias
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time 


#Se crea el bot, se instancia el driver, se abre google chrome y va a viajesexito
service = Service("driver/chromedriver.exe")
Driver = webdriver.Chrome(service=service)
Driver.maximize_window() 
Driver.get("https://www.viajesexito.com")


# va a paquetes y le da click
paquetes = Driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]/a/p') 
paquetes.click() 
time.sleep(1) 

#ya una vez en paquetes le da click en origen
origen = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
origen.click() 
time.sleep(1)

#copia el origen desde el que partiremos
origen2 = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origen2.send_keys("Jose Maria Cordova")
time.sleep(1)
origen2.send_keys(Keys.ENTER)
time.sleep(1)

#Damos click en destino
destino = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destino.click() 
time.sleep(1)

#copia el destino al que llegaremos
destino2 = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destino2.send_keys("Punta Cana")
time.sleep(1)
destino2.send_keys(Keys.ENTER)
time.sleep(1)

#clickea en fecha
fecha = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
fecha.click() 
time.sleep(1) 

#Ingresa la fecha de salida
fechaS = Driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[4]/div[3]/div[2]/div[1]') 
fechaS.click() 
time.sleep(1) 

#ingresa la fehca de volver
fechav = Driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[6]/div[2]/div[1]')
fechav.click() 
time.sleep(1) 

#Da click en aceptar
aceptar = Driver.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/button[2]') 
aceptar.click() 
time.sleep(1) 

#Click en habitación
habitacion = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]')
habitacion.click() 
time.sleep(1) 

#Crea una nueva habitación
habitacionn = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
habitacionn.click() 
time.sleep(1) 

#se da click en aplicar
aplicar = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button') 
aplicar.click() 
time.sleep(1) 

#click en buscar
buscar = Driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a') 
buscar.click() 
time.sleep(1)

#se abre una nueva ventana, el bot pasa a esa ventana
nuveaventana = Driver.window_handles[1] 
Driver.switch_to.window(nuveaventana) 
WebDriverWait(Driver, 26).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')))

#ciclo para tener los primeros 10 paquetes e imprime los precios
for i in range(1, 11): 
    xpath = f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[{i}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]' 
    price = Driver.find_element(By.XPATH, xpath) 
    print(price.text)

#click para escribir una aerolinea
aerolinea = Driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a') 
aerolinea.click() 
time.sleep(1) 

#escribe la aerolinea
aerolinea2 = Driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input') 
aerolinea2.click() 
aerolinea2.send_keys('Avianca') 
time.sleep(1) 
aerolinea2.send_keys(Keys.ENTER) 
time.sleep(1) 

#click en buscar
buscar2 = Driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input') 
buscar2.click() 
time.sleep(1) 

WebDriverWait(Driver, 26).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) 

#click en el whatsapp 
Contactanos = Driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p/a') 
Contactanos.click() 
time.sleep(10) 

#se apaga el bot
Driver.quit() 
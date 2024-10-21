from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://sig.ifc.edu.br/sigaa")

# Preencher o campo de nome
driver.find_element(By.NAME, "user.login").send_keys("João")

#preecnher o campo de senha
driver.find_element(By.NAME, "user.senha").send_keys("123456")

#Envia o formulário
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click
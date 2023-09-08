from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import requests

dir_path = os.getcwd()
print("está na pasta ->"+dir_path)
chrome_opcoes = Options()
chrome_opcoes.add_argument("user-data-dir="+dir_path+"/profile/whatsapp")
driver = webdriver.Chrome(options = chrome_opcoes)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
    try:
        print("foi")
        bolinha = driver.find_element(By.CLASS_NAME,'aumms1qt')
        bolinha = driver.find_elements(By.CLASS_NAME,'aumms1qt')
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        #acao_bolinha.click()
        #acao_bolinha.perform()
        #acao_bolinha.click()
        #acao_bolinha.perform()
        acao_bolinha.double_click().perform()

        #l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt
    except:
        print("teste") 

while True:
   bot() 
   
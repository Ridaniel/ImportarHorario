
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import properties
import time
import credentials

def driverSetUp():
    driver=webdriver.Chrome(executable_path=properties.DRIVER_PATH)
    driver.get('https://intranet.upc.edu.pe/Loginintermedia/loginupc.aspx?wap=558')
    accesWithCredentials(driver)


def accesWithCredentials(driver):
    print('accediendo')
    login=driver.find_element_by_id(properties.LOGIN_ELEMENT_ID).send_keys(credentials.USUARIO)
    print('encontre login')
    password=driver.find_element_by_id(properties.PASSWORD_ELEMENT_ID).send_keys(credentials.CONTRASEÑA)
    print('ingrese password')
    submit=driver.find_element_by_xpath('//a[contains(@href,"javascript:InvocarForm()")]').click()
    try:
        frame=frame_switch('F1',driver)
    #    print(driver.page_source)
        myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME,'FrmNotas')))
        print ("Page is ready!")
        for i in driver.find_elements_by_xpath('.//form[2]/table/tbody/tr/td/table/tbody/tr[3]'):
            print (i.text)
        #TODO HACER CLICK EN CADA ELEMENTO DE LA TABLA Y OBTENER INFORMACION
    
    except TimeoutException:
       
        print ("Loading took too much time!")
       


    time.sleep(800)


def frame_switch(name,driver):
      driver.switch_to.frame(driver.find_element_by_name(name))
def main():
    driverSetUp()    

if __name__ == "__main__":
    main()


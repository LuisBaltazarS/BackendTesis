from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver.init_driver import InitDriver
import json
import time


def test_eight_components(url):

    init_driver = InitDriver()
    init_driver.InitServiceDriver()
    driver = init_driver.PassUrlDriver(url)
    
    try:

        # Número de paginas

        time.sleep(10)

        cookie_button = WebDriverWait(driver, 10).until(

            EC.presence_of_element_located((By.CLASS_NAME, 'CookieConsentBanner__button'))

        )

        cookie_button.click()

        container_pages = WebDriverWait(driver, 15).until(

            EC.presence_of_element_located((By.CLASS_NAME, 'pagination__nav'))

        )

        number_pages = container_pages.find_elements(By.TAG_NAME, 'span')

        for i in number_pages:

            i.click()

            # Obteniedo el div que contiene tanto la marca, precio, etc.

            container = WebDriverWait(driver, 15).until(

                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "Showcase__content"))

            )

            # Recorremos el div ya que este trae una lista de objetos y se extrae lo que necesitamos.

            for e in container:

                # Obteniedo el titulo del div el cual es el nombre del producto
                producto = e.get_attribute("title")

                # Este div es el contenedor de la marca, precio fisico, precio virtual.
                container_mpp = e.find_element(
                    By.CLASS_NAME, 'Showcase__details')

                # Div que contiene la etiqueta p que contiene la marca
                container_marca = container_mpp.find_element(
                    By.CLASS_NAME, 'Showcase__brand')
                marca = container_marca.find_element(
                    By.TAG_NAME, 'a').get_attribute('innerText')

                # Cantidad de cada producto
                cantidad = container_mpp.find_element(
                    By.CLASS_NAME, 'Showcase__units-reference')

                # Div que contiene el precio fisico o virtual
                container_pfv = container_mpp.find_element(
                    By.CLASS_NAME, 'Showcase__priceBox')
                precios = container_pfv.find_elements(By.CLASS_NAME, 'price')

                if len(precios) > 1:

                    precio_fisica = precios[0].text
                    precio_virtual = precios[1].text

                else:

                    precio_fisica = precios[0].text
                    precio_virtual = None

                yield {

                    producto: {

                        "marca": marca,
                        "cantidad": cantidad.text,
                        "precio_fisica": precio_fisica,
                        "precio_virtual": precio_virtual

                    }

                }

    finally:

        driver.quit()


aceite = []

for o in test_eight_components("https://www.plazavea.com.pe/search/?_query=aceite&category-1=abarrotes"): 
    aceite.append(o)

print(aceite)

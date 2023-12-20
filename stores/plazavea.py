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

        try: 

            for i in number_pages:

                i.click()

                # Obteniedo el div que contiene tanto la marca, precio, etc.

                container = WebDriverWait(driver, 15).until(

                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "Showcase__content"))

                )

                # Recorremos el div ya que este trae una lista de objetos y se extrae lo que necesitamos.

                for e in container:

                    try: 

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

                        # Div que contiene a la imagen
                        container_img = e.find_element(
                            By.CLASS_NAME, 'Showcase__productImage'
                        )

                        # Obteniendo la imagen

                        image = container_img.find_element(
                            By.CLASS_NAME, 'showcase__image'
                        ).get_attribute('src')

                        if len(precios) > 1:

                            precio_fisica = precios[0].text
                            precio_virtual = precios[1].text

                        else:

                            precio_fisica = precios[0].text
                            precio_virtual = "No existe"

                        yield {

                            producto: {

                                "marca": marca,
                                "cantidad": cantidad.text,
                                "precio": precio_fisica,
                                "precio_virtual": precio_virtual,
                                "image": image

                            }

                        }

                    except: 

                        cantidad = "No existe"

                        if len(precios) > 1:

                            precio_fisica = precios[0].text
                            precio_virtual = precios[1].text

                        else:

                            precio_fisica = precios[0].text
                            precio_virtual = "No existe"

                        yield {

                            producto: {

                                "marca": marca,
                                "cantidad": cantidad,
                                "precio": precio_fisica,
                                "precio_virtual": precio_virtual,
                                "image": image

                            }

                        }

        except: 

            number_pages.pop(0)
            number_pages.pop(-1)

            for i in number_pages:

                i.click()

                # Obteniedo el div que contiene tanto la marca, precio, etc.

                container = WebDriverWait(driver, 30).until(

                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "Showcase__content"))

                )

                # Recorremos el div ya que este trae una lista de objetos y se extrae lo que necesitamos.

                for e in container:

                    try: 

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

                        # Div que contiene a la imagen
                        container_img = e.find_element(
                            By.CLASS_NAME, 'Showcase__productImage'
                        )

                        # Obteniendo la imagen
                        image = container_img.find_element(
                            By.CLASS_NAME, 'showcase__image'
                        ).get_attribute('src')

                        if len(precios) > 1:

                            precio_fisica = precios[0].text
                            precio_virtual = precios[1].text

                        else:

                            precio_fisica = precios[0].text
                            precio_virtual = "No existe"

                        yield {

                            producto: {

                                "marca": marca,
                                "cantidad": cantidad.text,
                                "precio": precio_fisica,
                                "precio_virtual": precio_virtual,
                                "image": image

                            }

                        }

                    except: 

                        cantidad = "No existe"

                        if len(precios) > 1:

                            precio_fisica = precios[0].text
                            precio_virtual = precios[1].text

                        else:

                            precio_fisica = precios[0].text
                            precio_virtual = "No existe"

                        yield {

                            producto: {

                                "marca": marca,
                                "cantidad": cantidad,
                                "precio": precio_fisica,
                                "precio_virtual": precio_virtual,
                                "image": image

                            }

                        }

    finally:

        driver.quit()

def set_elements(subcategory, url): 

    for o in test_eight_components(url): 
        subcategory.append(o)

# CARNES, AVES Y PESCADOS

pollo = []
res = []
cerdo = []
pescados = []
mariscos = []
pavo_pavita_gallina = []
enrollados = []
hamburguesas_nuggets_apanados = []

set_elements(pollo, "https://www.plazavea.com.pe/search/?_query=pollo&category-1=carnes-aves-y-pescados")
set_elements(res, "https://www.plazavea.com.pe/search/?_query=res&category-1=carnes-aves-y-pescados")
set_elements(cerdo, "https://www.plazavea.com.pe/search/?_query=cerdo&category-1=carnes-aves-y-pescados")
set_elements(pescados, "https://www.plazavea.com.pe/search/?_query=pescados&category-1=carnes-aves-y-pescados")
set_elements(mariscos, "https://www.plazavea.com.pe/search/?_query=mariscos")
set_elements(pavo_pavita_gallina, "https://www.plazavea.com.pe/search/?_query=pavo,%20pavita,%20gallina&category-1=carnes-aves-y-pescados")
set_elements(enrollados, "https://www.plazavea.com.pe/search/?_query=enrollados&category-1=carnes-aves-y-pescados")
set_elements(hamburguesas_nuggets_apanados, "https://www.plazavea.com.pe/search/?_query=hamburguesas,%20nuggets&category-1=carnes-aves-y-pescados&category-1=congelados")

# FRUTAS Y VERDURAS
        
frutas = []
verduras = []

set_elements(frutas, "https://www.plazavea.com.pe/search/?_query=frutas&category-1=frutas-y-verduras")
set_elements(verduras, "https://www.plazavea.com.pe/search/?_query=verduras&category-1=frutas-y-verduras")

# CONGELADOS
    
pescados_congelados = []
helados_postres = []

set_elements(pescados_congelados, "https://www.plazavea.com.pe/search/?_query=pescados&category-1=congelados")
set_elements(helados_postres, "https://www.plazavea.com.pe/search/?_query=helados,%20postres&category-1=congelados")

# LACTEOS Y HUEVOS
        
leche = []
yogurt = []
huevos = []
mantequilla_margarina = []

set_elements(leche, "https://www.plazavea.com.pe/search/?_query=leche&category-1=lacteos-y-huevos")
set_elements(yogurt, "https://www.plazavea.com.pe/search/?_query=yogurt&category-1=lacteos-y-huevos")
set_elements(huevos, "https://www.plazavea.com.pe/search/?_query=huevos&category-1=lacteos-y-huevos")
set_elements(mantequilla_margarina, "https://www.plazavea.com.pe/search/?_query=mantequilla,%20margarina&category-1=lacteos-y-huevos")

# QUESOS Y FIAMBRES
        
quesos = []
quesos_duros = []
embutidos = []
jamonadas = []

set_elements(quesos, "https://www.plazavea.com.pe/search/?_query=quesos%20blandos&category-1=quesos-y-fiambres")
set_elements(quesos_duros, "https://www.plazavea.com.pe/search/?_query=quesos%20duros")
set_elements(embutidos, "https://www.plazavea.com.pe/search/?_query=embutidos&category-1=quesos-y-fiambres")
set_elements(jamonadas, "https://www.plazavea.com.pe/search/?_query=jamonadas&category-1=quesos-y-fiambres")

# ABARROTES
        
aceite = []
arroz = []
azucar_endulzantes = []
menestras = []
conservas = []
fideos_pastas_y_salsas = []
salsas_cremas_y_condimentos = []
comidas_instantaneas = []
galletas_y_golosinas = []
chocolateria = []
snacks_y_piqueos = []

set_elements(aceite, "https://www.plazavea.com.pe/search/?_query=aceite&category-1=abarrotes")
set_elements(arroz, "https://www.plazavea.com.pe/search/?_query=arroz&category-2=arroz")
set_elements(azucar_endulzantes, "https://www.plazavea.com.pe/search/?_query=azucar%20y%20endulzantes&category-1=abarrotes")
set_elements(menestras, "https://www.plazavea.com.pe/search/?_query=menestras&category-1=abarrotes")
set_elements(conservas, "https://www.plazavea.com.pe/search/?_query=conservas&category-1=abarrotes")
set_elements(fideos_pastas_y_salsas, "https://www.plazavea.com.pe/search/?_query=fideos%20pastas%20y%20salsas&category-1=abarrotes")
set_elements(salsas_cremas_y_condimentos, "https://www.plazavea.com.pe/search/?_query=salsas%20cremas%20y%20condimentos&category-1=abarrotes")
set_elements(comidas_instantaneas, "https://www.plazavea.com.pe/search/?_query=comidas%20instantaneas&category-1=abarrotes")
set_elements(galletas_y_golosinas, "https://www.plazavea.com.pe/search/?_query=galletas%20y%20golosinas&category-1=abarrotes")
set_elements(chocolateria, "https://www.plazavea.com.pe/search/?_query=chocolate&category-1=abarrotes")
set_elements(snacks_y_piqueos, "https://www.plazavea.com.pe/search/?_query=snacks%20y%20piqueos&category-1=abarrotes")

# Desayunos

cafe = []
infusiones = []
cereales = []
mermeladas = []

# set_elements(cafe, "https://www.plazavea.com.pe/search/?_query=cafe&category-1=desayunos")
set_elements(infusiones, "https://www.plazavea.com.pe/search/?_query=infuciones&category-1=desayunos")
set_elements(cereales, "https://www.plazavea.com.pe/search/?_query=cereales&category-1=desayunos")
set_elements(mermeladas, "https://www.plazavea.com.pe/search/?_query=mermeladas&category-1=desayunos")

# Panadería y Pastelería

pan = []
panetones = []
postres = []
tortillas_masas = []

set_elements(pan, "https://www.plazavea.com.pe/search/?_query=pan&category-1=panaderia-y-pasteleria")
set_elements(panetones, "https://www.plazavea.com.pe/search/?_query=panetones&category-1=panaderia-y-pasteleria")
set_elements(postres, "https://www.plazavea.com.pe/search/?_query=postres&category-1=panaderia-y-pasteleria")
set_elements(tortillas_masas, "https://www.plazavea.com.pe/search/?_query=tortillas,%20masas&category-1=panaderia-y-pasteleria")

# Comidas Preparadas

pizzas_pastas_frescas = []
tamales_humitas = []
pastas_bocaditos_salsas = []

set_elements(pizzas_pastas_frescas, "https://www.plazavea.com.pe/search/?_query=pizzas,%20pastas,%20frescas&category-1=pollo-rostizado-y-comidas-preparadas")
set_elements(tamales_humitas, "https://www.plazavea.com.pe/search/?_query=tamales,%20humitas&category-1=pollo-rostizado-y-comidas-preparadas")
set_elements(pastas_bocaditos_salsas, "https://www.plazavea.com.pe/search/?_query=pastas,%20bocaditos,%20salsas&category-1=pollo-rostizado-y-comidas-preparadas")

# Bebidas

licores = []
vinos = []
espumantes = []
cervezas = []
gaseosas = []
aguas = []

set_elements(licores, "https://www.plazavea.com.pe/search/?_query=licores&category-1=bebidas")
set_elements(vinos, "https://www.plazavea.com.pe/search/?_query=vinos&category-1=bebidas")
set_elements(espumantes, "https://www.plazavea.com.pe/search/?_query=espumantes&category-1=bebidas")
set_elements(cervezas, "https://www.plazavea.com.pe/search/?_query=cervezas&category-1=bebidas")
set_elements(gaseosas, "https://www.plazavea.com.pe/search/?_query=gaseosas&category-1=bebidas")
set_elements(aguas, "https://www.plazavea.com.pe/search/?_query=aguas&category-1=bebidas")

test = {

    "Carnes, Aves y Pescados": {
        "Pollo": pollo,
        "Res": res,
        "Cerdo": cerdo,
        "Pescados": pescados,
        "Mariscos": mariscos,
        "Pavo, Pavita y Gallina": pavo_pavita_gallina,
        "Enrollados": enrollados,
        "Hamburguesas, Nuggets y Apanados": hamburguesas_nuggets_apanados
    },

    "Frutas y Verduras": {
        "Frutas": frutas,
        "Verduras": verduras
    },

    "Congelados": {
        "Pescados Congelados": pescados_congelados,
        "Helados Postres": helados_postres
    },

    "Lácteos y Huevos": {
        "Leche": leche,
        "Yogurt": yogurt,
        "Huevos": huevos,
        "Mantequilla y Margarina": mantequilla_margarina
    },

    "Quesos y Fiambres": {
        "Quesos": quesos,
        "Quesos Duros": quesos_duros,
        "Embutidos": embutidos,
        "Jamonadas": jamonadas
    },

    "Abarrotes": {

        "Arroz": arroz,
        "Aceite": aceite,
        "Azúcar y Endulzantes": azucar_endulzantes,
        "Menestras": menestras,
        "Conservas": conservas,
        "Fideos, Pastas y Salsas": fideos_pastas_y_salsas,
        "Salsas, Cremas y Condimentos": salsas_cremas_y_condimentos,
        "Comidas Instantáneas": comidas_instantaneas,
        "Galletas y Golosinas": galletas_y_golosinas,
        "Chocolatería": chocolateria,
        "Snacks y Piqueos": snacks_y_piqueos

    },

    "Desayunos": {
        "Café": cafe,
        "Infusiones": infusiones,
        "Cereales": cereales,
        "Mermeladas": mermeladas
    },

    "Panadería y Pastelería": {
        "Pan": pan,
        "Panetones": panetones,
        "Postres": postres,
        "Tortillas y Masas": tortillas_masas
    },

    "Comidas Preparadas": {
        "Pizzas y Pastas Frescas": pizzas_pastas_frescas,
        "Tamales y Humitas": tortillas_masas,
        "Pastas, bocaditos y salsas": pastas_bocaditos_salsas
    },

    "Bebidas": {
        "Licores": licores,
        "Vinos": vinos,
        "Espumantes": espumantes,
        "Cervezas": cervezas,
        "Gaseosas": gaseosas,
        "Aguas": aguas
    }

}

with open("plazavea.json", 'w') as archivo:
    json.dump(test, archivo, indent=4)


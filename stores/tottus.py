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

        container = WebDriverWait(driver, 30).until(

            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'div[data-pod="catalyst-pod"]')
            )

        )

        for e in container: 

            marca = e.find_element(
                By.CSS_SELECTOR, 'a > div > b'
            )

            producto = e.find_element(
                By.CSS_SELECTOR, 'a > span:nth-child(2) > b'
            )

            precio = e.find_element(
                By.CSS_SELECTOR, "a > div:nth-child(1) > ol > li.jsx-2112733514.prices-0 > div > span"
            )

            imagen = e.find_element(
                By.CSS_SELECTOR, "#testId-pod-image-https\:\/\/s7d2\.scene7\.com\/is\/image\/TottusPE\/40433790_1"
            )

            yield {

                producto: {

                    "marca": marca,
                    "cantidad": None,
                    "precio": precio,
                    "precio_virtual": None,
                    # "image": imagen

                }

            }
    
    except: 

        return "Error"
    
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

set_elements(pollo, "https://www.tottus.com.pe/buscar?q=pollo&filter=Categorias%3ACarnes-Pollo-Pavo")
set_elements(res, "https://www.tottus.com.pe/buscar?q=res&filter=Categorias%3ACarnes-Res-Cerdo")
set_elements(cerdo, "https://www.tottus.com.pe/buscar?q=cerdo&filter=Categorias%3ACarnes-Res-Cerdo")
set_elements(pescados, "https://www.tottus.com.pe/buscar?q=pescados&filter=Categorias%3APescados-Mariscos")
set_elements(mariscos, "https://www.tottus.com.pe/buscar?q=mariscos&filter=Categorias%3APescados-Mariscos")
set_elements(pavo_pavita_gallina, "https://www.tottus.com.pe/buscar?q=pavo+pavita+gallina&filter=Categorias%3ACarnes-Pollo-Pavo")
set_elements(enrollados, "https://www.tottus.com.pe/buscar?q=enrollados&filter=Categorias%3ACarnes-Res-Cerdo")
set_elements(hamburguesas_nuggets_apanados, "https://www.tottus.com.pe/buscar?q=hamburguesas+nuggets&filter=Categorias%3ACarnes-Pollo-Pavo")

# FRUTAS Y VERDURAS
        
frutas = []
verduras = []

set_elements(frutas, "https://www.tottus.com.pe/buscar?q=frutas&filter=Categorias%3AFrutas-Verduras")
set_elements(verduras, "https://www.tottus.com.pe/buscar?q=verduras&filter=Categorias%3AFrutas-Verduras")

# CONGELADOS
    
pescados_congelados = []
helados_postres = []

set_elements(pescados_congelados, "https://www.tottus.com.pe/buscar?q=pescados&filter=Categorias%3APescados-Mariscos")
set_elements(helados_postres, "https://www.tottus.com.pe/buscar?q=helados+postres&filter=Categorias%3ACongelados")

# LACTEOS Y HUEVOS
        
leche = []
yogurt = []
huevos = []
mantequilla_margarina = []

set_elements(leche, "https://www.tottus.com.pe/buscar?q=leche&filter=Categorias%3ALacteos-Huevos")
set_elements(yogurt, "https://www.tottus.com.pe/buscar?q=yogurt&filter=Categorias%3ALacteos-Huevos")
set_elements(huevos, "https://www.tottus.com.pe/buscar?q=huevos&filter=Categorias%3ALacteos-Huevos")
set_elements(mantequilla_margarina, "https://www.tottus.com.pe/buscar?q=mantequilla+margarina&filter=Categorias%3ALacteos-Huevos")

# QUESOS Y FIAMBRES
        
quesos = []
quesos_duros = []
embutidos = []
jamonadas = []

set_elements(quesos, "https://www.tottus.com.pe/buscar?q=quesos+blandos&filter=Categorias%3AQuesos-Fiambres")
set_elements(quesos_duros, "https://www.tottus.com.pe/buscar?q=quesos+duros&filter=Categorias%3AQuesos-Fiambres")
set_elements(embutidos, "https://www.tottus.com.pe/buscar?q=embutidos&filter=Categorias%3AQuesos-Fiambres")
set_elements(jamonadas, "https://www.tottus.com.pe/buscar?q=jamonadas&filter=Categorias%3AQuesos-Fiambres")

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

set_elements(aceite, "https://www.tottus.com.pe/buscar?q=aceite&filter=Categorias%3AAbarrotes")
set_elements(arroz, "https://www.tottus.com.pe/buscar?q=arroz&filter=Categorias%3AArroz")
set_elements(azucar_endulzantes, "https://www.tottus.com.pe/buscar?q=azucar+endulzantes&filter=Categorias%3AAbarrotes")
set_elements(menestras, "https://www.tottus.com.pe/buscar?q=menestras&filter=Categorias%3AAbarrotes")
set_elements(conservas, "https://www.tottus.com.pe/buscar?q=conservas&filter=Categorias%3AAbarrotes")
set_elements(fideos_pastas_y_salsas, "https://www.tottus.com.pe/buscar?q=fideos+pasta+salsas&filter=Categorias%3AAbarrotes")
set_elements(salsas_cremas_y_condimentos, "https://www.tottus.com.pe/buscar?q=salsas+cremas+condimentos&filter=Categorias%3AAbarrotes")
set_elements(comidas_instantaneas, "https://www.tottus.com.pe/buscar?q=comidas+instantaneas&filter=Categorias%3AAbarrotes")
set_elements(galletas_y_golosinas, "https://www.tottus.com.pe/buscar?q=galletas+golosinas&filter=Categorias%3AAbarrotes")
set_elements(chocolateria, "https://www.tottus.com.pe/buscar?q=chocolateria&filter=Categorias%3AAbarrotes")
set_elements(snacks_y_piqueos, "https://www.tottus.com.pe/buscar?q=snacks+piqueos&filter=Categorias%3AAbarrotes")

# Desayunos

cafe = []
infusiones = []
cereales = []
mermeladas = []

# set_elements(cafe, "https://www.tottus.com.pe/buscar?q=cafe&filter=Categorias%3ADesayunos")
set_elements(infusiones, "https://www.tottus.com.pe/buscar?q=infusiones&filter=Categorias%3ADesayunos")
set_elements(cereales, "https://www.tottus.com.pe/buscar?q=cereales&filter=Categorias%3ADesayunos")
set_elements(mermeladas, "https://www.tottus.com.pe/buscar?q=mermeladas&filter=Categorias%3ADesayunos")

# Panadería y Pastelería

pan = []
panetones = []
postres = []
tortillas_masas = []

set_elements(pan, "https://www.tottus.com.pe/buscar?q=pan&filter=Categorias%3APanaderia")
set_elements(panetones, "https://www.tottus.com.pe/buscar?q=panetones&filter=Categorias%3APanaderia")
set_elements(postres, "https://www.tottus.com.pe/buscar?q=postres&filter=Categorias%3APanaderia")
set_elements(tortillas_masas, "https://www.tottus.com.pe/buscar?q=tortillas+masas&filter=Categorias%3APanaderia")

# Comidas Preparadas

pizzas_pastas_frescas = []
tamales_humitas = []
pastas_bocaditos_salsas = []

set_elements(pizzas_pastas_frescas, "https://www.tottus.com.pe/buscar?q=pizzas+pastas+frescas&filter=Categorias%3APollo-Rostizado")
set_elements(tamales_humitas, "https://www.tottus.com.pe/buscar?q=tamales+humitas&filter=Categorias%3APollo-Rostizado")
set_elements(pastas_bocaditos_salsas, "https://www.tottus.com.pe/buscar?q=pastas+bocaditos+salsas&filter=Categorias%3APollo-Rostizado")

# Bebidas

licores = []
vinos = []
espumantes = []
cervezas = []
gaseosas = []
aguas = []

set_elements(licores, "https://www.tottus.com.pe/buscar?q=licores&filter=Categorias%3ABebidas")
set_elements(vinos, "https://www.tottus.com.pe/buscar?q=vinos&filter=Categorias%3ABebidas")
set_elements(espumantes, "https://www.tottus.com.pe/buscar?q=espumantes&filter=Categorias%3ABebidas")
set_elements(cervezas, "https://www.tottus.com.pe/buscar?q=cervezas&filter=Categorias%3ABebidas")
set_elements(gaseosas, "https://www.tottus.com.pe/buscar?q=gaseosas&filter=Categorias%3ABebidas")
set_elements(aguas, "https://www.tottus.com.pe/buscar?q=aguas&filter=Categorias%3ABebidas")

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

with open("tottus.json", 'w') as archivo:
    json.dump(test, archivo, indent=4)

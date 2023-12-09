
from selenium import webdriver


class InitDriver:

    def __init__(self):

        self.driver = ''

    def InitServiceDriver(self): 

        # Pasandole el webdriver descargado anteriormente 
        # (tiene que ser la misma version que tu chrome si lo tienes instalado)
        service = webdriver.ChromeService(
            executable_path=r"C:\Users\Luis Baltazar\Documents\EntornoVirtualPython\Selenium\chromedriver.exe")

        # Inicializamos el driver con el servicio
        self.driver = webdriver.Chrome(service=service)

    def PassUrlDriver(self, url): 

        # Obtenemos la estructura de la pagina indicada
        self.driver.get(url)

        return self.driver
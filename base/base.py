from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from random import randint


class base:

    def click_element(self, locator):
        """ Función para dar clic en un elemento mediante el localizador """
        WebDriverWait(self.driver, 10).until(expected.visibility_of_element_located(locator)).click()

    def do_click_list_random_element(self, locator):
        """ Función para realizar clic en un elemento al azar """
        WebDriverWait(self.driver, 15).until(expected.visibility_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        pos = randint(0, len(elements)-1)
        elements[pos].click()

    def get_text(self, locator):
        """ Función para obtener el texto de un elemento """
        element = WebDriverWait(self.driver, 10).until(expected.visibility_of_element_located(locator))
        return element.text


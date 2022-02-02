import unittest
import driver
from selenium.webdriver.common.by import By
from pages import page

a = 2
cTc = 0

class test(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = driver.driver_instance()
        cls.home = pages.page(cls.driver)
        time.sleep(10)

    def setUp(self):
        pass

    def test_1(self):
        self.home.add_random_home()
        self.assertEqual(self.home.get_text(self.home.count_homes), "1")
        self.home.remove_homes()
        self.home.add_random_home()
        self.assertEqual(self.home.get_text(self.home.count_homes), "1")
        self.home.remove_homes()
        self.driver.quit()
    
    def test_verificar_cantidad_cart(self):
        self.home.add_random_home()
        self.assertEqual(self.home.get_text(self.home.count_homes), cTc)

    def test_2_best_home(self):
        self.home.add_random_home()
        self.home.click_element(self.home.cart)
        self.home.click_element(self.home.buy_homes)
        #time.sleep(1)
        title, message = self.home.get_text_alert()
        self.assertEqual("Felicidades", title)
        self.assertEqual("Compra realizada con éxito", message)
        self.home.click_element((By.ID, "android:id/button1"))

    def test_2(self):
        self.home.add_random_home()
        self.home.click_element(self.home.cart)
        self.home.click_element(self.home.buy_homes)
        #time.sleep(1)
        title, message = self.home.get_text_alert()
        self.assertEqual("Felicidades", title)
        self.assertEqual("Compra realizada con éxito", message)
        self.home.click_element((By.ID, "android:id/button1"))

    def test_scroll_down(self):
        self.home.do_swipe(self.home.discovered, 2)
        department = self.home.get_text_department()
        self.assertEqual("Top mejores", department)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()


""" if __name__ == "__main__":
    unittest.main() """

from selenium.webdriver.common.by import By

class page():
    # Localizadores de la aplicación
    cart = (By.ID, "com.merqueo.debug:id/imvCartButton")
    discovered = (By.ID, "com.merqueo.debug:id/tvTitleCollection")
    add_movie = (By.ID, "com.merqueo.debug:id/btAddMovie")
    remove_movie = (By.ID, "com.merqueo.debug:id/btRemove")
    count_movies = (By.ID, "com.merqueo.debug:id/txvCount")
    buy_movies = (By.ID, "com.merqueo.debug:id/btBuyMovies")
    alert_title = (By.ID, "ccom.merqueo.debug:id/alertTitle")
    alert_message = (By.ID, "android:id/message")
    alert_close = (By.ID, "android:id/button1")

    def __init__(self, driver):
        self.driver = driver

    def add_random_movie(self):
        self.do_click_list_random_element(self.add_movie)

    def remove_movies(self):
        self.click_element((By.XPATH, '//*[@resource-id="com.merqueo.debug:id/home"]//*[''@text="Remover"]'))

    def get_text_alert(self):
        title = self.get_text(self.alert_title)
        message = self.get_text(self.alert_message)
        return title, message

    def get_text_department(self):
        return self.get_text(self.discovered)

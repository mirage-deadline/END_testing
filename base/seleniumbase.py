from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def __form_selenium_by(self, find_by) -> str:
        methods_and_names = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'name': By.NAME,
            'tag_name': By.TAG_NAME,
            'link': By.LINK_TEXT,
            'id': By.ID,
            'class_name': By.CLASS_NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
        }
        if find_by not in methods_and_names.keys():
            raise KeyError

        return methods_and_names[find_by]
    
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__form_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Есть элемент на странице"""
        return self.__wait.until(ec.presence_of_element_located((self.__form_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Ожидание того, пока пропадет элемент со страницы"""
        return self.__wait.until(ec.invisibility_of_element_located((self.__form_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__form_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Есть элементы на странице"""
        return self.__wait.until(ec.presence_of_all_elements_located((self.__form_selenium_by(find_by), locator)), locator_name)

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [el for el in elements if el.text.lower() == name][0]

from typing import List
from selenium.webdriver import Chrome
from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class HomepageNav(SeleniumBase):
    
    def __init__(self, driver: Chrome) -> None:
        super().__init__(driver)
        self.__nav_bar: str = '#navigation>span'
        self.NAV_LINK_TEXT_WIDTH_GT1000 = 'LATEST,BRANDS,CLOTHING,FOOTWEAR,ACCESSORIES,LIFESTYLE,GIFTS,SALE,LAUNCHES,FEATURES'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_bar, 'Header Navigation List')

    def get_nav_links_text(self):
        return ','.join([link.text for link in self.get_nav_links()])

    def get_nav_link_by_name(self, name: str):
        links = self.get_nav_links()
        return self.get_element_by_text(links, name)
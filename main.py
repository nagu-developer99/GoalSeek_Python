import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
import datetime as dt

download_btn = "//a[contains(@class, 'button') and contains(text(), 'Download Python') and contains(@href, 'amd64')]"
MAXELEMENTWAIT = 60


class CustomElement(WebElement):
    def __init__(self, driver):
        self.driver = driver
        self.wait = MAXELEMENTWAIT

    def prepare_xpath(self, attribs: dict) -> str:
        if 'type' not in attribs.keys():
            print(f'type not supplied')
            return ''
        type = attribs.pop('type')
        props = []
        for k, v in attribs.items():
            attr_name = 'text()' if k == 'text' else f'@{k}'
            part_xpath = f"contains({attr_name}, '{v}')"
            props.append(part_xpath)
        prop_clause = ' and '.join(props)
        return f'//{type}[{prop_clause}]'

    def get_all_elements(self, attribs: dict):
        elems = []
        end_time = dt.datetime.now() + dt.timedelta(seconds=self.wait)
        while dt.datetime.now() < end_time:
            try:
                elems = driver.find_elements(By.XPATH, self.prepare_xpath(attribs))
                if len(elems) > 0:
                    return elems
            except NoSuchElementException:
                pass
        return []

    def get_element(self, attribs: dict):
        elems = self.get_all_elements(attribs)
        if len(elems):
            return elems[0]
        else:
            return None


xyz = CustomElement(driver)

print(xyz.prepare_xpath({'class': 'button', 'text': 'Download Python', 'type': 'a', 'href': 'amd64'}))
xyz.prepare_xpath(_class='button', text='Download Python')

# class CustomElement(WebElement):
#     objTimeOut = 10
#     def get_element(self, props: dict):

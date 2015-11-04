__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com theater search results page
"""

from selenium.common.exceptions import NoSuchElementException


class Theaters:
    # Class to define elements of the theater search results page
    def __init__(self, driver):
        self.driver = driver
        self._theaterListContainer = driver.find_element_by_class_name("address-box")
        self.theatersList = []
        for theater in self._theaterListContainer.find_elements_by_class_name("type"):
            self.theatersList.append(theater.find_element_by_tag_name("a").text)

    def click_theater(self, linkText):
        try:
            self._theaterListContainer.find_element_by_partial_link_text(linkText).click()
        except NoSuchElementException:
            raise


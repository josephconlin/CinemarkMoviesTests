__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com theater search results page
"""

from TestBrowser import TestBrowser
from HeaderPage import Header
from TheaterDetailPage import TheaterDetail

import unittest
from selenium.common.exceptions import NoSuchElementException


class Theaters():
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


class TheatersTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        # For internal testing purposes, navigate to the theater search results page
        self.header = Header(self.driver)
        self.header.do_search("Salt Lake City")
        self.theaters = Theaters(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_theaters_list(self):
        self.assertNotEqual(0, len(self.theaters.theatersList), "Did not create theaters list")
        self.assertNotEqual(0, len(self.theaters.theatersList[0]), "Did not get a valid list of theaters")

    def test_clickTheaterBadInputText(self):
        self.assertRaises(NoSuchElementException, self.theaters.click_theater, "Non existent theater")

    def test_clickTheaterValidInputText(self):
        testTheaterName = "Cinemark"
        currentPage = self.driver.current_url
        self.theaters.click_theater(testTheaterName)
        newPage = self.driver.current_url
        theaterName = TheaterDetail(self.driver).theaterName
        self.assertNotEqual(currentPage, newPage, "Selecting a theater did not navigate to a new page")
        self.assertIn(testTheaterName.lower(), theaterName.lower(),
                      "Did not end up on theater detail page for selected theater")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TheatersTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

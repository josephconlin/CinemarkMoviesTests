__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com header items
"""

import TestBrowser

import unittest
import selenium
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randint


class Header():
    # Class to define elements of the header
    def __init__(self, driver):
        self.movieSelector = driver.find_element_by_class_name("btn-search")
        self.searchText = driver.find_element_by_id("main_inp1")
        self.searchSubmit = driver.find_element_by_xpath('//input[contains(@src,\"btn-submit.gif\")]')
        self.movieList = self.getMovieList(driver)

    def getMovieList(self, driver):
        self.movieSelector.click()
        movieList = []
        for movie in driver.find_element_by_class_name("inner").find_elements_by_tag_name("a"):
            movieList.append(movie.text)
        return movieList

    def selectRandomMovie(self, driver):
        i = randint(0,len(self.movieList)-1)
        ActionChains(driver).click_and_hold(self.movieSelector).perform()
        driver.find_element_by_link_text(self.movieList[i]).click()
        return i

    def inputSearchString(self, driver, searchString):
        self.searchText.clear()
        self.searchText.sendKeys(searchString)

    def doSearch(self, driver, searchString=''):
        self.inputSearchString(driver, searchString)
        self.searchSubmit.click()

class HeaderTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser.TestBrowser().getbrowser()
        self.header = Header(self.driver)

    def tearDown(self):
        self.driver.quit()

    def testMovieList(self):
        self.assertNotEqual(0, len(self.header.movieList), "Did not create movie list")
        self.assertNotEqual(0, len(self.header.movieList[0]), "Did not get a valid list of movies")

    def testMovieSelection(self):
        i = self.header.selectRandomMovie(self.driver)
        self.assertEqual(self.header.movieList[i].lower(), self.driver.find_element_by_tag_name("h1").text.lower(),
                      "Did not end up on movie listing page")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
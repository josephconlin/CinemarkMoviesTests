__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com header items
"""

from TestBrowser import TestBrowser

import unittest
from random import randint


class Header():
    # Class to define elements of the header
    def __init__(self, driver):
        self.driver = driver
        self.movieSelector = driver.find_element_by_class_name("btn-search")
        self.searchText = driver.find_element_by_id("main_inp1")
        self.searchSubmit = driver.find_element_by_xpath('//input[contains(@src,\"btn-submit.gif\")]')
        self.movieList = self.get_movie_list()

    def get_movie_list(self):
        self.movieSelector.click()
        movieList = []
        for movie in self.driver.find_element_by_class_name("inner").find_elements_by_tag_name("a"):
            movieList.append(movie.text)
        return movieList

    # TODO: Create select_movie_by_index and select_movie_by_name functions and have this one call one of those
    def select_random_movie(self):
        i = randint(0,len(self.movieList)-1)
        self.movieSelector.click()
        # Firefox doesn't detect the movie list as visible, IE and Chrome don't leave the movie display open
        # Set the style display on the movie list the same way the page does so that the link can be found and clicked
        self.driver.execute_script('arguments[0].setAttribute("style", "display: block;")',
                              self.driver.find_element_by_class_name("drop"))
        self.driver.find_element_by_class_name("inner").find_elements_by_tag_name("a")[i].click()
        return i

    def input_search_string(self, searchString):
        self.searchText.clear()
        self.searchText.send_keys(searchString)

    def do_search(self, searchString=''):
        self.input_search_string(searchString)
        self.searchSubmit.click()


class HeaderTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        self.header = Header(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_movie_list(self):
        self.assertNotEqual(0, len(self.header.movieList), "Did not create movie list")
        self.assertNotEqual(0, len(self.header.movieList[0]), "Did not get a valid list of movies")

    def test_movie_selection(self):
        currentPage = self.driver.current_url
        i = self.header.select_random_movie()
        newPage = self.driver.current_url
        self.assertNotEqual(currentPage, newPage, "Selecting a movie did not navigate to a new page")
        self.assertEqual(self.header.movieList[i].lower(), self.driver.find_element_by_tag_name("h1").text.lower(),
                      "Did not end up on movie listing page for selected movie")

    def test_search(self):
        testText = "ABC123"
        currentPage = self.driver.current_url
        self.header.do_search(testText)
        newPage = self.driver.current_url
        self.assertNotEqual(currentPage, newPage, "Searching did not navigate to a new page")
        self.assertIn(testText, newPage, "Search text not found in search URL string")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
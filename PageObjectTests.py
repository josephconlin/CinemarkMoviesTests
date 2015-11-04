__author__ = 'Joseph Conlin'
"""
Tests for page objects
"""
from TestBrowser import TestBrowser
from HeaderPage import Header
from TheatersPage import Theaters
import TheaterDetailPage

import unittest
from selenium.common.exceptions import NoSuchElementException

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
        theaterName = TheaterDetailPage.TheaterDetail(self.driver).theaterName
        self.assertNotEqual(currentPage, newPage, "Selecting a theater did not navigate to a new page")
        self.assertIn(testTheaterName.lower(), theaterName.lower(),
                      "Did not end up on theater detail page for selected theater")


class TheaterDetailTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        # For internal testing purposes, navigate to a theater details page
        self.header = Header(self.driver)
        self.header.do_search("Salt Lake City")
        self.theaters = Theaters(self.driver)
        self.theaters.click_theater("Cinemark")
        self.theater = TheaterDetailPage.TheaterDetail(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def test_theaters_list(self):
    #     a = TheaterDetailPage.MovieDetail(self.theater._theaterMoviesListContainer, 0)


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
    testsToRun = [
        # HeaderTests,
        # TheatersTests,
        TheaterDetailTests,
    ]
    suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(test) for test in testsToRun])
    unittest.TextTestRunner(verbosity=2).run(suite)

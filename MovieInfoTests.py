__author__ = 'Joseph Conlin'
"""
Tests for Cinemark.com movie info
"""
from TestBrowser import TestBrowser
from HeaderPage import Header
from TheatersPage import Theaters
import TheaterDetailPage

import unittest
from selenium.common.exceptions import NoSuchElementException

# Setup some common test variables
_headerSearchText = "Salt Lake City"
# _headerSearchTextNoSpaces = "ABC123"
_theaterLinkText = "Cinemark"


class MovieInfoTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        # For internal testing purposes, navigate to a theater details page
        self.header = Header(self.driver)
        self.header.do_search(_headerSearchText)
        self.theaters = Theaters(self.driver)
        self.theaters.click_theater(_theaterLinkText)
        self.theater = TheaterDetailPage.TheaterDetail(self.driver)
        self.theaterCalendar = TheaterDetailPage.TheaterCalendar(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_log_csv(self):
        pass


# class TheatersTests(unittest.TestCase):
#     def setUp(self):
#         self.driver = TestBrowser().get_browser()
#         # For internal testing purposes, navigate to the theater search results page
#         self.header = Header(self.driver)
#         self.header.do_search(_headerSearchText)
#         self.theaters = Theaters(self.driver)
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test_theaters_list(self):
#         self.assertNotEqual(0, len(self.theaters.theatersList), "Did not create theaters list")
#         self.assertNotEqual(0, len(self.theaters.theatersList[0]), "Did not get a valid list of theaters")
#
#     def test_click_theater_bad_input_text(self):
#         self.assertRaises(NoSuchElementException, self.theaters.click_theater, _headerSearchTextNoSpaces)
#
#     def test_click_theater_valid_input_text(self):
#         currentPage = self.driver.current_url
#         self.theaters.click_theater(_theaterLinkText)
#         newPage = self.driver.current_url
#         theaterName = TheaterDetailPage.TheaterDetail(self.driver).theaterName
#         self.assertNotEqual(currentPage, newPage, "Selecting a theater did not navigate to a new page")
#         self.assertIn(_theaterLinkText.lower(), theaterName.lower(),
#                       "Did not end up on theater detail page for selected theater")
#
#
# class TheaterDetailTests(unittest.TestCase):
#     def setUp(self):
#         self.driver = TestBrowser().get_browser()
#         # For internal testing purposes, navigate to a theater details page
#         self.header = Header(self.driver)
#         self.header.do_search(_headerSearchText)
#         self.theaters = Theaters(self.driver)
#         self.theaters.click_theater(_theaterLinkText)
#         self.theater = TheaterDetailPage.TheaterDetail(self.driver)
#         self.theaterCalendar = TheaterDetailPage.TheaterCalendar(self.driver)
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test_change_days(self):
#         currentPage = self.driver.current_url
#         self.theaterCalendar.click_today_plus_two()
#         newPage = self.driver.current_url
#         self.assertNotEqual(currentPage, newPage, "Selecting a different day did not navigate to a new page")
#
#     def test_movies_list_different_days(self):
#         currentMovieList = self.theater.theaterMoviesList
#         self.theaterCalendar.click_today_plus_one()
#         newTheater = TheaterDetailPage.TheaterDetail(self.driver)
#         newMovieList = newTheater.theaterMoviesList
#         self.assertNotEqual(currentMovieList[0].movieShowTimeList[0], newMovieList[0].movieShowTimeList[0],
#                             "Movie date and time from today matches movie date and time from tomorrow")


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
    testsToRun = [
        MovieInfoTests,
        # TheatersTests,
        # TheaterDetailTests,
    ]
    suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(test) for test in testsToRun])
    unittest.TextTestRunner(verbosity=2).run(suite)

__author__ = 'Joseph Conlin'
"""
Tests for Cinemark.com movie info
"""
from TestBrowser import TestBrowser
from HeaderPage import Header
from TheatersPage import Theaters
import TheaterDetailPage
import FileOutput

import unittest
import os
from selenium.common.exceptions import NoSuchElementException

# Setup some common test variables
_headerSearchText = "Salt Lake City"
_theaterLinkText = "Cinemark"
_csvFileName = "CSVTest"+FileOutput.WriteCSV.defaultFileExtension


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
        currentFileSize = 0
        try:
            currentFileSize = os.path.getsize(_csvFileName)
        except os.error:
            # Error is likely due to file not existing which means size 0 so do nothing
            pass

        # TODO: After TheaterDetailPage.TheaterCalendar has index based function, rewrite below in a loop
        # Initial load of self.theater is today so no need to click, just write data
        FileOutput.WriteCSV.write_movie_details(self.theater, _csvFileName)
        self.theaterCalendar.click_today_plus_one()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteCSV.write_movie_details(newDay, _csvFileName)
        self.theaterCalendar.click_today_plus_two()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteCSV.write_movie_details(newDay, _csvFileName)
        self.theaterCalendar.click_today_plus_three()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteCSV.write_movie_details(newDay, _csvFileName)
        self.theaterCalendar.click_today_plus_four()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteCSV.write_movie_details(newDay, _csvFileName)
        self.theaterCalendar.click_today_plus_five()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteCSV.write_movie_details(newDay, _csvFileName)
        self.theaterCalendar.click_today_plus_six()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteCSV.write_movie_details(newDay, _csvFileName)

        newFileSize = os.path.getsize(_csvFileName)
        self.assertLess(currentFileSize, newFileSize, "Did not write new data to csv output file")


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

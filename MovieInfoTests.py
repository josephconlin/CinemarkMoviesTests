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
_excelFileName = "ExcelTest"+FileOutput.WriteExcel.defaultFileExtension
_jsonFileName = "JSONTest"+FileOutput.WriteJSON.defaultFileExtension


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
        except FileNotFoundError:
            # Error is due to file not existing which means size 0 so do nothing
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

    def test_log_excel(self):
        currentFileSize = 0
        try:
            currentFileSize = os.path.getsize(_excelFileName)
        except FileNotFoundError:
            # Error is due to file not existing which means size 0 so do nothing
            pass

        # TODO: After TheaterDetailPage.TheaterCalendar has index based function, rewrite below in a loop
        # Initial load of self.theater is today so no need to click, just write data.
        FileOutput.WriteExcel.write_movie_details(self.theater, _excelFileName)
        self.theaterCalendar.click_today_plus_one()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteExcel.write_movie_details(newDay, _excelFileName)
        self.theaterCalendar.click_today_plus_two()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteExcel.write_movie_details(newDay, _excelFileName)
        self.theaterCalendar.click_today_plus_three()
        TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteExcel.write_movie_details(newDay, _excelFileName)
        self.theaterCalendar.click_today_plus_four()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteExcel.write_movie_details(newDay, _excelFileName)
        self.theaterCalendar.click_today_plus_five()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteExcel.write_movie_details(newDay, _excelFileName)
        self.theaterCalendar.click_today_plus_six()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteExcel.write_movie_details(newDay, _excelFileName)

        newFileSize = os.path.getsize(_excelFileName)
        self.assertLess(currentFileSize, newFileSize, "Did not write new data to Excel output file")

    def test_log_json(self):
        currentFileSize = 0
        try:
            currentFileSize = os.path.getsize(_jsonFileName)
        except FileNotFoundError:
            # Error is due to file not existing which means size 0 so do nothing
            pass

        # TODO: After TheaterDetailPage.TheaterCalendar has index based function, rewrite below in a loop
        # Initial load of self.theater is today so no need to click, just write data.
        FileOutput.WriteJSON.write_movie_details(self.theater, _jsonFileName)
        self.theaterCalendar.click_today_plus_one()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteJSON.write_movie_details(newDay, _jsonFileName)
        self.theaterCalendar.click_today_plus_two()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteJSON.write_movie_details(newDay, _jsonFileName)
        self.theaterCalendar.click_today_plus_three()
        TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteJSON.write_movie_details(newDay, _jsonFileName)
        self.theaterCalendar.click_today_plus_four()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteJSON.write_movie_details(newDay, _jsonFileName)
        self.theaterCalendar.click_today_plus_five()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteJSON.write_movie_details(newDay, _jsonFileName)
        self.theaterCalendar.click_today_plus_six()
        newDay = TheaterDetailPage.TheaterDetail(self.driver)
        FileOutput.WriteJSON.write_movie_details(newDay, _jsonFileName)

        newFileSize = os.path.getsize(_jsonFileName)
        self.assertLess(currentFileSize, newFileSize, "Did not write new data to JSON output file")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MovieInfoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

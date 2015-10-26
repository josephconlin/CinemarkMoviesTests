__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com header items
"""

import unittest
import selenium
import TestBrowser


class Header():
    # Class to define elements of the header
    def __init__(self, driver):
        self.movieSelector = driver.find_element_by_class_name("btn-search")
        self.searchText = driver.find_element_by_id("main_inp1")
        self.searchSubmit = driver.find_element_by_xpath('//input[contains(@src,\"btn-submit.gif\")]')

class HeaderTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser.TestBrowser().getbrowser()
        self.header = Header(self.driver)

    def tearDown(self):
        self.driver.quit()

    def testMovieSelection(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
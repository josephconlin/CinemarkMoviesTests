__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com header items
"""

import unittest
import appium


class Header():
    # Class to define elements of the header
    def __init__(self, driver):
        self.movieSelector = driver.find_element_by_class("btn-search")
        self.searchText = driver.find_element_by_id("main_inp1")
        self.searchSubmit = driver.find_element_by_xpath('//input[contains(@src,\"btn-submit.gif\")]')


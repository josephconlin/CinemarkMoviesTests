__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com theater detail page
"""

from TestBrowser import TestBrowser
from HeaderPage import Header

import unittest


class TheaterDetail():
    # Class to define elements of the theater detail page
    def __init__(self, driver):
        self.driver = driver
        self.theaterName = driver.find_element_by_class_name("inner-holder").find_element_by_tag_name("h1").text
        self._theaterMoviesListContainer = driver.find_element_by_class_name("content-box")
        self.theaterMoviesList = []
        # for theater in self._theaterListContainer.find_elements_by_class_name("type"):
        #     self.theatersList.append(theater.find_element_by_tag_name("a").text)


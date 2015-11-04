__author__ = 'Joseph Conlin'
"""
Page Object and tests for Cinemark.com theater detail page
"""

# from TestBrowser import TestBrowser
# from HeaderPage import Header
# from TheatersPage import Theaters
#
# import unittest


class MovieDetail:
    # Class to define details about a movie being shown at a specific theater
    def __init__(self, theaterMoviesListContainer, movieListIndex):
        self._movieInfoContainer = theaterMoviesListContainer.find_elements_by_class_name("item")[movieListIndex]
        self._movieNameContainer = self._movieInfoContainer.find_element_by_class_name("holder")

        self.movieName = self._movieNameContainer.find_element_by_tag_name("a").text
        # movieImageURL is obtained from the first img tag inside _movieInfoContainer so just use singular find_element
        self.movieImageURL = self._movieInfoContainer.find_element_by_tag_name("img").get_attribute("src")


class TheaterDetail:
    # Class to define elements of the theater detail page
    def __init__(self, driver):
        self.driver = driver
        self.theaterName = driver.find_element_by_class_name("inner-holder").find_element_by_tag_name("h1").text
        self._theaterMoviesListContainer = driver.find_element_by_class_name("movies-box")
        # self.theaterMoviesList = []
        # for theater in self._theaterListContainer.find_elements_by_class_name("type"):
        #     self.theatersList.append(theater.find_element_by_tag_name("a").text)


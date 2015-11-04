__author__ = 'Joseph Conlin'
"""
Page Object for Cinemark.com header items
"""

from random import randint


class Header:
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

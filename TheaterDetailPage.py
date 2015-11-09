__author__ = 'Joseph Conlin'
"""
Page Object for Cinemark.com theater detail page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MovieDetail:
    # Class to define details about a movie being shown at a specific theater
    def __init__(self, theaterMovieListContainer):
        self._movieNameContainer = theaterMovieListContainer.find_element_by_class_name("holder")
        # Note that sold out movies do not have the class used below and will not be captured in _movieShowTimeElements
        self._movieShowTimeElements = theaterMovieListContainer.find_elements_by_class_name("theatreShowtimeSingle")

        self.movieName = self._movieNameContainer.find_element_by_tag_name("a").text
        # movieImageURL is obtained from the first img tag inside _movieInfoContainer so just use singular find_element
        self.movieImageURL = theaterMovieListContainer.find_element_by_tag_name("img").get_attribute("src")
        self.movieShowTimeList = self.get_movie_show_times()

    def get_movie_show_times(self):
        """Return a list of strings of the format (m)m/(d)d/yyyy (h)h:mm[A,P]M, ie 11/5/2015 7:00PM"""
        showTimeList = []
        for showTime in self._movieShowTimeElements:
            showTimeList.append(showTime.get_attribute("title"))
        return showTimeList


class TheaterDetail:
    # Class to define elements of the theater detail page
    def __init__(self, driver):
        self.driver = driver
        # Sometimes need to wait for the page load to complete
        self._theaterMoviesListContainer = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "movies-box")))

        self.theaterName = driver.find_element_by_class_name("inner-holder").find_element_by_tag_name("h1").text
        self.theaterMoviesList = self.get_movies_list()

    def get_movies_list(self):
        movieList = []
        for movie in self._theaterMoviesListContainer.find_elements_by_class_name("item"):
            movieList.append(MovieDetail(movie))
        return movieList


class TheaterCalendar:
    # Class to define elements of the calendar item on the theater detail page.
    def __init__(self, driver):
        self.driver = driver
        self._theaterCalendarLinks = driver.find_element_by_class_name("week-item").find_elements_by_tag_name("a")

    """Using any of these click functions will cause a section of the TheaterDetail page to be changed.
       You will need new objects from this file to represent the new HTML page as the driver will have changed.
       Wait after the click so that the new page doesn't accidentally grab the old data elements
    """
    def click_today(self):
        self._theaterCalendarLinks[0].click()
        time.sleep(1)

    def click_today_plus_one(self):
        self._theaterCalendarLinks[1].click()
        time.sleep(1)

    def click_today_plus_two(self):
        self._theaterCalendarLinks[2].click()
        time.sleep(1)

    def click_today_plus_three(self):
        self._theaterCalendarLinks[3].click()
        time.sleep(1)

    def click_today_plus_four(self):
        self._theaterCalendarLinks[4].click()
        time.sleep(1)

    def click_today_plus_five(self):
        self._theaterCalendarLinks[5].click()
        time.sleep(1)

    def click_today_plus_six(self):
        self._theaterCalendarLinks[6].click()
        time.sleep(1)

    def click_more(self):
        self._theaterCalendarLinks[7].click()

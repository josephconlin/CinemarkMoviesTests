__author__ = 'Joseph Conlin'
"""
Classes for outputting movie information in various formats
"""
from TheaterDetailPage import TheaterDetail, MovieDetail

import os
import csv

# Setup common variables
_defaultFileName = "MovieInfo"


class WriteCSV:
    """Parse a given TheaterDetailPage.TheaterDetail object to write each show time on a single row as below:
       <theaterName>, <movieName>, <movieImageURL>, <showTime>
       Expect multiple rows per theater / movie combination
    """
    defaultFileExtension = ".csv"
    _csvHeader = ['TheaterName', 'MovieName', 'MovieImageURL', 'ShowTime']

    @staticmethod
    def write_movie_details(theaterDetail, fileName=_defaultFileName+defaultFileExtension):
        with open(fileName, 'a', newline='') as outFile:
            csvFile = csv.writer(outFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            # Check for empty file and write headers on first line if empty
            if os.path.getsize(fileName) == 0:
                csvFile.writerow(WriteCSV._csvHeader)
            for movieDetail in theaterDetail.get_movies_list():
                for showTime in movieDetail.get_movie_show_times():
                    csvFile.writerow([theaterDetail.theaterName, movieDetail.movieName, movieDetail.movieImageURL,
                                      showTime])

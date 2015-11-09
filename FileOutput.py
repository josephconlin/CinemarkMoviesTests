__author__ = 'Joseph Conlin'
"""
Classes for outputting movie information in various formats
"""
import os
import csv

from TheaterDetailPage import TheaterDetail, MovieDetail

# Setup common variables
_defaultFileName = "MovieInfo"


class WriteCSV:
    """Parse a given TheaterDetailPage.TheaterDetail object to write each show time on a single row as below:
       <theaterName>, <movieName>, <movieImageURL>, <showTime>
       Expect multiple rows per theater / movie combination
    """
    _defaultFileExtension = ".csv"
    _csvHeader = ['TheaterName', 'MovieName', 'MovieImageURL', 'ShowTime']

    def write_movie_details(self, theaterDetail, fileName=_defaultFileName):
        with open(fileName+WriteCSV._defaultFileExtension, 'w', newline='') as outFile:
            csvFile = csv.writer(outFile, delimiter=',')
            # Check for empty file and write headers on first line if empty
            if os.path.getsize(outFile) == 0:
                csvFile.writerow(WriteCSV._csvHeader)
            data = [theaterDetail.theaterName]
            for movieDetail in theaterDetail.get_movies_list():
                data.append(movieDetail.movieName)
                data.append(movieDetail.movieImageURL)
                for showTime in movieDetail.get_movie_show_times():
                    data.append(showTime)
                    csvFile.writerow(data)

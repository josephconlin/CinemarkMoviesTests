__author__ = 'Joseph Conlin'
"""
Classes for outputting movie information in various formats
"""
from TheaterDetailPage import TheaterDetail, MovieDetail

import os
import csv
# import xlwt
from openpyxl import Workbook, load_workbook

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


# class WriteExcel:
#     """Parse a given TheaterDetailPage.TheaterDetail object to write each show time on a single row as below:
#        <theaterName>, <movieName>, <movieImageURL>, <showTime>
#        Expect multiple rows per theater / movie combination
#     """
#     defaultFileExtension = ".xls"
#     _excelHeader = ['TheaterName', 'MovieName', 'MovieImageURL', 'ShowTime']
#
#     @staticmethod
#     def write_movie_details(theaterDetail, fileName=_defaultFileName+defaultFileExtension, row=0):
#         # Setup Excel data objects
#         wb = xlwt.Workbook()
#         ws = wb.add_sheet('Movie Info')
#
#         # Check for empty file and write headers on first line if empty
#         try:
#             # Use try to determine if file does not exist, use if inside try to determine if file exists with no data.
#             if os.path.getsize(fileName) == 0:
#                 pass
#         except FileNotFoundError:
#             pass
#         finally:
#             ws.write(row, 0, WriteExcel._excelHeader[0])
#             ws.write(row, 1, WriteExcel._excelHeader[1])
#             ws.write(row, 2, WriteExcel._excelHeader[2])
#             ws.write(row, 3, WriteExcel._excelHeader[3])
#             row += 1
#
#         for movieDetail in theaterDetail.get_movies_list():
#                 for showTime in movieDetail.get_movie_show_times():
#                     ws.write(row, 0, theaterDetail.theaterName)
#                     ws.write(row, 1, movieDetail.movieName)
#                     ws.write(row, 2, movieDetail.movieImageURL)
#                     ws.write(row, 3, showTime)
#                     row += 1
#
#         wb.save(fileName)
#         return row

class WriteExcel:
    """Parse a given TheaterDetailPage.TheaterDetail object to write each show time on a single row as below:
       <theaterName>, <movieName>, <movieImageURL>, <showTime>
       Expect multiple rows per theater / movie combination
    """
    defaultFileExtension = ".xlsx"
    _excelHeader = ['TheaterName', 'MovieName', 'MovieImageURL', 'ShowTime']

    @staticmethod
    def write_movie_details(theaterDetail, fileName=_defaultFileName+defaultFileExtension):
        # Check for empty file and write headers on first line if empty
        try:
            # Setup Excel data objects
            wb = Workbook()
            # Use try to determine if file does not exist, use if inside try to determine if file exists with no data.
            if os.path.getsize(fileName) == 0:
                ws = wb.active
                ws.append(WriteExcel._excelHeader)
                wb.save(fileName)
        except FileNotFoundError:
            ws = wb.active
            ws.append(WriteExcel._excelHeader)
            wb.save(fileName)

        # Load file that now exists and write data to it
        wb = load_workbook(filename = fileName)
        ws = wb.active
        for movieDetail in theaterDetail.get_movies_list():
                for showTime in movieDetail.get_movie_show_times():
                    ws.append([theaterDetail.theaterName, movieDetail.movieName, movieDetail.movieImageURL, showTime])

        wb.save(fileName)

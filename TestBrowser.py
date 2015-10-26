__author__ = 'Joseph Conlin'
"""Base class to represent possible browsers to be used in tests.
"""


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import Settings


class TestBrowser():
    def getbrowser(self):
        testdriver = webdriver.Remote(
            command_executor=Settings.seleniumHubURL,
            desired_capabilities=getattr(DesiredCapabilities, Settings.browserType))
        testdriver.get(Settings.baseURL)
        return testdriver

# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from .logger import logger
from .exceptions import BrowserLaunchError
from .config_loader import load_config


# The Browser Manager class:
class Browser:
    _driver = None  # Class variable (private)



    @classmethod
    def start(cls, browser_type="chrome", remote_url=None, config_path=None):   # The config_path here is for user's customizable path
        try:
            logger.info(f"Starting The Browser: {browser_type}")

            config = load_config(config_path)
            options = None   # Initialize the options and service, will update later
            service = None

            # Chrome logic:
            if browser_type.lower() == "chrome":
                options = ChromeOptions()
                driver_path = config.get("chrome")
                if not driver_path:
                    raise FileNotFoundError("Chrome Driver Path Not Specified In config.yaml")
                service = ChromeService(executable_path=driver_path)

                for arg in config.get("chrome_args", []):
                    options.add_argument(arg)

            # Edge logic:
            elif browser_type.lower() == "edge":
                options = EdgeOptions()
                driver_path = config.get("edge")
                if not driver_path:
                    raise FileNotFoundError("Edge Driver Path Not Specified In config.yaml")
                service = EdgeService(executable_path=driver_path)

                for arg in config.get("edge_args", []):
                    options.add_argument(arg)

            # Firefox logic:
            elif browser_type.lower() == "firefox":
                options = FirefoxOptions()
                driver_path = config.get("firefox")
                if not driver_path:
                    raise FileNotFoundError("Firefox Driver Path Not Specified In config.yaml")
                service = FirefoxService(executable_path=driver_path)


                for key, value in config.get("firefox_prefs", {}).items():
                    options.set_preference(key, value)

            else:
                raise ValueError(f"Not Supported Browser Type: {browser_type}")

            # Logic of dealing with remote url:
            if remote_url:
                logger.info(f"Utilizing Remote WebDriver: {remote_url}")
                cls._driver = webdriver.Remote(command_executor=remote_url, options=options)
            else:
                if browser_type.lower() == "chrome":
                    cls._driver = webdriver.Chrome(service=service, options=options)
                elif browser_type.lower() == "edge":
                    cls._driver = webdriver.Edge(service=service, options=options)
                elif browser_type.lower() == "firefox":
                    cls._driver = webdriver.Firefox(service=service, options=options)

                cls._driver.maximize_window()

            logger.info(f"{browser_type} Successfully Running")
            return cls._driver

        except Exception as e:
            logger.error(f"Error Occured When Trying To Start The Browser: {str(e)}")
            raise BrowserLaunchError(f"Failed To Start The Browser: {str(e)}")




    '''
    This method acts as a getter, 
    it returns the current driver object
    '''
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            raise BrowserLaunchError("Not Starting The Browser Yet, Please call Browser.start()")
        return cls._driver




    @classmethod
    def quit(cls):
        try:
            if cls._driver:
                logger.info("Closing the browser")
                cls._driver.quit()
                cls._driver = None
        except Exception as e:
            logger.error(f"Failed to close the browser: {str(e)}")



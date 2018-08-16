import requests

# from selenium import common
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

from akpy.time_mgmt import *
from akpy.stnd_vars import StandardMessages


msg_contactak = StandardMessages.msg_contactak


def get_chrome_webdriver(dirpath_dl,
                         prompt_for_download=False,
                         directory_upgrade=True,
                         safebrowsingenabled=True):
    print('[', time_stamp(), ']', 'DRIVER: starting chrome driver')

    check_internet_connection()
    # max_retries = 9
    # for i in range(max_retries):
    #     try:
    #         requests.get('https://google.com', timeout=3)
    #     except requests.exceptions.ConnectionError as e:
    #         print('[', time_stamp(), ']',
    #               'CONNECTION ERROR: internet connection could not be established\n',
    #               e)
    #         print('[', time_stamp(), '] RETRY', str(i+1) + ': process will retry')
    #         wait_sec(1, True)
    #         continue  # retrying
    #
    #     else:
    #         break
    # else:
    #     print('[', time_stamp(), ']',
    #           'CONNECTION ERROR: internet connection could not be established after', max_retries+1, 'attempts')
    #     print('ERROR Ref.: def get_chrome_webdriver')
    #     sys.exit(msg_contactak)

    # options = Options()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs",
                                    {"download.default_directory": dirpath_dl,
                                     "download.prompt_for_download": prompt_for_download,
                                     "download.directory_upgrade": directory_upgrade,
                                     "safebrowsing.enabled": safebrowsingenabled})
    driver = webdriver.Chrome(chrome_options=options)
    return driver


def quit_chrome_webdriver(driver):
    print('[', time_stamp(), ']', 'DRIVER: closing chrome driver')
    driver.quit()


def check_internet_connection(max_retries=9, url_to_test='https://google.com', timeout_sec=3):
    max_retries = max_retries
    for i in range(max_retries):
        try:
            requests.get(url_to_test, timeout=timeout_sec)
        except requests.exceptions.ConnectionError as e:
            print('[', time_stamp(), ']',
                  'CONNECTION ERROR: internet connection could not be established\n',
                  e)
            print('[', time_stamp(), '] RETRY', str(i+1) + ': process will retry')
            wait_sec(1, True)
            continue  # retrying

        else:
            break
    else:
        print('[', time_stamp(), ']',
              'CONNECTION ERROR: internet connection could not be established after', max_retries+1, 'attempts')
        print('ERROR Ref.: def check_interent_connection')
        sys.exit(msg_contactak)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome(executable_path="chromedriver.exe") as driver:
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.youtube.com/watch?v=zWmZhWCazw0&list=PLsaURXf-TfmS2QzlvQcYBl7D02kvfqRIp&ab_channel=DubstepGutter")
    titles = driver.find_elements_by_class_name("ytd-playlist-panel-video-renderer")
    # titles = driver.find_element_by_css_selector('h4.ytd-playlist-panel-video-renderer')

    for title in titles:
        print(title.text)
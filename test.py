from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# class_slector = "yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer"
class_slector = "ytd-playlist-panel-video-renderer"

with webdriver.Chrome(executable_path="chromedriver.exe") as driver:
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.youtube.com/watch?v=zWmZhWCazw0&list=PLsaURXf-TfmS2QzlvQcYBl7D02kvfqRIp&ab_channel=DubstepGutter")
    titles = driver.find_elements_by_class_name(class_slector)
    # titles = driver.find_element_by_css_selector('h4.ytd-playlist-panel-video-renderer')

    for title in titles:
        print(title.text)
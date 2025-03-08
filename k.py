import os
import time
import sys
from dataclasses import dataclass
from typing import Generator
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def loading_animation(message="Loading...", duration=5, animation_type="spinner"):
    """
    Displays a loading animation in the terminal.

    Args:
        message (str): The message to display alongside the animation.
        duration (int): The duration of the animation in seconds.
        animation_type (str): The type of animation to display. Options: "spinner", "bars", "dots".
    """
    start_time = time.time()
    end_time = start_time + duration

    if animation_type == "spinner":
        symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        while time.time() < end_time:
            for symbol in symbols:
                print(f"\r{symbol} {message}", end="")
                sys.stdout.flush()
                time.sleep(0.1)

    elif animation_type == "bars":
        bars = ["|", "/", "-", "\\"]
        while time.time() < end_time:
            for bar in bars:
                print(f"\r{bar} {message}", end="")
                sys.stdout.flush()
                time.sleep(0.2)

    elif animation_type == "dots":
        dots = ["", ".", "..", "..."]
        while time.time() < end_time:
            for dot in dots:
                print(f"\r{message}{dot}", end="")
                sys.stdout.flush()
                time.sleep(0.3)

    else:
        print("Invalid animation type.")
        return

    print(f"\r{message} \N{check mark} {' ' * (len(message) + 10)}") #clear the line, including extra characters.

# Example usage:
#loading_animation("Processing data...", duration=3, animation_type="spinner")
@dataclass
class UploadConfig:
    profile_path: str = "/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/ip6t33by.ShitassNigga"
    geckodriver_path: str = "/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/geckodriver"
    upload_file_path: str = "/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/t666.webm"
    screenshot_dir: str = "/home/runner/work/zace32wdawvgrwsaqq1/zace32wdawvgrwsaqq1/shit"
    upload_url: str = "https://www.youtube.com"
    title_text: str = "nee thanda driver 🤣🤣 #bgmi #bgmifunnymoments #bgmitamil #bgmishorts #shorts #fypシ゚viral #fyp #fypシ゚"
    description_text: str = "_1_"
    timeout: int = 10

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

class YouTubeUploader:
    def __init__(self, config: UploadConfig):
        self.config = config
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        options.add_argument("--log-level=3")
        options.add_argument("-profile")
        options.add_argument(self.config.profile_path)
        options.add_argument("-headless")
        driver = webdriver.Firefox(service=webdriver.firefox.service.Service(self.config.geckodriver_path), options=options)
        driver.implicitly_wait(5) #reduced implicit wait.
        return driver

    def _wait_and_click(self, locator, by=By.XPATH):
        WebDriverWait(self.driver, self.config.timeout).until(EC.presence_of_element_located((by, locator))).click()
        time.sleep(8)

    def _wait_and_send_keys(self, locator, keys, by=By.XPATH):
#        print("W : ", locator, keys , by)
        element = WebDriverWait(self.driver, self.config.timeout).until(EC.presence_of_element_located((by, locator)))
#        element.clear()
        element.send_keys(keys)
        time.sleep(20)
    def _wait_and_send_keyss(self, locator, keys, by=By.XPATH):
#        print(" sssssss: ", locator, keys , by)
        elementt = WebDriverWait(self.driver, self.config.timeout).until(EC.presence_of_element_located((by, locator)))
        elementt.clear()
        elementt.send_keys(keys)

    def _take_screenshot(self, filename):
        self.driver.save_screenshot(os.path.join(self.config.screenshot_dir, filename))

    def _upload_steps(self) -> Generator[tuple[str, str, str, By], None, None]:
        yield ("//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]", "d4.png", "Click Create Button", By.XPATH)
        yield ("ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)", "d5.png", "Clicked Upload Video", By.CSS_SELECTOR)
        yield ("//*[@id=\"content\"]/input", "d6.png", "Uploading Video", By.XPATH)
        yield ("div.title ytcp-social-suggestion-input > div", "d7.png", "setting up title", By.CSS_SELECTOR)
        yield ("div.description ytcp-social-suggestion-input > div", "d8.png", "setting up description", By.CSS_SELECTOR)
        yield ("ytkc-made-for-kids-select tp-yt-paper-radio-button:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1)", "d9.png", "selected Not for kids", By.CSS_SELECTOR)
        yield ("//ytcp-button[@id='next-button']/ytcp-button-shape[@class='style-scope ytcp-button']", "d11.png", "clicked next button", By.XPATH)
        yield ("//ytcp-button[@id='next-button']/ytcp-button-shape[@class='style-scope ytcp-button']", "d12.png", "  ", By.XPATH)
        yield ("//ytcp-button[@id='next-button']/ytcp-button-shape[@class='style-scope ytcp-button']", "d13.png", "  ", By.XPATH)
        yield ("tp-yt-paper-radio-button:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1)", "d14.png", "selecting public", By.CSS_SELECTOR)
        yield ("//ytcp-button[@id='done-button']/ytcp-button-shape[@class='style-scope ytcp-button']", "d15.png", "Published", By.XPATH)

    @timeit
    def upload(self):
        try:
            self.driver.get(self.config.upload_url)
            self._take_screenshot("start.png")
            print(dir(self.driver))
            time.sleep(5)
            
            for locator, screenshot, __, by in self._upload_steps():
#                print("LOCATOR : ", locator, "SCREENSHOT : ", screenshot)
                loading_animation(f"{__}", duration=10, animation_type="spinner")
                if locator == "//*[@id=\"content\"]/input":
                    self._wait_and_send_keys(locator, self.config.upload_file_path, by)
                elif locator == "div.title ytcp-social-suggestion-input > div":
                    self._wait_and_send_keyss(locator, self.config.title_text, by)
                elif locator == "div.description ytcp-social-suggestion-input > div":
                    self._wait_and_send_keyss(locator, self.config.description_text, by)
                else:
                    self._wait_and_click(locator, by)
                self._take_screenshot(screenshot)
#            self._take_screenshot("d10.png")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error: {e}")
            self._take_screenshot("error_screenshot.png")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    config = UploadConfig()
    uploader = YouTubeUploader(config)
    uploader.upload()

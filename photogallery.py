import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver path and options
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# Navigate back to the home page
#open first window
driver.get("https://labour.gov.in/")

firstwindow = driver.window_handles[0]
#sleep for 2 seconds
time.sleep(3)

# Navigate to the "Media" menu and then to "Photo Gallery"
media_menu = driver.find_element(By.LINK_TEXT, "Media")
#click on the media_menu
media_menu.click()
#navigate to the allpressrelease
allpreseerelease = driver.find_element(By.LINK_TEXT,"Click for more info of Press Releases")
#click on the allpressrelease
allpreseerelease.click()
#navigate to the photo-gallery_menu
photo_gallery_menu = driver.find_element(By.LINK_TEXT, "Photo Gallery")
#click on the photo_gallery_menu
photo_gallery_menu.click()
#sleep 5 seconds
time.sleep(5)


#window_handles
driver.switch_to.window(driver.window_handles[1])
firstright = driver.window_handles[-1]
#navigate to new window
driver.switch_to.window(firstright)
#sleep for 2 sec
time.sleep(2)

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".views-field-field-image img")))

# Create a folder to store the photos
photo_folder = r"C:\Users\HP\OneDrive\Desktop\photo_gallery.py"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

# Download the first 10 photos from the photo gallery
photos = driver.find_elements(By.CSS_SELECTOR, ".views-field-field-image img")[:10]
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute('src')
    if not photo_url.startswith('http'):
        photo_url = "https://labour.gov.in" + photo_url  # Ensure the URL is absolute
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), 'wb') as file:
        file.write(photo_response.content)
    print(f"Downloaded photo {index + 1}")

print("Photos downloaded successfully.")
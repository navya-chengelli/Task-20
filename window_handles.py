import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Initialize the WebDriver
driver = webdriver.Chrome()
# Open the homepage
driver.get("https://www.cowin.gov.in/")
# Wait  the page is fully loaded (adjust time as needed)
time.sleep(5)
# Find and click the "FAQ" link to open in a new window
faq_link = driver.find_element(By.XPATH, "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")
faq_link.click()
time.sleep(2)  # Wait for the new window to open
# Find and click the "Partners" link to open in a new window
partners_link = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')
partners_link.click()
time.sleep(2)  # Wait for the new window to open
# Get all window handles
all_window_handles = driver.window_handles
# Display the window handles on the console
print("All window handles:", all_window_handles)
# Identify the handles for the homepage and the two new windows
homepage_handle = driver.current_window_handle
new_window_handles = [handle for handle in all_window_handles if handle != homepage_handle]
# Display the handles for the new windows
print("New window handles:", new_window_handles)
# Close the new windows
for handle in new_window_handles:
    driver.switch_to.window(handle)
    driver.close()
# Switch back to the homepage window
driver.switch_to.window(homepage_handle)
# Confirm the current window is the homepage
print("Current window handle (should be homepage):", driver.current_window_handle)
#  navigate to the homepage again
driver.get("https://www.cowin.gov.in/")
time.sleep(3)
# Quit the WebDriver
driver.quit()
#
##############################################################################################################





























# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# import os
#
# # Initialize the WebDriver (make sure you have the appropriate driver executable installed and in your PATH)
# driver = webdriver.Chrome()
#
# # URL of the webpage containing the photos
# url = "https://labour.gov.in/"
#
# # Navigate to the webpage
# driver.get(url)
#
# # Create a folder to save downloaded photos
# os.makedirs('downloaded_photos', exist_ok=True)
#
# # Locate the photos (adjust the selector based on the webpage structure)
# photos = driver.find_elements(By.TAG_NAME, 'img')
#
# # Extract the URLs and download the photos
# for index, photo in enumerate(photos):
#     photo_url = photo.get_attribute('src')
#     try:
#         response = requests.get(photo_url)
#         if response.status_code == 10:
#             file_path = os.path.join('downloaded_photos', f'photo_{index + 1}.jpg')
#             with open(file_path, 'wb') as file:
#                 file.write(response.content)
#             print(f'Downloaded {file_path}')
#         else:
#             print(f'Failed to download {photo_url} (status code: {response.status_code})')
#     except Exception as e:
#         print(f'Error downloading {photo_url}: {e}')
#
# # Close the WebDriver
# driver.quit()

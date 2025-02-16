from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass 



EMAIL = input("Enter your LinkedIn email: ")
PASSWORD = getpass.getpass("Enter your LinkedIn password: ")

JOB_TITLE = "Python Developer"
LOCATION = "India"

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keep browser open
driver = webdriver.Chrome(options=chrome_options)

# Open LinkedIn Jobs
driver.get("https://www.linkedin.com/jobs")
time.sleep(3)

# Login
login_email = driver.find_element(By.ID, "session_key")
login_email.send_keys(EMAIL)

login_password = driver.find_element(By.ID, "session_password")
login_password.send_keys(PASSWORD)
login_password.send_keys(Keys.ENTER)

time.sleep(5)

easy_apply = driver.find_element(By.ID,value="ember56")
# print(easy_apply.get_attribute("id"))
easy_apply.click()

mobile_no = driver.find_element(By.XPATH,value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4133040107-14609380068-phoneNumber-nationalNumber"]')
mobile_no.send_keys("",Keys.ENTER)

next_button = driver.find_element(By.CSS_SELECTOR,value='.pv4 button')
# print(next_button.get_attribute("class"))
next_button.click()


review_button = driver.find_element(By.XPATH,value='//*[@id="ember345"]')
review_button.click()

submit_application = driver.find_element(By.XPATH,value='//*[@id="ember355"]')
submit_application.click()
# driver.quit()

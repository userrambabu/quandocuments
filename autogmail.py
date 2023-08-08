from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium webdriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the Gmail link and click it
gmail_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='Gmail']"))
    )
gmail_link.click()

# Wait for Gmail to load
time.sleep(3)

# Find the Email input field and enter the username
email_input = driver.find_element_by_id("identifierId")
email_input.send_keys("ecekingstar@gmail.com")

# Press Enter or click Next
email_input.send_keys(Keys.ENTER)
# Alternatively, you can click the "Next" button if available
# next_button = driver.find_element_by_id("identifierNext")
# next_button.click()

# Wait for password input field to load
time.sleep(3)

# Find the Password input field and enter the password
password_input = driver.find_element_by_name("password")
password_input.send_keys("ram93ram93")

# Press Enter or click Login
password_input.send_keys(Keys.ENTER)
# Alternatively, you can click the "Login" button if available
# login_button = driver.find_element_by_id("passwordNext")
# login_button.click()

# Wait for Gmail to load after login
time.sleep(5)

# Find the Compose button and click it
compose_button = driver.find_element_by_xpath("//div[text()='Compose']")
compose_button.click()

# Wait for the compose window to load
time.sleep(3)

# Find the To field and enter the recipient email
to_field = driver.find_element_by_name("to")
to_field.send_keys("rambabuas93@gmail.com")

# Find the Subject field and enter the email subject
subject_field = driver.find_element_by_name("subjectbox")
subject_field.send_keys("Test Email")

# Find the email body field and enter the email content
body_field = driver.find_element_by_xpath("//div[@aria-label='Message Body']")
body_field.send_keys("This is a test email.")

# Find the Send button and click it to send the email
send_button = driver.find_element_by_xpath("//div[text()='Send']")
send_button.click()

# Wait for the email to be sent
time.sleep(3)

# Close the browser
driver.quit()

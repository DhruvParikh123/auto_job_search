# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# service = Service("D:\job_find\chrome-win32\chrome.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://google.com")
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# service = Service(r"D:\job_find\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# wait = WebDriverWait(driver, 20)

# # Open LinkedIn
# driver.get("https://www.linkedin.com/jobs/")

# # Click Sign in
# sign_in = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign in')]"))
# )
# sign_in.click()

# # Click Continue with Google
# google_btn = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Continue with Google')]/ancestor::div[@role='button']"))
# )
# google_btn.click()

# # ===== IMPORTANT: Switch to Google login window =====
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[-1])

# # ===== Enter Email =====
# email_input = wait.until(
#     EC.presence_of_element_located((By.ID, "identifierId"))
# )

# email_input.send_keys("parikhdhruv05@gmail.com")

# # Click Next
# next_btn = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/ancestor::button"))
# )

# next_btn.click()

# time.sleep(50)
# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver path
service = Service(r"D:\job_find\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Credentials
email = "parikhdhruv05@gmail.com"
password = "dhruvparikh@1234"

# Open LinkedIn Jobs page
driver.get("https://www.linkedin.com/jobs/")

# Login email
email_input = wait.until(
    EC.presence_of_element_located((By.ID, "session_key"))
)
email_input.send_keys(email)

# Login password
password_input = wait.until(
    EC.presence_of_element_located((By.ID, "session_password"))
)
password_input.send_keys(password)

# Click login
sign_in_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
sign_in_btn.click()

# Wait for jobs page load
wait.until(EC.url_contains("jobs"))

# 🔍 Job search box (IMPORTANT PART)
job_search = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='typeahead-input']"))
)

job_search.clear()
job_search.send_keys("Python Developer 3 years experience")

# Optional: press ENTER to search
from selenium.webdriver.common.keys import Keys
job_search.send_keys(Keys.ENTER)

print("Job search executed successfully!")

time.sleep(10)
driver.quit()
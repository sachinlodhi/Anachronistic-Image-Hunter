from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com")
driver.find_element(By.ID,"email").send_keys("sachinlodhi8614@gmail.com")
driver.find_element(By.ID,"pass").send_keys("hellothere")
driver.find_element(By.ID,"u_0_b").click()
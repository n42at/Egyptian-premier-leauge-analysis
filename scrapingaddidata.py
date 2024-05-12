from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service, options=options)
driver.execute("get", {'url': "https://www.365scores.com/football/league/premier-league-552/standings"})
#driver.get("https://www.365scores.com/football/league/premier-league-552/stats")
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[1]/div[2]/button'))).click()

table_body = driver.find_element(By.XPATH, "//tbody")
rows = table_body.find_elements(By.TAG_NAME, "tr")
all_data = []
for row in rows[1:]:
    table_data = row.find_elements(By.TAG_NAME, "td")
    row_data = []
    for data in table_data:
        row_data.append(data.text)
    row_data = row_data[1:10]
    all_data.append(row_data)
    print(row_data)
    
headers = ['Team position', 'Club', 'Matches played','F:A','Goal Difference','PTS','W','D','L'] 
print(all_data)
with open('table.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  # existing code to get row_data
  writer.writerows(all_data)

driver.quit()
    
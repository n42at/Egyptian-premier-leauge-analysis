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
driver.execute("get", {'url': "https://www.365scores.com/football/league/premier-league-552/stats"})
#driver.get("https://www.365scores.com/football/league/premier-league-552/stats")
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[1]/div[2]/button'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/main/div[5]/div/div/div/div[1]/div[2]/div[4]'))).click()
time.sleep(4) 
#add timeout element
#driver.implicitly_wait(10) 

goalscorers = driver.find_elements(By.CLASS_NAME,"entity-stats-widget_row__sCcPB")
#goalsnums = driver.find_elements(By.CLASS_NAME,"entity-stats-widget_entity_text__oNWJS")

#element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".selector")))

#goalscorers = driver.find_elements_by_class_name("entity-stats-widget_row__sCcPB")
counter=0
names = []
goalsar = []
clubs = []
positions = []
player_images = []
for goalscorer in goalscorers:
    counter += 1
    if counter > 20:
        break
    name = goalscorer.find_element(By.CLASS_NAME, "entity-stats-widget_player_name__WvQPB").text
    names.append(name)
    goals = goalscorer.find_element(By.CLASS_NAME, 'entity-stats-widget_stats_value__des13').text
    goalsar.append(goals)
    #goals_int = int(goals)
    #print("goals: " + goals_int)
    #print("name: " + name)
    #name = goalscorer.find_element_by_xpath("/html/body/div[2]/div/main/div[5]/div/div/div/div[1]/div[2]/div[2]/a[1]/div[1]/div/div[1]/span[1]").text
    club = goalscorer.find_element(By.CLASS_NAME,"entity-stats-widget_entity_competitor_name__pXZcQ").text
    clubs.append(club)
    #print("club: "+club)
    position = goalscorer.find_element(By.CLASS_NAME,"entity-stats-widget_entity_position_name__D6PpA").text
    positions.append(position)
    #print("position: " + position)

    #webscrape numbers
    

for i in range(1,21):
    image_elements = driver.find_elements(By.CSS_SELECTOR, "body > div.app-module-router-container.scores365app.direction-ltr.support-hover > div > main > div.website_main__jLpbE > div > div > div > div:nth-child(1) > div.entity-stats-widget_table__xlIar > div.list_container__AMVNC > a:nth-child(" + str(i) + ") > div.entity-stats-widget_entity__9mqaq > img")
    for element in image_elements:
        image_url = element.get_attribute("src")
        player_images.append(image_url)
    



image_elements_res = driver.find_elements(By.XPATH, '//*[@id="collapsible-content-1708493060195"]/div/div/a[2]/div[1]/img')
for element in image_elements_res:
    image_url2 = element.get_attribute("src")
    player_images.append(image_url2)
      
print(names,clubs, positions, goalsar,player_images)



#collapsible-content-1708495466082 > div > div > a:nth-child(1) > div.entity-stats-widget_entity__9mqaq
# Add a short wait 
with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    header = ['Name', 'Clubs', 'Positions','Goals','player images'] 
    writer.writerow(header)
    for name, goals, club,position in zip(names, goalsar, clubs, positions,player_images):
        writer.writerow([name, club, position, goals]) 
        

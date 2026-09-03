# Task 6

import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver config
options = webdriver.ChromeOptions()
options.add_argument('--headless')  
options.add_argument('--headless=new')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),options=options
)

# create empty list for dict values
owasp_vulnerabilities = []

try:
    # load owasp top ten project webpage
    driver.get("https://owasp.org/www-project-top-ten/")
    
    # find webpage title
    webpage_title = driver.title 
    # print(f"Webpage title: {webpage_title}")
    
    # wait 5 seconds
    time.sleep(5)
    
    # find webpage body
    body = driver.find_element(By.CSS_SELECTOR, 'body')

    if body:
        # find anchor tag web elements on main page
        web_elements = driver.find_elements(By.TAG_NAME, "a")
        # print(f"\nLocated {len(web_elements)} main page links\n")
        
        # create empty list for results
        # vulnerability_results = []

    # iterate through list of web elements
    for entry in web_elements:
        # if web element exists
        if entry:
            # get title
            element_title = entry.text.strip()
            # print(f"Element title: {element_title}")

            # get link
            element_link = entry.get_attribute("href") 
            # print(f"Element link: {element_link}\n")

            # if specific title and link found
            if element_title == "OWASP Top Ten 2025" and element_link:
                # print(f"Navigating to OWASP Top 10:2025 List: {element_link}\n")
                # stop loop
                break

    # if element link exists
    if element_link:
        # load target page
        driver.get(element_link)
        
        # find anchor tag web elements on target page
        vulnerability_elements = driver.find_elements(By.TAG_NAME, "a")
        # print(f"Located {len(vulnerability_elements)} target page links\n")
        
        # iterate through list of web elements
        for entry in vulnerability_elements:
            # if web element exists
            if entry:
                # strip whitespace
                vulnerability_title = entry.text.strip()
                # print(f"Vulnerability: {vulnerability_title}")

                # filter titles that start with A and contain :2025
                if vulnerability_title.startswith("A") and ":2025" in vulnerability_title:
                    # print(f"Vulnerability: {vulnerability_title}")
                      
                    # get link
                    vulnerability_link = entry.get_attribute("href")
                    # print(f"Link: {vulnerability_link}\n")
                    
                    # create dict for results
                    vulnerability_results = {
                        "title": vulnerability_title,
                        "link": vulnerability_link
                    }
                    # print(f"Vulnerability results: {vulnerability_results}\n")

                    # add vulnerability_results to final dict
                    owasp_vulnerabilities.append(vulnerability_results)

    # print(f"Vulnerabilities: {owasp_vulnerabilities}")

except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")

finally:
    # close browser connection
    driver.quit()

# ///////////////////////////////////////

import csv

# write owasp_vulnerabilities to owasp_top_10.csv
with open('owasp_top_10.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writerows(owasp_vulnerabilities)

print(f"Successfully saved vulnerabilities to csv.")
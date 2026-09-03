# Task 2

list_item_tag = "li"
list_item_class = "cp-search-result-item"
title_class = "cp-title"
author_link_class = "author-link"
format_div_class = "cp-search-result-item-content"
format_label_class = "cp-format-label"

# /////////////////////////////////

# Task 3

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
results = []

try:
    # load durham county library page
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart&locale=en-US")
    
    # find webpage title
    webpage_title = driver.title 
    # print(f"Webpage title: {webpage_title}")
    
    # wait 5 seconds
    time.sleep(5)
    
    # find page body
    body = driver.find_element(By.CSS_SELECTOR, 'body')

    if body:
        
        # construct book list css selector
        list_css_selector = f"{list_item_tag}.{list_item_class}"

        # find book search results within page body
        books_list = body.find_elements(By.CSS_SELECTOR, list_css_selector)
        # print(f"Located {len(books_list)} search results.\n")
        
        # iterate through list of book entries
        for book in books_list:

            # find book titles
            title_elements = book.find_elements(By.CLASS_NAME, title_class)

            # if book titles found
            if len(title_elements) > 0:

                # strip whitespace from title
                title_text = title_elements[0].text.strip()
                # print(f"Book title: {title_text}")
                
            # find book authors
            author_elements = book.find_elements(By.CLASS_NAME, author_link_class)
            
            # if book authors found
            if len(author_elements) > 0:

                # create empty list for authors
                author_names = []

                # iterate through links to get authors
                for link in author_elements:

                    # strip whitespace from link text
                    name = link.text.strip()

                    # if name exists
                    if name:

                        # add to author_names list
                        author_names.append(name)
                
                # join multiple authors with semicolon
                if len(author_names) > 0:
                    author_text = "; ".join(author_names)
                    # print(f"Book author(s): {author_text}")
                
            # find div containers that contain book formats
            format_div = book.find_elements(By.CLASS_NAME, format_div_class)

            # if div containers found
            if len(format_div) > 0:

                # strip whitespace from text
                context_text = format_div[0].text.strip()
                # print(f"Text: {context_text}")
                
                # split text into lines
                text_lines = context_text.split("\n")
                # print(f"Lines: {text_lines}")
                
                # iterate through lines
                for line in text_lines:

                    # if format keyword found
                    if "eBook" in line or "Audiobook" in line or "Book" in line:

                        # strip whitespace from line
                        format_year_text = line.strip()
                        # print(f"Format, Year: {format_year_text}")
            
            # create dict for above values
            books_dict = {
                "Title": title_text,
                "Author": author_text,
                "Format-Year": format_year_text
            }
            
            # append dict to results list
            results.append(books_dict)

    # create df from list of dicts
    books_df = pd.DataFrame(results)
    print(f"\nBooks DataFrame:\n{books_df}")

except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")

finally:
    # close browser connection
    driver.quit()

# /////////////////////////////////

# Task 4

import csv
import json

# write books_df to get_books.csv
with open('get_books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Format-Year"])

    for book in results:
        writer.writerow([book["Title"], book["Author"], book["Format-Year"]])

print(f"Successfully saved df to csv.")

# write results list to get_books.json
# indent=4 makes file human-readable
with open('get_books.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, indent=4, ensure_ascii=False)
    
print(f"Successfully saved results to JSON.")

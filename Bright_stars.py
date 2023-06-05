from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# IMP NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future, hence the current data might be different.
# Perform data scraping from scratch with HTML Tags/Class Names!


# URLto Scrape Data
bright_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

# Get Page
page = requests.get(bright_url)

# Parse Page
soup = bs(page.text,'html.parser')

# Get <table> with class = 'wikitable sortable'
star_table = soup.find('table')



temp_list= []

# IMP NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future.
# Hence check the index number poperly for star_table[1]
# Currently, there are there 3 table with class = "class":"wikitable sortable" and "Field brown dwarfs" Table is the 2nd table
# Thus the index is 1
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum=[]


for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius',"Luminosity"]  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=headers)
print(df2)

df2.to_csv('bright_stars.csv', index=True, index_label="id")

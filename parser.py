from bs4 import BeautifulSoup 
import requests 
 
url = 'https://www.isscheb.eu/jmenny-telefonni-seznam/' 
response = requests.get(url) 
soup = BeautifulSoup(response.text, 'html.parser') 
 
tables = soup.find_all(class_='tablepress') 
 
if tables: 
 
    table = tables[0] 
 
    with open('table_data.txt', 'w') as file: 
  
        for row in table.find_all('tr'): 
            cells = row.find_all('td') 
            if cells: 
                row_data = [cell.text.strip() for cell in cells] 
                file.write('\t'.join(row_data) + '\n') 
else: 
    print("Tabulka nebyla nalezena.")

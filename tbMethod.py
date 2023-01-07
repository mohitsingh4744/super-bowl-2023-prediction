from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
def tableMethod(year, input_id, url2):
    url = url2.format(year)
    page = requests.get(url)
    soup = BeautifulSoup(re.sub("<!--|-->", "", page.text), "lxml")
    table1 = soup.find('table', id=input_id)
    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title)
    temp = []
    for i in headers:
        if (i != ''):
            temp.append(i)
    headers = temp
    del headers[len(headers) - 32:]
    place = False
    local = []
    for j in headers:
        if(j=='Tm'):
            place = True
        if(place == False):
            local.append(j)
    for i in local:
        headers.remove(i)
    df = pd.DataFrame(columns=headers)
    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(df)
        if(len(row) != 0):
            df.loc[length] = row
    return df
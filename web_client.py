import pandas as pd
import requests

print(pd.read_csv('1.csv'))

HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnROYW1lIjoid2ViYXBwLXYzMSIsInNjb3BlIjoic3RhdGljLWNvbnRlbnQtYXBpLGN1cmF0aW9uLWFwaSxuZXh4LWNvbnRlbnQtYXBpLXYzMSx3ZWJhcHAtYXBpIn0.mbuG9wS9Yf5q6PqgR4fiaRFIagiHk9JhwoKES7ksVX4',
}

res1 = requests.get('http://pbom.dev/', headers=HEADERS)

res2 = requests.get('http://ox.security/', allow_redirects=True)

res3 = requests.get('https://megalinter.io/', verify=False)


import json
import re
import requests
from bs4 import BeautifulSoup


url = "https://www.worldometers.info/coronavirus/usa/california/"
html = requests.get(url).text

scripts = [
    script.string for script in
    BeautifulSoup(html, "lxml").find_all("script", {"type": "text/javascript"})
    if script.string is not None
]

graph_titles = [
    "Active Cases",
    "Total Coronavirus Cases",
    "Total Coronavirus Deaths",
]

output = {}

for script in scripts:
    scrip_body = script.string
    # print(scrip_body)
    for title in graph_titles:
        if title in scrip_body:
            c = re.search(r"categories: \[(.*)\]", script.string).group(1)
            d = re.search(r"data: \[(.*)\]\s+}", script.string).group(1).split(",")
            output[title] = {
                "dates": re.findall(r"[A-Za-z]{3} \d{1,2}, \d{4}", c),
                "series": d,
            }
        else:
            continue
print(output)
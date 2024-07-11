import requests
import os
import re

def fetch_urls(domain):
    command = f"echo {domain} | waybackurls"
    result = os.popen(command).read()
    urls = result.splitlines()
    print(f"Fetched {len(urls)} URLs")
    return urls

def fetch_content(urls):
    content = {}
    for url in urls:
        if url:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    content[url] = response.text
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
        else:
            print("Empty URL encountered")
    return content

def search_for_keywords(content, keywords):
    leaks = {}
    for url, text in content.items():
        for keyword in keywords:
            if re.search(keyword, text, re.IGNORECASE):
                if url not in leaks:
                    leaks[url] = []
                leaks[url].append(keyword)
    return leaks

domain = "https://ENTERWEBSITEURLHERE.com"
keywords = ["ENTER", "KEYWORDS", "HERE"]

urls = fetch_urls(domain)
content = fetch_content(urls)
leaks = search_for_keywords(content, keywords)

with open("potential_leaks.txt", "w") as f:
    for url, found_keywords in leaks.items():
        f.write(f"URL: {url}\nKeywords: {', '.join(found_keywords)}\n\n")

print("Search completed. Check potential_leaks.txt for results.")

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wayback Password Leak Search</title>
</head>
<body>

<h1>Wayback Password Leak Search</h1>

<p>This script automates the process of fetching archived URLs from the Wayback Machine for a given domain, retrieving their content, and searching for potential password leaks using specified keywords.</p>

<h2>Prerequisites</h2>
<p>Ensure you have the following installed:</p>
<ul>
  <li>Python 3.x</li>
  <li><code>requests</code> library for Python</li>
  <li><code>waybackurls</code> tool</li>
</ul>

<h2>Installation</h2>

<h3>Install Python Requests Library</h3>
<p>Install the <code>requests</code> library using pip:</p>
<pre><code>sudo apt update
sudo apt install python3-pip
pip3 install requests
</code></pre>

<h3>Install waybackurls</h3>
<p>Install <code>waybackurls</code> using Go:</p>
<pre><code>go get -u github.com/tomnomnom/waybackurls
</code></pre>

<h2>Usage</h2>

<ol>
  <li>
    <p><strong>Save the Script</strong></p>
    <p>Save the following script as <code>search_password_leaks.py</code>:</p>
    <pre><code>import requests
import os
import re
import concurrent.futures

def fetch_urls(domain):
    command = f"echo {domain} | waybackurls"
    result = os.popen(command).read()
    urls = result.splitlines()
    print(f"Fetched {len(urls)} URLs")
    return urls

def fetch_content(url):
    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return url, response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return url, None

def search_for_keywords(content, keywords):
    leaks = {}
    for url, text in content.items():
        if text:
            for keyword in keywords:
                if re.search(keyword, text, re.IGNORECASE):
                    if url not in leaks:
                        leaks[url] = []
                    leaks[url].append(keyword)
    return leaks

domain = "https://ENTERURLHERE.com"
keywords = ["password", "pwd", "login", "credentials"]

urls = fetch_urls(domain)
content = {}

# Fetch content concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future_to_url = {executor.submit(fetch_content, url): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url, data = future.result()
        if data:
            content[url] = data

leaks = search_for_keywords(content, keywords)

with open("potential_leaks.txt", "w") as f:
    for url, found_keywords in leaks.items():
        f.write(f"URL: {url}\nKeywords: {', '.join(found_keywords)}\n\n")

print("Search completed. Check potential_leaks.txt for results.")
</code></pre>
  </li>
  <li>
    <p><strong>Run the Script</strong></p>
    <p>Execute the script by running:</p>
    <pre><code>python3 search_password_leaks.py
</code></pre>
  </li>
  <li>
    <p><strong>Check the Output</strong></p>
    <p>The results will be saved in <code>potential_leaks.txt</code> in the same directory. You can view the file using:</p>
    <pre><code>cat potential_leaks.txt
</code></pre>
  </li>
</ol>

<h2>License</h2>
<p>NONE</p>

<h2>Contributing</h2>
<p>Contributions are welcome! Please open an issue or submit a pull request with your changes.</p>

</body>
</html>

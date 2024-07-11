<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Wayback Keyword Search</h1>

<p>This script automates the process of fetching archived URLs from the Wayback Machine for a given domain, retrieving their content, and searching for potential  leaks using specified keywords.</p>

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
    <p>Save the script as <code>search_leaks.py</code></p> 
    <p>And be sure to change the URL and add the KEYWORDS to the script before saving!</p>

  </li>
  <li>
    <p><strong>Run the Script</strong></p>
    <p>Execute the script by running:</p>
    <pre><code>python3 search_leaks.py
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

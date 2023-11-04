import httpx
from bs4 import BeautifulSoup
from rich import print

# Get webpage and html code
print("Please enter a webpage url to get title of:")
site = httpx.get(input())
code = site.text

# Get title of webpage
title = BeautifulSoup(code, 'html.parser').title
title = str(title)
start = title.find(">")
end = title[1:].find("<")
title = title[start+1:end+1]
print("[yellow]Title:[/yellow] [bold green]" + title + "[/bold green]")

# Send fireworks emoji
print(":fireworks:")
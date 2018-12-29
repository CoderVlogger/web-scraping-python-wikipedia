import bs4
import requests


response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

if response is not None:
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    title = html.select("#firstHeading")[0].text
    paragraphs = html.select("p")
    for para in paragraphs:
        print (para.text)

    intro = '\n'.join([ para.text for para in paragraphs[0:5]])
    print (intro)

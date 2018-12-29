import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

page = wiki_wiki.page('Python_(programming_language)')
print(page.summary)

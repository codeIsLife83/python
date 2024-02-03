import re
import urllib.request
import html

# https://www.dictionary.com/browse/start

listofwords = ["finish", "conclude", "commence", "initiate", "launch", "open", "originate", "set", "stop", "close", "halt", "conclude", "end", "finish", "terminate"]

def get_definition(word):
    url = "https://www.dictionary.com/browse/" + word
    htmltext = urllib.request.urlopen(url).read()
    htmltext = htmltext.decode("utf-8")
    m = re.search('data-type="word-definition-content"><p>', htmltext)
    section = htmltext[m.end() : m.end() + 300]
    m = re.search("</p>", section)
    section = section[: m.start()]
    definition = section.split(";")[0]
    return html.unescape(definition)

search = input("would you like to search a word? (yes/no)")
if search == "yes":
    word = input("what word would you like to search?")
    print(get_definition(word))
else:
    print("ok, here are the synonyms for some words:")
    for word in listofwords:
        print(word + ": " + get_definition(word))

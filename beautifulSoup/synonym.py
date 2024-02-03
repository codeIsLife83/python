import requests
from bs4 import BeautifulSoup


def getSynonym(word):
    url = f"https://www.thesaurus.com/browse/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        synonym_element = soup.find(
            "a",
            {"class": "KmScG4NplKj_3H5E3oA_"},
        )
        synonym = synonym_element.text.strip()
        return synonym
    else:
        return "Failed to retrieve antonym information."


word = input("Enter a word: ")
antonym = getSynonym(word)
print(f"Synonym for {word}: {antonym}")

# SynonymAndAntonymCard-module_s100_a649c1b836994a8ffdc7 SynonymAndAntonymCard-module_antonym_d70dabe8d34f0b3020a3

import requests
import wikipedia

def initialize():
    """
    The initialize function downloads a list of words from the internet, sorts them by how many hits they get, then sorts them by the rarest few
    :return: A list of 1000 words
    """
    url = "https://raw.githubusercontent.com/jeremy-rifkin/Wordlist/master/master.txt"
    response = requests.get(url)
    words = response.text.split("\n")
    words = [word for word in words if len(word) > 3]
    words = words[:1000]
    words.sort(key=lambda word: len(requests.get(f"https://www.google.com/search?q={word}").text))

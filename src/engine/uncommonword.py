import requests
import wikipedia

url = "https://raw.githubusercontent.com/jeremy-rifkin/Wordlist/master/master.txt"

response = requests.get(url)

words = response.text.split("\n")

words = [word for word in words if len(word) > 3]

words = words[:1000]

words.sort(key=lambda word: wikipedia.search(word)[0].lower() == word.lower())

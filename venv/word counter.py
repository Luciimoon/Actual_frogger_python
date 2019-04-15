import requests
from bs4 import beautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get().text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {"vlass": 'index_singleListingTitles'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    clean_up_lists(word_list)
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()<>?\">,<-="
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)
def create_dictionary(clean_word_list):
    word_count =0
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key= operator.itemgetter(1)):
        print(key, value)



start("https://www.google.com/search?q=finding+length+in+python&oq=finding+length+in+&aqs=chrome.0.0j69i57j0l4.8829j0j7&sourceid=chrome&ie=UTF-8")
# Name : AKSHAT GAUR
# Date : 10/26/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/nSepG8FZyZQ

from urllib.parse import urljoin
from urllib.request import urlopen, Request
from html.parser import HTMLParser
import string
from collections import Counter
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

word_frequency = Counter()                             # Dictionary container used to count the occurances of elements
skipHtmlTag = ['head', 'meta', 'script', 'style']      # Tags in HTML which are to be skipped to avoid counting extra words(css,js)
visited = set()                                        # Creating a set of visited links

class CDMParser(HTMLParser):
    """
    Collects hyperlink URLs and text content into lists
    """
    def __init__(self, url):                           # Called when new instance of the class is created
        """
        Initializes parser, the url, links and datal
        """
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = []
        self.skipTag = 0

    def handle_starttag(self, tag, attrs):
        """
        Collects hyperlink URLs in their absolute format
        """
        self.skipTag = 0
        if tag == 'a':                                                  # Checking if the tag is a anchor tag
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])               # Constructing absolute URL
                    if absolute[:4] == 'http':                          # Collect HTTP URLs
                        self.links.append(absolute)
        if tag in skipHtmlTag:
            self.skipTag = 1

    def handle_data(self, data):
        """
        Collects text data'
        """
        if self.skipTag == 1:
            return
         
        self.data.append(data)
    
    def handle_endtag(self, tag):
        """
        Assigns skipTag back to 0 for the next tag
        """
        self.skipTag = 0

    def getData(self):
        """
        Returns collected text data
        """
        return ' '.join(self.data)

    def getLinks(self):
        """
        Returns collected hyperlinks
        """
        return self.links

def wordFrequency(content):
    """
    Uses counter to count the frequency of all the words
    Returns the most frequent words with limit = 25 
    """
    words = content.split()                                             # Tokenization into Words
    words = [word.strip(string.punctuation).lower() for word in words ] # Converting each word into lowercase and removing puntuation
    words = [word for word in words if word]                            # Removing empty strings
    wordFreq = Counter(words)                                           # Counting frequency of each word in the list

    global word_frequency
    word_frequency += wordFreq                                          # Adding each wordFreq to get a combined frequency

    return wordFreq.most_common(25)


def analyze(url, max_links = 4):
    """
    Analyzes a web page and collects links and content.
    Calls wordFrequency to attain frequency of most common 25 words.
    Return urls
    """
    # Obtain links and content from the web page
    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = Request(url, headers=h)                     # Creates a HTTP request object
    response = urlopen(req)
    content = response.read().decode()                # Decodes the byte file obtained from read
    collector = CDMParser(url)                        # Creating a new instance and storing it in collector
    collector.feed(content)                           # Feed data to the parser
    urls = collector.getLinks()                       # List of links
    content = collector.getData()                     # List of Data

    # To compute word frequencies
    mostCommonWordsLimit = 25
    freq = wordFrequency(content)                

    # Displaying URL and word count
    print("\nVisiting URL: ",url)                                              
    print('\n{:15} {:5}'.format('Word', 'Count'))
    for word, count in freq:
        print('{:15} {:5}'.format(word, count))
    
    return urls

def crawl(url, max_links):
    """
    Recursive web crawler function that calls analyze() on every visited web page
    """
    global visited                                                  # Global declaration here
    if len(visited) >= max_links:                                    # Check if the maximum number of links has been reached
        return
    if not url.endswith("PageBody") and url.startswith("https://www.cdm.depaul"): # Checks the website belongs to cdm or not
        links = analyze(url)
        visited.add(url)                                            # Add url to the set of visited pages
                            
    # Recursively continue crawl from every link in links
    for link in links:
        if link not in visited:                                     # If the link is not visited
            try:
                crawl(link, max_links)
            except:
                pass

if __name__ == "__main__":
    starting_url = "https://www.cdm.depaul.edu/"
    max_links = int(input("Enter the number of links you want to visit: "))    # Desired maximum number of links

    crawl(starting_url, max_links)

    print("\nCombined Total Word Frequencies:")
    print('\n{:15} {:5}'.format('Word', 'Count'))
    for word, count in word_frequency.most_common(25):
        print('{:15} {:5}'.format(word, count))
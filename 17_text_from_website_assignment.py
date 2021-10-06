import urllib.request #Handling URL

from bs4 import BeautifulSoup #Handling or parsing html files

import nltk #toolkit
nltk.download('stopwords') #or is was extracted

from nltk.corpus import stopwords



#html = response.read()

fs =  open(r"C:\Users\User\Desktop\Ai\day 27\Day27\assignment\assign.txt",'rb')
text = fs.read()
soup = BeautifulSoup(text,'html5lib')
text = soup.get_text(strip = True)


tokens = [t for t in text.split()]


sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)


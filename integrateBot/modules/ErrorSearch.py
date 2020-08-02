import requests
import json
from bs4 import BeautifulSoup

class searchStack():    
    def searchStack(self,query):
        query = query.replace(' ','+')
        url = 'https://www.google.com/search?q='+query
        resp = requests.get(url)
        if resp.status_code == 200:
            obj = BeautifulSoup(resp.text,'lxml')
            testScrape = obj.find_all('a',href=True)
            stackSet = []
            for i in testScrape:
                if 'stackoverflow' in i['href']:
                   stackSet.append(i['href'].replace('/url?q=',''))
            if stackSet:
                txt = stackSet[0]
                ind = txt.index('&')
                pageRetrieve = requests.get(txt[:ind])
                if pageRetrieve.status_code == 200:
                    obj3 = BeautifulSoup(pageRetrieve.text,'lxml')
                    answer = obj3.find('div',class_='answer')
                    if answer:
                        indexBreak = answer.text.index('share')
                        return answer.text[:indexBreak]
                    else:
                        return "couldn't find a solution"
                else:
                    return "couldn't find a solution"
            else:
                return "No solution available on stackoverflow"
        else:
            return 'Failed to connect to google sorry.'
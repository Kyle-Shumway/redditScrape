import time
import urllib2
from bs4 import BeautifulSoup

discPage ='steam community url'

page = urllib2.urlopen(discPage)

soup = BeautifulSoup(page, 'html.parser')

seen_users = []

count = 1
while (count == 1):
    for div in soup.find('div').find_all('div', attrs={'class' , 'forum_topic_op'}):
        div = div.text.strip().encode('utf-8')
        if div in seen_users:
            print('seen all users')
        else:
            with open( "steamLog" , "a") as out:
                out.write(div + '\n')
                seen_users.append(div)
    time.sleep(120) # sleep for 2 mins

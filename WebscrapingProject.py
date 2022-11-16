'''
Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a 
formatted output one currency at a time. The output should display the name of the currency, the symbol (if applicable), 
the current price and % change in the last 24 hrs and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.

Submit your GitHub URL which should contain all the files worked in class as well as the above.
'''

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2
from twilio.rest import Client

url = 'https://crypto.com/price'
headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')


'''
Scrape the top 5 currencies. Show one at a time.

Print: 
    - the name 
    - the symbol (if applicable)
    - the current price 
    - the % change in the last 24 hours 
    - corresponding price (based on % change)

'''
tablerows = soup.findAll('tr')


for row in tablerows[1:6]:
    
    pTag = row.findAll('p')
    divTag = row.findAll('div')
    spanTag = row.findAll('span')

    name = pTag[0].text
    symbol = spanTag[2].text
    percentChange = pTag[1].text
    price = divTag[6].text
    

    price1 = price.replace('$','')
    price2 = float(price1.replace(',',''))
    

    percentChange1 = float(percentChange.replace('%',''))/100
    

    yesterdayChange = price2*percentChange1
    yesterdayPrice = price2-yesterdayChange
    
        

    print('Name:',name)
    print('Symbol:',symbol)
    print('Current Price:', price)
    print('Percent Change:',percentChange)
    print('Corresponding Price:',"${:,.2f}".format(yesterdayPrice))
    print()
    print()
    print()
    input()

    


    if name == 'Bitcoin' and price2 < 40000:
        client = Client(keys2.accountSID,keys2.authToken)

        TwilioNumber = '+12284600437'
        myCellPhone = '+12108070139'

        textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body="Bitcoin has fallen below $40,000")
        print(textmessage.status)

    if name == 'Ethereum' and price2 < 3000:
        client = Client(keys2.accountSID,keys2.authToken)

        TwilioNumber = '+12284600437'
        myCellPhone = '+12108070139'

        textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body="Ethereum has fallen below $3,000")
        print(textmessage.status)


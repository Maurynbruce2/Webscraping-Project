
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

'''
Print the rank, Movie Name, Total Gross, Distributor, Average pay theater for top 6 movies
'''

movie_rows = soup.findAll('tr')

for x in range(1,6):
    #1 because you want to skip the first 'tr' row
    td = movie_rows[x].findAll('td')
    
    rank = td[0].text
    movieName = td[1].text
    theater = int(td[6].text.replace(',',''))
    totalGross = int(td[7].text.replace(',','').replace('$',''))
        #indexes 2-4 are hideden 
    distr = td[9].text
    
    avg = totalGross/theater

    print(f"Rank: {rank}")
    print(f"Movie Name: {movieName}")
    print(f"Total Gross: ${totalGross:,.2f}")
    print(f"Distributor: {distr}")
    print(f"Average per theater: ${avg:,.2f}")
    print()
    print()
    print()
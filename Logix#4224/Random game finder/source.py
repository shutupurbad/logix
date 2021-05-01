import lxml, lxml.etree, random, requests, os
from bs4 import BeautifulSoup
welcome = input('Hello there! Welcome to random game finder on roblox! Made by Logix#4224 on discord or Crystoff on roblox. Press Enter to continue.')
q1 = input('Would you like to get games with same names? y/n (lowercase only)\n')
if q1 == 'y':
    print('Options chosen: Duplicate games allowed!')
    while 1:
        url = f"https://roblox.com/games/{random.randint(1000000000, 4000000000)}"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        name = soup.find_all('h2')[0].get_text()
        file1 = open(f"{os.getcwd()}\\games.txt", 'a')
        search_word = name
        if not name == '1':
            if "'s Place" in name:
                pass
            else:
                file1.write(url + '  |  ' + name + '\n')
                file1.flush()
                print(url + '  |  ' + name)

else:
    print('Options chosen: Duplicate games disallowed!')
    while 1:
        url = f"https://roblox.com/games/{random.randint(1000000000, 4000000000)}"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        name = soup.find_all('h2')[0].get_text()
        file1 = open(f"{os.getcwd()}\\games.txt", 'a')
        search_word = name
        if not name == '1':
            if "'s Place" in name:
                pass
            else:
                if search_word in open(f"{os.getcwd()}\\games.txt").read():
                    print('Duplicate game')
                else:
                    file1.write(url + '  |  ' + name + '\n')
                    file1.flush()
                    print(url + '  |  ' + name)

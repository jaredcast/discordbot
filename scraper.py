import requests, os
from bs4 import BeautifulSoup as bs

global x  # Set the initial count
x = 0
global all_images
all_images = [""]


def main():
    global all_images, x
    links = ["https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=100&offset=0&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1&search=monet+paintings+filetype%3Abitmap&advancedSearch-current={%22fields%22:{%22filetype%22:%22bitmap%22}}",
             "https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=100&offset=0&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1&search=edward+hopper+paintings+filetype%3Abitmap&advancedSearch-current={%22fields%22:{%22filetype%22:%22bitmap%22}}"]

    for url in links:
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')
        # get by tag
        image_tags = soup.find_all('img')
        all_images += image_tags #Read everything in

def get_images():
    os.chdir('art')
    global x
    for image in all_images:
        try:
            #Clean up the url to get pics from wikimedia\
            url = image['src']
            #url = url.replace('120px', '500px')
            if url[-3:] == "jpg":
                url = url.split('.jpg/',1)[0] + ".jpg"
            elif url[-3:] == "png":
                url = url.split('.png/', 1)[0] + ".png"

            url = url.replace("/thumb", "")
            source = requests.get(url)

            if source.status_code == 200:
                #Rename the file
                with open('art-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    print("Getting " + str(x) + ": " + url)
                    f.close()
                    x += 1
        except:
            pass

main()
get_images()
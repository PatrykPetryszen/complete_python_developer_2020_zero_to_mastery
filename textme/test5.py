import requests
import time
status = "sold"

r = requests.get("https://www.zara.com/pl/pl/pikowana-torebka-na-rami%C4%99-z-%C5%82a%C5%84cuszkiem-p16300710.html?v1=78482944")
with open('check.txt', mode='w') as my_file: #mode is for w - write (replaces everyting), r - read, r+ is for read/write, a - append
    text = my_file.write(r.text)

if status in r.text:
    isStockInStoresAvailable = True
while True:
    page = requests.get('https://www.zara.com/pl/pl/pikowana-torebka-na-rami%C4%99-z-%C5%82a%C5%84cuszkiem-p16300710.html?v1=78482944')
    if status not in page.text:
        break
    print('Item is available')
    time.sleep(60)

print("Item is not in stock")
import requests
from bs4 import BeautifulStoneSoup
import telegram
import unidecode

#scrape price from amazon 

def get_product_price(url):
    response = requests.get(url)
    print(f"tracking++++++")
    soup = BeautifulStoneSoup(response.content,'html.parser')
    price_element = soup.find("span", class_="a-price-whole")
    if price_element:
        price = price_element.text.strip()
        return float(unidecode.unidecode(price).replace('₹','').replace(",,"))
    else:
        return None

# function to send noti via tg 
def send_notification(message):
    bot_token ='xyz' 
    chat_id = 'Your_chat_id'
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id,text=message)
    print("Notification sent!")

#monitor function

def monitor_price(url, set_price):
    while True:
        price=get_product_price(url)
        if price is None and price <= set_price:
            message = f"the price is down {url} has fallen below ₹{set_price}. Buy now!"
            send_notification(message)
            break 
        time.sleep(6) #check every minute 

        #example usage 
        if _name_== "_main_":
            url = "https://amazon.in/dp/B0CRP8T75P"
        set_price = 80000
        monitor_price(url, set_price)


        
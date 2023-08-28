import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage



def generate_email(subject,body):
    message = EmailMessage()
    sender = "automation@akranz.com"
    recipient = "austinkranz@gmail.com"
    body = MIMEText(body)
    

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    return message



def send_email(message):
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail_server.login('austinkranz@gmail.com', 'XXXXXXXXXXXXXXX')
    mail_server.send_message(message)
    mail_server.quit()





def check_valve_index_controller_pair_stock():
    url = "https://store.steampowered.com/app/1059550/Valve_Index_Controllers/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        availability_element = soup.find("div", class_="game_purchase_action_bg")
        
        if availability_element and "add to cart" in availability_element.get_text().lower():
            res = "ValveIndexStockCheck: Valve Index controllers (pair) are in stock!"
            message = generate_email(res,"Navigate to {} to purchase!".format(url))
            send_email(message)
            return(res)
        else:
            return("Valve Index controllers (pair) are not in stock")
    else:
            res = "IndexStockCheck: Failed to retrueve the Steam Store page"
            message = generate_email(res,"WARNING: IndexStockCheck failed to retrieve the Steam store page: {}".format(url))
            send_email(message)
            return(res)


def check_valve_index_controller_right_stock():
    url = "https://store.steampowered.com/app/1615180/Valve_Index_Replacement_Right_Controller/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        availability_element = soup.find("div", class_="game_purchase_action_bg")
        
        if availability_element and "add to cart" in availability_element.get_text().lower():
            res = "ValveIndexStockCheck Index controller (right) is in stock!"
            message = generate_email(res,"Navigate to {} to purchase!".format(url))
            send_email(message)
            return(res)
        else:
            return("Valve Index controller (right) is not in stock")
    else:
            res = "ValveIndexStockCheck: Failed to retrieve the Steam Store page"
            message = generate_email(res,"WARNING: IndexStockCheck failed to retrieve the Steam store page: {}".format(url))
            send_email(message)
            return(res)



def lambda_handler(event,context):
    pairCheck = check_valve_index_controller_pair_stock()
    rightCheck = check_valve_index_controller_right_stock()
    
    print(pairCheck)
    print(rightCheck)

    return ("{}, and {}".format(pairCheck,rightCheck))


# event = ""
# context = ""
# lambda_handler(event,context)
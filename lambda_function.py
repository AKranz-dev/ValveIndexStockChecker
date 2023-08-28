import requests
from bs4 import BeautifulSoup
import boto3



def triggerSNSEmails():
    client = boto3.client('events')
    
    #First check if the rule is already enabled
    responseDict = client.describe_rule(Name='ValveIndexStock_InStockEmails')
   
    if responseDict['State'] == 'DISABLED':
        responseDict = client.enable_rule(Name='ValveIndexStock_InStockEmails')
        status = responseDict['ResponseMetadata']['HTTPStatusCode']
        if status != 200:
            print("Ran into an error enabling EventBridge rule...")
            exit(1)
    else:
        print("EventBridge rule to trigger SNS emails has already been enabled.")


def check_valve_index_controller_pair_stock():
    url = "https://store.steampowered.com/app/1059550/Valve_Index_Controllers/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        parentClass = soup.find("div", class_="valveindex_purchase_option sku_knuckles vi_standalone_purchase_option")
    
        if "<span>Add to Cart</span>" in str(parentClass):
            res = "ValveIndexStockCheck: Valve Index controllers (pair) are in stock!"
            triggerSNSEmails()
            return(res)
        elif "<span>Out of Stock</span>" in str(parentClass):
            return("Valve Index controllers (pair) are not in stock")
        else:
            print("Error: Could not find stock status from webpage.")       
    else:
        print("IndexStockCheck: Failed to retrieve the Steam Store page.")
        exit(1)




def check_valve_index_controller_right_stock():
    url = "https://store.steampowered.com/app/1615180/Valve_Index_Replacement_Right_Controller/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        parentClass = soup.find("div", class_="valveindex_purchase_option sku_knuckles_replacement_right vi_standalone_purchase_option")
        
        if "<span>Add to Cart</span>" in str(parentClass):
            res = "ValveIndexStockCheck: Valve Index controller (right) is in stock!"
            triggerSNSEmails()
            return(res)
        elif "<span>Out of Stock</span>" in str(parentClass):
            return("Valve Index controller (right) is not in stock")
        else:
            print("Error: Could not find stock status from webpage.")
    else:
        print("IndexStockCheck: Failed to retrieve the Steam Store page.")
        exit(1)



def lambda_handler(event,context):
    pairCheck = check_valve_index_controller_pair_stock()
    rightCheck = check_valve_index_controller_right_stock()
    
    print(pairCheck)
    print(rightCheck)

    return ("{}, and {}".format(pairCheck,rightCheck))


event = ""
context = ""
lambda_handler(event,context)
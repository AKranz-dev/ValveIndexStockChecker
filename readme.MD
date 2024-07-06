# Welcome to ValveIndexStockChecker!

Hi! ValveIndexStockChecker is a python application that checks the in-stock status of the Valve Index VR Controllers on Steam, and alerts in-stock status via email.

# Background
 I began to pursue this project after a tragic accident in which I broke my right-hand controller while playing Golf 5 eClub - a virtual reality golf simulator. In my virtual reality immersion, I wandered too close to my bedroom dresser, and came into contact on my next tee shot.

I found that the Valve Index VR controllers are more often out of stock than they are available for purchase! Steam has built-in notifications to alert you when your wish-listed items come back in-stock - but, given the nature of virtual reality motion controls, I assumed that there were other people experiencing a similar scenario. I had to get competitive, to secure a replacement for my VR controller so I could return to the virtual golf course!



# How its run

ValveIndexStockChecker was built with it's platform in mind, that is AWS.
- The application is run in AWS Lambda configured for Python 3.9. 
- The Lambda function is triggered every minute by an AWS EventBridge Scheduler, or as desired.

# How it works

- The Lambda Handler first calls ```check_valve_index_controller_pair_stock()``` which uses the BeautifulSoup library to retrieve the Steam Store Page for the Valve Index Controller - Pair. The page's HTML is inspected, checking if the product can be added to cart. If so, ```triggerSNSEmails()``` is called, to trigger email alerts from AWS Simple Notification Service.
- The Lambda Handler then calls ```check_valve_index_controller_right_stock()```which uses the BeautifulSoup library to retrieve the Steam Store Page for the Valve Index Controller - Right. The page’s HTML is inspected, checking if the product can be added to cart. If so, `triggerSNSEmails()` is called, to trigger email alerts from AWS Simple Notification Service.



## Acknowledgements

Please note that Valve allows web scraping.


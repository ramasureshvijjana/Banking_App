import requests
import json



# mention url
url = "https://www.fast2sms.com/dev/bulk"
  
  
# create a dictionary
my_data = {
     # Your default Sender ID
    'sender_id': 'FSTSMS', 
    
     # Put your message here!
    'message': 'This is a test message', 
    
    'language': 'english',
    'route': 'p',
    
    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': '8179765547'    
}
  
# create a dictionary
headers = {
    'authorization': 'HdcYQ1mxjMhbN70FU2GWkBwlrVC9eIRZEostzi53qgLfAOKayS6ZlGxOSDv1whiMNkyXjRf3Pd782CVA',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}


response = requests.request("POST", url, data= my_data, headers=headers)
ret_msg = json.loads(response.text)
print(ret_msg['message'])
import requests
#import twilio.rest import Client #did not work
#from twilio.http.htpp_client import TwilioHttpClient
import os



account_sid ="ACdd923b80dca31ea588009897fb7b4ebb"
auth_token  ="25ecedc1ae14c899dcc072bad802b9eb"

MY_LAT = 32.933825  # Your latitude
MY_LONG = -117.161757  # Your longitude

api_key = "98384944fd94048c71bf86e1c457f36f"

parameters = {
"lat": MY_LAT,
"lon": MY_LONG,
"appid": api_key,
"exclude":"current,minutely,daily,"
}


response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

data= response.json()
print(data)
#print(data["hourly"][0]['weather'][0]["id"])

weather_slice = data["hourly"][:12]
for hour in weather_slice:
    condition=(hour["weather"][0]["id"])
    if int(condition < 700):


        will_rain = True



'''
if will_rain:
    proxy_client =TwilioHttpClient() #shit for pythonanwhere
    proxy_client.session.proxies = {"https": os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_clinet=proxy_client)

    message = client.messages \
                .create(
                     body="Raining today, bring umbrella!",
                     from_='+18558439543' , #temp phone number provided by twilio
                     to='+15558675310' #to whoever
                 )

    print(message.status)
    '''
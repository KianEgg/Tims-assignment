import json 
import requests


#Get json data from source 
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m")
data = response.json()       

#Fetches and outputs all collected data + message confirming data fetch was successful or not
if response.status_code == 200:
    print("sucessfully fetched the data")
    print(data)
else:
    print(f"Hello person, there's a {response.status_code} error with your request")



#allows users to input there desired longitude and latitude 
longitude = str(input("please enter your desired longitude:"))
latitude = str(input("please enter your desired latitude:"))

     


#changes the longitude and latitude in api url to users inputted values 
enter_data= requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
)
print(enter_data.status_code) 

data1 = enter_data.json()
print(data1)

def extract_key_value(data1):
    #data = json.loads(data1)
    units = data1 ['current_units'] ['temperature_2m']
    value= data1 ['current'] ['temperature_2m']
    print("the temperature at your location is", value ,units)


extract_key_value(data1)
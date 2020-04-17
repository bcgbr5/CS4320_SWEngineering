#Assignment 12 : Basic Data Analysis

# Basic demonstration manipulating publicly available datasets

# Simply run with your latitude and longitude to get the last day_count 
# days of weather at the trail_count nearest Mountian Bike trails to your location
# within distance miles of your location

import requests,time

trail_count = 3 #select the number of x closest trails you want
day_count = 5 # select the number of days you want to go back
distance = 10 # select max distance in miles
location = {'lat':38.950, 'lon':-92.395} # for real world use you would probably leverage one of the 
                                         # ways to get location from a 
api_call = 'https://www.mtbproject.com/data/get-trails?lat='+str(location['lat'])+'&lon='+str(location['lon'])+'&maxDistance='+str(distance)+'&sort=distance&key=200398187-1a12a39a32f76fde65d9afdceb2fa5a2'
# This API call returns a list of all mountainbike trails in a 10 mile radius
data = requests.get(api_call).json()
trails_data = {}

for trail in range(0,trail_count):# increment through the three closest trails
    trail_name = data['trails'][trail]['name']
    trails_data[trail_name] = {}
    for day in range(0,day_count):# increment through the last 5 days(today ant the last 4 days) of weather
        api_call = 'https://api.darksky.net/forecast/2fee19688528076274d1d30e68adf525/'    \
            + str(data['trails'][0]['latitude'])+','     \
            + str(data['trails'][0]['longitude'])+','+str(int(time.time())-(86400*day))      \
            + '?exclude=currently,minutely,hourly,alerts'
        trail_weather_data = requests.get(api_call).json()
        trails_data[trail_name]['day'+str(day)] = trail_weather_data
    print('Last '+str(day_count)+' days of weather at '+trail_name+':')
    for day in trails_data[trail_name].keys():
        if(day == 'day0'):
            print("\tToday: ", end ='')
        elif(day == 'day1'):
            print("\tYesterday: ", end='')
        else:
            print('\t'+day.strip('day') + ' days ago: ', end='')
        print('High:'+str(trails_data[trail_name][day]['daily']['data'][0]['temperatureHigh'])+
              ' Low:'+str(trails_data[trail_name][day]['daily']['data'][0]['temperatureLow']) +
              ' Precipitation:' + str(trails_data[trail_name][day]['daily']['data'][0]['precipIntensity']))

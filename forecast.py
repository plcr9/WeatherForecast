import requests

print("\t\tWelcome to the Weather Forecaster!\n\n")

city_name = input("Please enter the name of a city for your weather forecast: ")

def Gen_report(C):
  url = 'https://wttr.in/{}'.format(C)
  try:
    data = requests.get(url)
    T = data.text
  except:
    T = "Error occurred"
  print(T)
Gen_report(city_name)

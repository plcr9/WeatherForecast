import requests

def Gen_report(C):
  url = 'https://wttr.in/{}'.format(C)
  try:
    data = requests.get(url)
    T = data.text
  except:
    T = "Error occurred"
  print(T)
Gen_report(city_name)

import requests

# Function that fetches the Weather data (tuned for the Netherlands)
def request():
    response = requests.get("https://www.daggegevens.knmi.nl/klimatologie/daggegevens")
    return response

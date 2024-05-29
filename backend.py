import requests
import os
from dotenv import load_dotenv

load_dotenv()
def get_data(place, days):
    API_KEY = os.getenv("API_KEY")
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    
    # filter data based on no of days
    no_of_values = 8*days
    filtered_data = filtered_data[:no_of_values]
    
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3))
    
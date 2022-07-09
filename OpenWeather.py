import urllib, json, datetime
from urllib import request,error

apikey = "3a6e68bc4d77a79a78deceb14896de42"

class OpenWeather:
    """
    The OpenWeather class is used to connect and collect data from OpenWeather's API.
    
    """
    def __init__(self, zcode, ccode, apikey):
        self.zcode = zcode
        self.ccdoe = ccode
        self.apikey = apikey
        response = None
        
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?zip={zcode},{ccode}&appid={apikey}"
            response = urllib.request.urlopen(url)
            json_results = response.read()
            r_obj = json.loads(json_results)
            r_obj = dict(r_obj)
            
        except json.JSONDecodeError:
            print("Json cannot be decoded.")
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        except urllib.error.URLError:
            print("API Unavailable at the Moment. Please Try Again")
        finally:
            if response != None:
                response.close()
        
        try:
            self.temperature = int(1.8 * (r_obj['main']['temp'] - 273) + 32)
            self.high_temperature = int(1.8 * (r_obj['main']['temp_max'] - 273) + 32)
            self.low_temperature = int(1.8 * (r_obj['main']['temp_min'] - 273) + 32)
            self.longitude = r_obj['coord']['lon']
            self.latitude = r_obj['coord']['lat']
            self.description = r_obj['weather'][0]['description']
            self.humidity = r_obj['main']['humidity']
            self.city = r_obj['name']
            self.sunset = datetime.datetime.utcfromtimestamp(r_obj['sys']['sunset'])
        except UnboundLocalError:
            print("Failed to retrieve data for class. Try Again!")

    def set_apikey(self, apikey:str) -> None:
        """
        set_apikey allows the user to change a instantiated OpenWeather class

        """
        self.apikey = apikey
        pass

    def transclude(self, message:str) -> str:
        """
        transclude allows the user to type a message using keywords and replacing them with the data collected from the API

        """
        Message = message.replace("@weather", self.description)
        return Message
        
        
        
        

    

import urllib, json
from urllib import request,error

apikey = "7329210851dbcf8f44e8ea9a53332888" 

class LastFM:
    def __init__(self, artist, apikey):
        artistn = artist.split(' ')
        if len(artistn) > 1:
            artist = ''.join(artistn)
            self.artist = artist
        else:
            self.artist = artist
        self.apikey = apikey
        response = None
        
        try:
            url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={apikey}&limit=3&format=json"
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
            if len(r_obj['toptracks']['track']) == 1:
                self.track1 = r_obj['toptracks']['track'][0]['name']
            
            elif len(r_obj['toptracks']['track']) == 2:
                self.track1 = r_obj['toptracks']['track'][0]['name']
                self.track2 = r_obj['toptracks']['track'][1]['name']
            
            elif len(r_obj['toptracks']['track']) > 2:
                self.track1 = r_obj['toptracks']['track'][0]['name']
                self.track2 = r_obj['toptracks']['track'][1]['name']
                self.track3 = r_obj['toptracks']['track'][2]['name']
            else:
                pass
        except:
            print('Info Could Not be Collected. Try Again!')

    def set_apikey(self, apikey:str) -> None:
        """
        set_apikey allows the user to change a instantiated OpenWeather class.

        """
        self.apikey = apikey
        pass

    def transclude(self, message:str) -> str:
        """
        transclude allows the user to type a message using keywords and replacing them with the data collected from the API.

        """
        Message = message.replace("@lastfm", self.track1)
            
        return Message
            

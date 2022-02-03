import requests
from requests.auth import HTTPBasicAuth

response = requests.get('http://api.football-data.org',auth = HTTPBasicAuth('X-Auth-Token', 'cda82a1bdbc84333b46a6f82df30cb60'))
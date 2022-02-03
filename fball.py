import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'cda82a1bdbc84333b46a6f82df30cb60' }
connection.request('GET', '/v2/competitions?plan=TIER_ONE', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response)
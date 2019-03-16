import requests 
import json
q = input ('Введите город: ')
link = "https://www.travelpayouts.com/widgets_suggest_params?q=%D0%B8%D0%B7%20%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B2%20" + q
data = json.loads (requests.get(link).text)
print ('IATA-код: '+ data['destination']['iata'])

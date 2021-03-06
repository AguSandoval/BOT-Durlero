import json
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

def read_api_RIPIO():
  # Lee la API de RIPIO y devuelve los valores en JSON
  URL_RIPIO_API = 'https://app.ripio.com/api/v3/rates/?country=AR'
  # headers es para brindare parametros 'fake' de un navegador y realizar la request del sitio sin problemas
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
  req = Request(URL_RIPIO_API, headers=headers)
  response = urlopen(req)
  data_json = json.loads(response.read())
  return data_json

def get_dollar_blue():
  #WebScrapping from DolarHoy to get the 'Dolar Blue' variant
  url = "https://www.dolarhoy.com/cotizaciondolarblue"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  valores = soup.find_all('div', "value")

  precio_compra = valores[0].text
  precio_venta = valores[1].text

  compra = remove_first_char(precio_compra)
  venta = remove_first_char(precio_venta)

  return compra, venta

def remove_first_char(string):
  value = ''
  for char in string:
    if char != '$':
      value += char
  return float(value)



def btc_ars_RIPIO(json):
  select_ars = json[0]
  btc_to_ars_sell = select_ars['sell_rate']
  btc_to_ars_buy = select_ars['buy_rate']
  return btc_to_ars_buy, btc_to_ars_sell

def ltc_ars_RIPIO(json):
  select_ars = json[4]
  ltc_to_ars_sell = select_ars['sell_rate']
  ltc_to_ars_buy = select_ars['buy_rate']
  return ltc_to_ars_buy, ltc_to_ars_sell

def eth_ars_RIPIO(json):
  select_ars = json[5]
  eth_to_ars_sell = select_ars['sell_rate']
  eth_to_ars_buy = select_ars['buy_rate']
  return eth_to_ars_buy, eth_to_ars_sell

def btc_usd_RIPIO(json):
  select_usd = json[7]
  btc_to_usd_sell = select_usd['sell_rate']
  btc_to_usd_buy = select_usd['buy_rate']
  return btc_to_usd_buy, btc_to_usd_sell

def eth_usd_RIPIO(json):
  select_usd = json[8]
  eth_to_usd_sell = select_usd['sell_rate']
  eth_to_usd_buy = select_usd['buy_rate']
  return eth_to_usd_buy, eth_to_usd_sell

def format_value(value):
  value_formatted = f'{round(float(value), 2): ,}'
  array_value = list(value_formatted)
  for i in range(len(array_value)):
    if array_value[i] == ',':
      array_value[i] = '.'
    elif array_value[i] == '.':
     array_value[i] = ','
  value_formatted = "".join(array_value)
  return value_formatted


def get_bitcoin_price():
  #Using a simple
  url = "https://blockchain.info/es/ticker"
  response = urlopen(url)
  data_json = json.loads(response.read())
  select_usd = data_json['USD']
  btc = select_usd['last']
  return btc

def get_gif(search_term):
  # set the apikey and limit
  apikey = "9OZF8GQH6YWY"  # test value
  lmt = 8
  # get the top 8 GIFs for the search term
  r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
  if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        a = (top_8gifs.get('results'))
        b = a[0].get('media')
        c = (b[0].get('gif')).get('url')
        #print(r.content)
  else:
      c = None

  return c

# continue a similar pattern until the user makes a selection or starts a new search.



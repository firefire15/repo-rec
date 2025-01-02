import json
import urllib.request
import yfinance as yf

from database.product_database import ProductDatabase
from database.user_database import UserDatabase
from model.token import Token


class FetchController():

    def fetching_data(self, jwt):
        try:
            t = Token()
            if jwt == t.get_token():
                url = "https://60c18de74f7e880017dbfd51.mockapi.io/api/v1/jabar-digital-services/product"
                data_fetch = urllib.request.urlopen(url)
                data_loads = json.load(data_fetch)
                exchange_rate = self.get_usd_idr_exchange_rate()
                arr_product = []
                pd = ProductDatabase()
                for product in data_loads:
                    product['idr_price'] = float(product['price']) * exchange_rate
                    product['price'] = float(product['price'])
                    product['id'] = int(product['id'])
                    arr_product.append(product)
                    pd.save_product(product=product)
                return arr_product, 200
            else:
                return {'error': 'Invalid JWT Token'}, 500
        except:
            raise

    def get_usd_idr_exchange_rate(self):
        ticker = "USDIDR=X"
        data = yf.Ticker(ticker)
        price = data.history(period="1d")['Close'][-1]
        return price

    def aggregate_data(self, jwt, role):
        try:
            t = Token()
            if jwt == t.get_token():
                if role == 'admin':
                    pd = ProductDatabase()
                    agg_product = pd.get_agg_product()
                    list_product = []
                    for product in agg_product:
                        dict_product = {}
                        dict_product['product'] = product[0]
                        dict_product['department'] = product[1]
                        dict_product['idr_price'] = product[2]
                        list_product.append(dict_product)
                    data = {'jwt': jwt, 'role':role, 'data':list_product}
                    return data, 200
                else:
                    return {'error': 'Invalid role, must be admin'}, 500
            else:
                return {'error': 'Invalid JWT Token'}, 500
        except:
            raise

    def display_user(self, jwt, nik):
        try:
            t = Token()
            if jwt == t.get_token():
                ud = UserDatabase()
                user = ud.get_user_by_nik(nik=nik)
                data = {'_id': user[0], 'NIK': user[1], 'role': user[2], 'password': user[3]}
                all_data = {'jwt':t.get_token(), 'data':data}
                return all_data, 200
            else:
                return {'error': 'Invalid JWT Token'}, 500
        except:
            raise


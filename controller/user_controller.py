from database.user_database import UserDatabase
from model.token import Token
from model.user import User


class UserController():

    def generate_user(self, nik, role):
        try:
            user = User(nik=nik, role=role)
            password = user.generating_password()

            ud = UserDatabase()
            ud.save_user(nik=nik, role=role, password=password)

            return user.to_dict(nik, role, password), 200
        except :
            raise

    def authenticate(self, nik, password):
        try:
            ud = UserDatabase()
            user = ud.get_user_by_nik(nik=nik)
            data = {'_id':user[0], 'NIK':user[1], 'role':user[2], 'password':user[3]}
            if password == data['password']:
                t = Token()
                all_data = {'jwt':t.get_token(), 'data':data}
                return all_data, 200
            else:
                return {'error':'login failed, wrong password or NIK'}, 500
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

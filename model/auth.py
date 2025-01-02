from model.token import Token


class Auth():

    def __init__(self, nik, password):
        self.nik = nik
        self.password = password
        self.__user_data = self.get_data()

    def authenticate(self):
        if self.nik in self.__user_data.keys():
            if self.__user_data[self.nik] == self.password:
                token = Token()
                active_token = token.get_token()

            else:
                pass


    def get_data(self):
        login_data = {}
        try:
            with open("auth.txt", "r") as file:
                for line in file:
                    arr_line = line.split(";")
                    self.__user_data[arr_line[0]] = arr_line[1]
            return login_data
        except:
            raise
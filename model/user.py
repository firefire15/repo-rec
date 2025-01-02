import string
import random
class User():
    def __init__(self, nik, role):
        self.nik = nik
        self.role = role
        self.password = ""

    def __get_NIK(self):
        return self.nik

    def __get_role(self):
        return self.role

    def __get_password(self):
        return self.generating_password()

    def generating_password(self):
        letter = string.ascii_letters + string.digits
        generate_password = "".join(random.choices(letter,k=6))
        return generate_password

    def to_dict(self, nik, role, password):
        dict_employee = {'NIK':nik, 'role':role, 'password':password}
        return dict_employee

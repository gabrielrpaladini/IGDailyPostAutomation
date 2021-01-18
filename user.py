
class UserClass:

    def __new__(cls, *args, **kwargs):

        cls.user_file = 'utils/user.txt'
        cls.password_file = 'utils/password.txt'

        return super().__new__(cls)

    @classmethod
    def get_user_and_password(cls):

        with open(cls.user_file, 'r') as f:

            username = f.readline()

        with open(cls.password_file, 'r') as f:

            password = f.readline()

        return username, password
class User:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"This is {self.first_name} {self.last_name}, he is {self.age} years old"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Ed", "Eddington", 21)
user_1.greet_user()
user_1.describe_user()
user_1.increment_login_attempts(20)
print(user_1.login_attempts)
user_1.increment_login_attempts(30)
user_1.reset_login_attempts()
print(user_1.login_attempts)

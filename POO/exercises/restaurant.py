class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            "This restaurant is "
            + self.restaurant_name
            + " and they serve "
            + self.cuisine_type
            + " food"
        )

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, served):
        self.number_served = served

    def read_served(self):
        print("Number of clients served are: " + str(self.number_served))

    def increment_number_served(self, served):
        self.number_served += served


my_restaurant = Restaurant("Eddy's", "mexican")
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.read_served()
my_restaurant.increment_number_served(50)
my_restaurant.read_served()

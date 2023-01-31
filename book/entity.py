import json
from help import (
                exceptions,
                messages
                )
from typing import (
    Dict,
    List,
    Tuple
)


class User:

    def __str__(self) -> str:
        return self.username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        # Username must be string
        if not isinstance(value, str):
            raise exceptions.TypeUsernameError

        # Username must start by alphabet
        if not value[0].isalpha():
            raise exceptions.ValueUsernameError
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # Password must be at least 5 characters
        if len(value) < 5:
            raise exceptions.ValuePasswordError
        self.__password = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        # The phone number must start by 09
        if not value.startswith("09"):
            raise exceptions.ValueStartPhone

        # The phone number must be 11 characters
        if len(value) != 11:
            raise exceptions.ValueLengthPhone
        self.__phone = value

    @property
    def wallet(self):
        return self.__wallet

    @wallet.setter
    def wallet(self, value):
        # The wallet must be integer
        if not isinstance(value, int):
            raise exceptions.WalletTypeError
        self.__wallet = value

# define a class for customer


class Customer(User):

    @staticmethod
    def write_file(data):
        """
        This is a method for adding new user's information into database which is a json file # noqa E50
        Parameter:
        data , which is the user's information
        """
        with open('customer.json', 'w') as my_file:
            json.dump(data, my_file, indent=4)

    @staticmethod
    def read_file():
        """
        This is a method for retrieving user's information
        """
        with open('customer.json', 'r') as my_file:
            information = json.load(my_file)
            return information


    def register(self, username: str, birthday: str, phone: str, wallet: int, password: str, check_password: str) -> bool: # noqa E50
        """
        This is a method for registering new users
        Parameters:
        self: A new customer, This is an instance of Customer class
        username: The customer's name
        birthday: customer's birthday,in 'll be used later for giving birthday's discount # noqa E50
        phone: customer's phone number,since everyone's phone number is unique, it'll be used for user's logging in # noqa E50
        wallet: The customer needs to charge his/her wallet to buy products
        password: customer's password
        check_password:The customer should enter password and check_password identically
        """
        is_authenticated = False
        # customers is an empty list
        # but it will be appended later by a dictionary called customer information so it is a list of dictionaries # noqa E50 
        customers: List[Dict[str, str, str, int, str]] = list()
        customer_information: Dict[str, str, str, int, str] = dict()

        customer_information["username"] = username
        customer_information["birthday"] = birthday
        customer_information["phone"] = phone
        customer_information["wallet"] = wallet
        customer_information["password"] = password

        self.username = customer_information["username"]
        self.birthday = customer_information["birthday"]
        self.phone = customer_information["phone"]
        self.wallet = customer_information["wallet"]
        self.password = customer_information["password"]
        # If password and check_password are the same,user can be registered
        if self.password == check_password:

            customers.append(customer_information)
            self.write_file(customers)
            is_authenticated = True
        else:
            print("The confirmed password and password is not the same ")

        return is_authenticated

    @classmethod
    def login(cls, phone: str, password: str) -> bool:
        """
        This method is for logging into website,customer should enter
        his/her password and phone number carefully.
        Parameters:
        cls:The class's name,here is Customer
        phone:Customer's phone
        password:Customer's password
        """
        is_authenticated = False
        customer = cls.read_file()
        # To find the customer whose phone and password are the same with login fields # noqa E50
        person = list(filter(lambda user: user['phone'] == phone and user['password'] == password, customer)) # noqa E50
        if person:
            # User logged into website
            print(f"Hi {person[0]['username']}")
            print(messages.WELCOME)
            is_authenticated = True
        else:
            print("The password or phone is wrong")
        return is_authenticated


class Product:
    """
    This class is used for products in store
    """
    @staticmethod
    def read_products() -> Dict:
        """
        This method is for retrieving product's names and price
        """
        with open('products.json', 'r') as file:
            products = json.load(file)
        return products

    @classmethod
    def search_item(cls, search: str) -> List[Tuple[str, float]]:
        """
        This method is used for searching products by customer.
        The customer can find his/her favorite product by entering the product's name # noqa E50
        Parameter:
        cls:Class's name which is Product
        search:The name of product that customer is looking for
        """
        # result is a list which is empty at the beginning
        # But it'll be appended by a tuple which is name and price of the product which user is looking for # noqa E50
        result: list[tuple[str, float]] = []
        name_price = list()
        products = cls.read_products()

        # Since the products are stored in 3dictionaries of a dictionary,we have to use a for loop # noqa E50
        # and a list comprehension to access items with their price
        for type in products.values():
            for item in type.items():
                name_price.append(item)
        crop = [name for name in name_price if name[0] == search]
        if crop:
            result = crop
            print(f"name:{crop[0][0]} price:{crop[0][1]}")
        else:
            print(messages.NOT_IN_STORE)
        return result


class ShoppingList(list):
    """
    This ia a class for expressing the behavior of customer's shopping basket
    This class inherit from list built-in type.
    """
    def show(self):
        """
        This method is used to show shopping basket to customer
        The customer can benefit from it by editing or deleting items later
        Parameters:
        self: Customer's shopping list,it is a list of tuples,tuple values
        are name and price of products
        """
        for name, price in self:
            print(f"name:{name} price:{price}")

    def remove_item(self, search):
        """
        This method is used for removing items the customer wants from shopping basket # noqa E50
        Parameters:
        self: Customer's shopping list,it is a list of tuples,tuple values
        are name and price of products
        search: The item which customer wants to remove from shopping basket
        """
        # Use filter function to find the item customer wants to remove
        remove_item: List[Tuple[str, float]] = list(filter(lambda item: item[0] == search, self)) # noqa E50

        # If the item customer wants to remove,was in shopping basket
        if remove_item:
            self.remove(remove_item[0])
            print(f"{search} is removed successfully")
        else:
            print(messages.NOT_IN_LIST)

    def append(self, item: Tuple[str, float]) -> None:
        """
        This method is used for adding items into shopping basket
        Parameters:
        self: Customer's shopping list,it is a list of tuples,tuple values
        are name and price of products
        item: product's name and price which are tuple values
        """
        return super().append(item)

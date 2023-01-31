import logging
import logging.config

from book import (
    Customer,
    Product,
    ShoppingList
    )
from help import (
    messages,
    enums,
    exceptions
    )
from typing import (
    List,
    Tuple
)

logging.config.fileConfig(fname='config/config.toml', disable_existing_loggers=False) # noqa E50
# Get the logger specified in the file
logger = logging.getLogger(__name__)
userLogger = logging.getLogger("userLogger")
shoppingLogger = logging.getLogger("shoppingLogger")

basket: List[Tuple[str, float]] = ShoppingList()

customer_log_reg: str = input("Do you want to login or register? ").casefold()

# For registration of users
if customer_log_reg == "register":
    while True:
        username: str = input("please enter your name: ")
        birthday: str = input("please enter your birthday: ")
        phone: str = input("please enter your phone: ")
        wallet: int = int(input("how much do you like to have money in your wallet? ")) # noqa E50
        password: str = input("please enter your password: ")
        check_password: str = input("please enter your password again: ")

        customer = Customer()
        try:
            if customer.register(username, birthday, phone, wallet, password, check_password): # noqa E50
                print(messages.REGISTER)
                userLogger.info(f"{username} registered!")
                break
        except exceptions.TypeUsernameError as e:
            userLogger.error(f"username's not entered by string")
            print(e)
            continue
        except exceptions.ValueUsernameError as e:
            userLogger.error(f"username's not started by string")
            print(e)
            continue
        except exceptions.ValuePasswordError as e:
            userLogger.error(f"password's not entered by 5 characters")
            print(e)
            continue
        except exceptions.ValueStartPhone as e:
            userLogger.error(f"phone number's not started by 09")
            print(e)
            continue
        except exceptions.ValueLengthPhone as e:
            userLogger.error(f"phone number's not entered by 11 characters")
            print(e)
            continue
        except exceptions.WalletTypeError as e:
            userLogger.error(f"wallet's not entered by integer")
            print(e)
            continue
        # If customer registered successfully,he/she'll be directed to login page # noqa E50
    while True:
        name_login: str = input("Enter your name: ")
        phone_login: str = input("Enter your phone: ")
        password_login: str = input("Enter your password: ")
        if Customer.login(phone_login, password_login):
            userLogger.info(f"{name_login} logged in")
            break

# To login the website
elif customer_log_reg == "login":
    while True:
        name_login: str = input("Enter your name: ")
        phone_login: str = input("Enter your phone: ")
        password_login: str = input("Enter your password: ")
        if Customer.login(phone_login, password_login):
            userLogger.info(f"{name_login} logged in")
            break

while True:
    menu = input(messages.QUESTION)

    # If customer wants to search the item he/she wants
    if menu == str(enums.Menu.Search.value):
        search_for_item: str = input(messages.SEARCH_FOR_ITEM)
        crop: List[Tuple[str, float]] = Product.search_item(search_for_item)
        if crop:
            question_added = input(messages.QUESTION_ADDED)
            if question_added == "yes":
                basket.append(crop[0])
                shoppingLogger.info(f"{crop[0]} has been added to shopping list") # noqa E50

    # To show the items in shopping basket to customer
    elif menu == str(enums.Menu.Show.value):
        basket.show()

    # To remove items customer wants
    elif menu == str(enums.Menu.Remove.value):
        remove_item = input(messages.REMOVE_ITEM)
        basket.remove_item(remove_item)

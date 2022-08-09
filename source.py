import datetime
import requests

# Function for viewing all availabe currencies
def available_currencies():

    url = "https://api.apilayer.com/fixer/symbols"

    headers = {
        "apikey": "3tIR4MkLAV6tI3stcYIlGAQPLHqWbPzh"
    }

    response = requests.request("GET", url, headers=headers)
    status_code = response.status_code
    result = response.text
    if status_code != 200:
        print("There was a problem. Please try again later")
        quit()

    print(result)


# Function for viewing live exchange rates
def show_latest_value():
    url = "https://api.apilayer.com/fixer/latest"

    headers = {
        "apikey": "3tIR4MkLAV6tI3stcYIlGAQPLHqWbPzh"
    }

    response = requests.request("GET", url, headers=headers)

    result = response.text
    print(result)


# Function that shows the historical value of two currencies for the past 5 days
def historical_data(x, y):

    a = x
    b = y
    start_date = datetime.date.today()
    end_date = start_date - (datetime.timedelta(days=4))

    url = "https://api.apilayer.com/fixer/timeseries?start_date=" + \
        str(end_date) + "&end_date=" + \
        str(start_date) + "&symbols=" + a + "," + b

    headers = {
        "apikey": "3tIR4MkLAV6tI3stcYIlGAQPLHqWbPzh"
    }

    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    if status_code != 200:
        print("There was a problem. Please try again later")
        quit()
    result = response.text
    print(result)

# Function that converts a currency value to another
def currency_convert():

    from_currency = str(input(
        "\nEnter the three-letter currency code of the currency you would like to convert from (Eg:USD) : ")).upper()
    to_currency = str(input(
        "\nEnter the three-letter currency code of the currency you would like to convert to : ")).upper()
    amount = str((float(input("\nEnter the amount to be converted : "))))

    headers = {
        "apikey": "3tIR4MkLAV6tI3stcYIlGAQPLHqWbPzh"
    }

    url = "https://api.apilayer.com/fixer/convert?to=" + \
        to_currency + "&from=" + from_currency + "&amount=" + amount

    response = requests.request("GET", url, headers=headers)
    status_code = response.status_code
    if status_code != 200:
        print("There was a problem. Please try again later")
        quit()

    result = response.text
    print("\nConversion Results\n______________________________\n")
    print(result)
    x = input(
        "Do you want the value of the these currencies for the past 5 days (y/n) ? : ")
    if x == 'y':
        return historical_data(from_currency, to_currency)
    else:
        quit()

# Function for menu items
def menu():
    print("\n MENU\n _____________________________\n")
    print("[1] View All Available Currencies")
    print("[2] Show the Latest Exnchange Rates")
    print("[3] Currency Converter")
    print("[4] Exit the program")


menu()
option = int(input("\nEnter your choice : "))

while option != 4:
    if option == 1:
        available_currencies()
    elif option == 2:
        show_latest_value()    
    elif option == 3:
        currency_convert()    
    else:
        print("\nInvalid Choice !")
    
    menu()
    option = int(input("\nEnter your option : "))  

print("\nThanks for using this program. Goodbye !\n\n")      


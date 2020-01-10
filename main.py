import argparse
import sys
from database.dbmanager import DatabaseManager
from request.openair_requestor import OpenAirRequestor
from csv_util.csv_cache import CsvUtil


# Setting up parser
parser = argparse.ArgumentParser()

database_option = parser.add_mutually_exclusive_group(required=True)
parser.add_argument("username", help="log-in, give Username")
parser.add_argument("password", help="log-in, give Password")
database_option.add_argument("-p",
                             help="Check user", action="store_true")
database_option.add_argument("-a", "--add", help="Add user",
                             action="store_true")
database_option.add_argument("-d", "--delete", help="Clean database",
                             action="store_true")
parser.add_argument("-v", "--verbosity", help="Increase output verbosity",
                    action="store_true")

args = parser.parse_args()


# Initialising database manager
manager = DatabaseManager()

# Checking user in database 
if args.p: 
    check = manager.check_for_username_correct(args.username, args.password)
   
    # If user doesn't exist
    if not check:
        sys.exit("Sorry, user doesn't exist")
elif args.add:
    manager.save_new_username_correct(args.username, args.password)
elif args.delete:
    manager.clean_up()
    sys.exit("Database cleaned")

manager.close()

print("This is a program that takes from OpenAQ website the value of",
      "air quality in some city around the world")
print("Available parameter: bc, co, no2, o3, pm10, pm25, so2")

# Initialising Requestor and Util
requestor = OpenAirRequestor()
csv_util = CsvUtil()

# Creating cache of previous requests 
cache = []
while True:
    city = input("Insert the city ")
    parameter = input("Insert parameter ")
   
    # If the city is a new one
    if city not in cache:
        
        # Sending request to the OpenAQ web site for the city
        result = requestor.get_quality(city.capitalize())
       
        # Storing request results 
        csv_util.add_city(result)
        cache.append(city)
    
    # Getting requested parameters from saved data
    air_quality = csv_util.get_data(city, parameter)
    if args.verbosity:
        if air_quality:
            print("The parameter {} of the city {}",
                  "is {}".format(parameter, city.capitalize(), air_quality))
        else:
            print("Sorry, we couldn't find any result for parameter {}",
                  "in {}".format(parameter, city.capitalize()))
    else:
        print(air_quality)

    # Checking if user wants to exit
    # If yes, delete the cvs
    exit = input("Exit? Y/N ")
    if exit.lower() == "y":
        csv_util.delete_cache()
        break
    if exit.lower() != "n":
        csv_util.delete_cache()
        sys.exit("Error! Command not recognised")

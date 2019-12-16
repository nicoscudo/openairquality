import argparse
import sys 
from database.dbmanager import DatabaseManager
from request.openair_requestor import OpenAirRequestor
from csv_util.csv_cache import CsvUtil

parser = argparse.ArgumentParser()
database_option = parser.add_mutually_exclusive_group(required=True)
parser.add_argument("username", help="log-in, give Username")
parser.add_argument("password", help="log-in, give Password")
database_option.add_argument("-p",
                    help="Check user", action="store_true")
database_option.add_argument("-a", "--add", help="Add user", action="store_true")
database_option.add_argument("-d", "--delete", help="Clean database", action="store_true")
parser.add_argument("-v", "--verbosity", help="Increase output verbosity", action="store_true")
args = parser.parse_args()

manager = DatabaseManager()
if args.p:
    check = manager.check_for_username_correct(args.username, args.password)
    if not check:
        sys.exit("Sorry, user doesn't exist")
elif args.add:
    manager.save_new_username_correct(args.username, args.password)
elif args.delete:
    manager.clean_up()
    sys.exit("Database cleaned")

manager.close()
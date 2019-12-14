from openairquality import get_quality


parser = argparse.ArgumentParser()
parser.add_argument("username", help="Username to log-in (password required)")
parser.add_argument("-p", "--password",
                    help="Password to log-in required", required=True)
parser.add_argument("-c", "--city",
                    help="Name of the European city to be sought",
                    required=True)
parser.add_argument("-m", "--mol",
                    help="Polluting molecule required (default=pm10)",
                    choices=list_csv('pypackage/parameters.csv'),
                    default="pm10")
parser.add_argument("-v", "--verbosity", help="Increase output verbosity",
                    action="count")
args = parser.parse_args()






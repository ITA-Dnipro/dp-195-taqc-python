import json
import os	
from pyats import aetest	from pyats import aetest


from settings import host, email, customer_password



def from_file(filename: str):	def from_file(filename: str):
    """Load test data from json file."""	    """Load test data from json file."""
    with open(filename, "r") as data:	    with open(filename, "r") as data:
        return json.loads(data.read())	        return json.loads(data.read())




def test_run(	def test_run() -> None:
    host: str = "127.0.0.1",	    aetest.main(host=host, email=email, password=customer_password)

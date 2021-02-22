# DP-195 group project

## Project structure
The following directories tree outlines the most important information about project structure:
```text
.
├── README.md                      <= This file which documents the project.
├── reports                        <= pyATS reports directory (excluded from git)
├── oct                            <= a root package
│   ├── __main__.py                <= a job file to run all tests
│   ├── tests                      <= a root package for all automated tests
│       └── datafile               <= a directory for tests datafiles
│   └── pages                      <= a root package for page objects
│       ├── base                   <= package containing base classes for page object assessment
│       └── models                 <= a directory for page objects
│   ├── drivers.py                 <= This module contains various selenium driver options available for tests
│   └── device_connection.py       <= This module provides device connection interfaces for test purposes
├── settings.py                    <= This module provides tests with parameters stored in the environmrnt
├── testbed.yaml                   <= Testbed configuration file
├── docker-compose-webabb.yaml     <= This file running app in docker
├── docker-compose-selenium.yaml   <= This file running selenium server in docker
├── requirements.txt               <= Python packages for automated tests execution
├── requirements-dev.txt           <= Python packages for quality of the code
└── code-assessment.sh             <= This file running tools for code quality evaluation
```

## Usage of automated tests
### Installation
Please use Python `3.6.5` for the test execution.

Before running any command complete following steps:

Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

Add setup.py file to oct package:
```{python}
# setup.py
from setuptools import setup

setup()
```

Add oct package to $PYTHONPATH by running following command from inside the package:
```bash
python setup.py develop
```

Create .env file in the project root directory with the following environmet variables:
```bash
PROTOCOL=http
BROWSER=chrome_remote
CUSTOMER_EMAIL=testuser@gmail.com
CUSTOMER_PASSWORD=testpass6
```

Follow this procedure to make your secret strings cryptographically secure:
1. Create inside a virtual environment file:
```bash
$VIRTUAL_ENV/pyats.conf
```

2. Update your pyATS configuration file as follows:
```bash
[secrets]
string.representer = pyats.utils.secret_strings.FernetSecretStringRepresenter
```

3. Generate a cryptographic key:
```bash
> pyats secret keygen
Newly generated key :
dSvoKX23jKQADn20INt3W3B5ogUQmh6Pq00czddHtgU=
```

4. Update your pyATS configuration file as follows:
```bash
[secrets]
string.representer = pyats.utils.secret_strings.FernetSecretStringRepresenter
string.key = dSvoKX23jKQADn20INt3W3B5ogUQmh6Pq00czddHtgU=
```

5. Encode a password:
```bash
> pyats secret encode --string MySecretPassword
Encoded string :
gAAAAABdsgvwElU9_3RTZsRnd4b1l3Es2gV6Y_DUnUE8C9y3SdZGBc2v0B2m9sKVz80jyeYhlWKMDwtqfwlbg4sQ2Y0a843luOrZyyOuCgZ7bxE5X3Dk_NY=
```

6. Add your encoded password to a testbed.yaml %ENC{} block:
```bash
testbed:
    name: sampleTestbed
    credentials:
        default:
            username: admin
            password: "%ENC{gAAAAABdsgvwElU9_3RTZsRnd4b1l3Es2gV6Y_DUnUE8C9y3SdZGBc2v0B2m9sKVz80jyeYhlWKMDwtqfwlbg4sQ2Y0a843luOrZyyOuCgZ7bxE5X3Dk_NY=}"
```

### System under test (SUT) installation

#### Google Cloud
For testing purposes application is being deployed to the Googgle Cloud server.

Make sure you have [Docker](https://docs.docker.com/engine/install/ubuntu/) engine installed on server.
To deploy application, first copy docker-compose files to the server in the the root 
directory of the testuser:
```bash
scp docker-compose-webapp.yaml docker-compose-selenium.yaml testuser@34.107.116.227:~/
```

Connect to the server's testuser via ssh:
```bash
ssh testuser@34.107.116.227
```

Build and start docker containers:
```bash
docker-compose -f docker-compose-webapp.yaml up -d
docker-compose -f docker-compose-selenium.yaml up -d
```

In your browser open http://34.107.116.227 and manually create test user account with followin credantials
```bash
login: testuser
password: testpass6
```

If you want to shutdown docker you must run:
```bash
docker-compose -f docker-compose-webapp.yaml down
docker-compose -f docker-compose-selenium.yaml down
```

### Execution

To run job file:
```bash
python -m oct -testbed_file testbed.yaml -html_logs ./reports/
```

If you need to run a particular test, please run:
```bash
python -m oct.tests.test_script -datafile="./oct/tests/datafile/common_data.yaml" -uids="Or('common_setup, <testcase>')"
```

To view test results open reports directory and choose corresponding Tasklog file 

## Development of automated tests
All contributors have to follow
[Google Python's style guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
until it conflicts with the configured tools for code quality evaluation.

Also, docstrings are optional for the project.

[Type Hints](https://www.python.org/dev/peps/pep-0484/) are mandatory.

### Installation
Please install required Python's dependencies with
```bash
pip install -r requirements-dev.txt
```

### Code formatting
We use [Black](https://black.readthedocs.io/en/stable/) for the auto-formatting of the code.
This allows supporting of common code style across all contributors and will reduce amount of
lines for either merge conflicts or review.

Please run `black .` to reformat the code according to the projects convention.

### Code assessment
We use some tools to guarantee the quality of the code.

1. [Black](https://black.readthedocs.io/en/stable/) checks the quality of the code formatting.
2. [Pylint](https://pylint.org) analyzes the code and assesses it accordingly.
3. [flake8](http://flake8.pycqa.org/en/latest/) applies some style checks on the code.
4. [pydocstyle](http://www.pydocstyle.org/en/stable/) analyses the quality of docstrings
(executed via `flake8`).
5. [Mypy](https://mypy.readthedocs.io/en/latest/) checks static types.
6. [py.test](https://docs.pytest.org) runs unittests.

In order to run code assessment, you need to run `./code-assessment.sh` command and make sure
that there is no message like **_Code assessment is failed! Please fix errors!!!_**. If you face
the massage, please fix all violations.

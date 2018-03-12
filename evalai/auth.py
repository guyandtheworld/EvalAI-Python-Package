import base64
import json
import logging
import os
import pickle
import requests

from cliff.command import Command


def login(username=None, password=None, domain="default"):
    """
    This is used for configuring the authentication details the initial time the user
    logs in. We can also configure the domain to do the requests to. After the initial
    setup the user need not have to log in again.
    """

    if domain == "default":
        url = "http://localhost:8000/api/auth/login"

    auth_details = {
            "username": username,
            "password": password
    }

    response = requests.post(url, auth_details)

    if response.status_code == requests.codes.ok:
        print("You're now logged-in!")
    else:
        print("Something went wrong, please check your connection.")

    token = response.text
    json_token = json.loads(token)
    hashed_token = base64.b64encode(json_token["token"])

    __location__ = os.path.realpath(os.path.join(os.getcwd(),
                                    os.path.dirname(__file__)))
    outputFile = '.data'
    file_path = os.path.join(__location__, outputFile)
    with open(file_path, 'wb') as fw:
        pickle.dump({'Token': hashed_token}, fw)


class LoginCLI(Command):
    "Login to EvalAI"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(LoginCLI, self).get_parser(prog_name)
        parser.add_argument('-u', '--username', help='username')
        parser.add_argument('-p', '--password', help='password')
        return parser

    def take_action(self, parsed_args):
        parsed_arg_dict = vars(parsed_args)

        username = parsed_arg_dict['username']
        password = parsed_arg_dict['password']

        login(username=username, password=password)

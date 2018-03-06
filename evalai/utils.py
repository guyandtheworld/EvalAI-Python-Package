import base64
import os
import pickle


def get_token():
    """
    Loads the user's token after logging in.
    """
    __location__ = os.path.realpath(os.path.join(os.getcwd(),
                                    os.path.dirname(__file__)))
    outputFile = '.data'
    data = []
    with open(os.path.join(__location__, outputFile), 'rb') as fr:
        data = pickle.load(fr)
    token = base64.b64decode(data["Token"])
    return token

import base64
import pickle


def get_token():
    outputFile = '.data'
    data = []
    with open(outputFile, 'rb') as fr:
        data = pickle.load(fr)
    token = base64.b64decode(data["Token"])
    return token
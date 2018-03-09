import base64
import json
import os
import pickle
import requests


AUTH_DETAILS = {}


def get_auth_details():
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

    AUTH_DETAILS = {
            "Authorization": "Token {}".format(token),
    }

    return AUTH_DETAILS


def get_challenge_id(challenge=None, domain=None):
    """
    Checks if the challenge exist and get the challenge id.
    """
    challenges_url = "{}/api/challenges/challenge/present"
    challenges_url = challenges_url.format(domain)
    response = requests.get(challenges_url)

    data = json.loads(response.text)

    if 'results' not in data:
        raise ValueError('Something went wrong, try again.')

    if len(data['results']) == 0:
        raise ValueError('No challenges exists.')

    for json_challenge in data['results']:
        if challenge == json_challenge['title']:
            CHALLENGE_ID = json_challenge['id']
            break

    if CHALLENGE_ID == "":
        raise ValueError('Challenge with that name doesn\'t exist.')

    return CHALLENGE_ID


def get_challenge_phase_id(challenge=None, challenge_phase=None, domain=None):
    """
    Checks if the challenge phase exist and get the challenge phase id.
    """
    CHALLENGE_ID = get_challenge_id(challenge, domain)

    challenge_phase_url = "{}/api/challenges/challenge/{}/challenge_phase"
    challenge_phase_url = challenge_phase_url.format(domain, CHALLENGE_ID)
    response = requests.get(challenge_phase_url)

    data = json.loads(response.text)
    if 'results' not in data:
        raise ValueError('Something went wrong, try again.')

    if len(data['results']) == 0:
        raise ValueError('No challenges phases exists.')

    for json_challenge_phase in data['results']:
        if challenge_phase == json_challenge_phase['name']:
            CHALLENGE_PHASE_ID = json_challenge_phase['id']

    if CHALLENGE_PHASE_ID == "":
        raise ValueError('Challenge phase with that name doesn\'t exist.')

    return CHALLENGE_PHASE_ID

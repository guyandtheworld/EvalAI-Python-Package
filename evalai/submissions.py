import base64
import json
import requests

from utils import get_token


def submit(challenge_title=None, challenge_phase_title=None, submission_file=None, domain="http://localhost:8000"):
    CHALLENGE_ID = ""
    CHALLENGE_PHASE_ID = ""
    TOKEN = get_token()
    AUTH_DETAILS = {
            "Authorization": "Token: {}".format(TOKEN),
    }

    # Checks if the challenge exist and get the challenge id.

    challenges_url = "{}/api/challenges/challenge/present"
    challenges_url = challenges_url.format(domain)
    response = requests.get(challenges_url, AUTH_DETAILS)

    data = json.loads(response.text)

    if 'results' not in data:
        raise ValueError('Something went wrong, try again.')

    if len(data['results']) == 0:
        raise ValueError('No challenges exists.')

    for challenge in data['results']:
        if challenge_title == challenge['title']:
            CHALLENGE_ID = challenge['id']

    if CHALLENGE_ID == "":
        raise ValueError('Challenge with that name doesn\'t exist.')

    # Checks if the challenge phase exist and get the challenge phase id.

    challenge_phase_url = "{}/api/challenges/challenge/{}/challenge_phase"
    challenge_phase_url = challenge_phase_url.format(domain, CHALLENGE_ID)
    response = requests.get(challenge_phase_url, AUTH_DETAILS)

    data = json.loads(response.text)
    if 'results' not in data:
        raise ValueError('Something went wrong, try again.')

    if len(data['results']) == 0:
        raise ValueError('No challenges phases exists.')

    for challenge_phase in data['results']:
        if challenge_phase_title == challenge_phase['name']:
            CHALLENGE_PHASE_ID = challenge_phase['id']

    if CHALLENGE_PHASE_ID == "":
        raise ValueError('Challenge phase with that name doesn\'t exist.')

    print CHALLENGE_ID, CHALLENGE_PHASE_ID

    # Checking if the user is a participant of the challenge.

    # Doing the submissions.

    submission_url = "{}/api/jobs/challenge/{}/challenge_phase/{}/submission/"
    submission_url = submission_url.format(domain, CHALLENGE_ID, CHALLENGE_PHASE_ID)
    files = {'file': open('results.txt', 'rb')}
    AUTH_DETAILS = {
            "Authorization": "Token: {}".format(TOKEN),
    }

    response = requests.get(submission_url, AUTH_DETAILS)
    print response.text

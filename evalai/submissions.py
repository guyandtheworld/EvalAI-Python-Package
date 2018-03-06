import base64
import json
import os
import requests

from utils import get_token


def submit(challenge=None, challenge_phase=None, submission_file=None, domain="http://localhost:8000"):
    """
    This is used to connect to submit a file to a specic phase of an active challenge
    """

    CHALLENGE_ID = ""
    CHALLENGE_PHASE_ID = ""
    PARTICIPATED = False
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

    for json_challenge in data['results']:
        if challenge == json_challenge['title']:
            CHALLENGE_ID = json_challenge['id']
            break

    if CHALLENGE_ID == "":
        raise ValueError('Challenge with that name doesn\'t exist.')


    # Checks if the user is a participant of the Challenge.

    participant_url = "{}/api/participant_teams/challenges/{}/user"
    participant_url = participant_url.format(domain, CHALLENGE_ID)

    response = requests.get(challenges_url, AUTH_DETAILS)

    data = json.loads(response.text)
    print data
    if len(data['results']) == 0:
        raise ValueError('You haven\'t participated in any challenges.')

    for json_challenge in data['results']:
        if challenge == json_challenge['title']:
            PARTICIPATED = True

    if not PARTICIPATED:
        raise ValueError('You have to participate to submit files!')

    # Checks if the challenge phase exist and get the challenge phase id.

    challenge_phase_url = "{}/api/challenges/challenge/{}/challenge_phase"
    challenge_phase_url = challenge_phase_url.format(domain, CHALLENGE_ID)
    response = requests.get(challenge_phase_url, AUTH_DETAILS)

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


    # Doing the submissions.

    submission_url = "{}/api/jobs/challenge/{}/challenge_phase/{}/submission/"
    submission_url = submission_url.format(domain, CHALLENGE_ID, CHALLENGE_PHASE_ID)

    # Location of the submission file
    __location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))

    file = {'file': open(os.path.join(__location__, submission_file), 'rb')}

    AUTH_DETAILS = {
            "Authorization": "Token: {}".format(TOKEN),
    }

    response = requests.post(submission_url, AUTH_DETAILS)

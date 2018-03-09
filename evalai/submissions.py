import base64
import json
import os
import pandas as pd
import requests

from utils import (
                   get_auth_details,
                   get_challenge_id,
                   get_challenge_phase_id
                  )


def submit(challenge=None, challenge_phase=None, submission_file=None, domain="http://localhost:8000"):
    """
    This is used to connect to submit a file to a specic phase of an active challenge
    """

    CHALLENGE_ID = ""
    CHALLENGE_PHASE_ID = ""
    PARTICIPATED = False
    AUTH_DETAILS = get_auth_details()


    CHALLENGE_ID = get_challenge_id(challenge, domain)


    # Checks if the user is a participant of the Challenge.

    challenges_url = "{}/api/challenges/challenge/present"
    challenges_url = challenges_url.format(domain)

    participant_url = "{}/api/participants/participant_teams/challenges/{}/user"
    participant_url = participant_url.format(domain, CHALLENGE_ID)

    response = requests.get(challenges_url, AUTH_DETAILS)
    data = json.loads(response.text)
    if len(data['results']) == 0:
        raise ValueError('You haven\'t participated in any challenges.')

    for json_challenge in data['results']:
        if challenge == json_challenge['title']:
            PARTICIPATED = True

    if not PARTICIPATED:
        raise ValueError('You have to participate to submit files!')


    CHALLENGE_PHASE_ID = get_challenge_phase_id(challenge, challenge_phase, domain)


    # Doing the submissions.

    submission_url = "{}/api/jobs/challenge/{}/challenge_phase/{}/submission/"
    submission_url = submission_url.format(domain, CHALLENGE_ID, CHALLENGE_PHASE_ID)

    # Location of the submission file
    __location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))

    file = {'file': open(os.path.join(__location__, submission_file), 'rb')}
    response = requests.post(submission_url, AUTH_DETAILS)


def leaderboard(challenge=None, challenge_phase=None, domain="http://localhost:8000"):
    """
    pretty prints the leader-board of a particular challenge.
    """
    AUTH_DETAILS = get_auth_details()
    CHALLENGE_ID = get_challenge_id(challenge, domain)
    CHALLENGE_PHASE_ID = get_challenge_phase_id(challenge, challenge_phase, domain)
    PHASE_SPLIT_ID = ""

    # To find the dataset split according to the phase given.
    challenge_split_url = '{}/api/challenges/{}/challenge_phase_split'
    challenge_split_url = challenge_split_url.format(domain, CHALLENGE_ID)
    response = requests.get(challenge_split_url, AUTH_DETAILS)
    data = json.loads(response.text)

    for split in data:
        if CHALLENGE_PHASE_ID == split["challenge_phase"]:
            PHASE_SPLIT_ID = split["challenge_phase"]
            break

    # Get the submission data using the phase split id.
    leaderboard_data_url = "{}/api/jobs/challenge_phase_split/{}/leaderboard/?page_size=1000";
    leaderboard_data_url = leaderboard_data_url.format(domain, PHASE_SPLIT_ID)
    response = requests.get(leaderboard_data_url, AUTH_DETAILS)
    data = json.loads(response.text)
    results = data['results']
    
    # Defining data to be pretty printed.
    participant_team = []
    score = []
    submission_time = []
    for result in results:
        participant_team.append(result['submission__participant_team__team_name'])
        score.append(result['filtering_score'])
        submission_time.append(result['submission__submitted_at'])

    # Converting json list into pandas data frame.
    columns = {'Participant Team': participant_team,
               'Score': score,
               'Submission time': submission_time}
    df = pd.DataFrame(columns)
    df.index += 1
    df.index.names = ['Rank']
    print df


def show_all_my_submissions(challenge=None, challenge_phase=None, domain="http://localhost:8000"):
    """
    pretty prints all the submissions of a particular user.
    """
    AUTH_DETAILS = get_auth_details()
    CHALLENGE_ID = get_challenge_id(challenge, domain)
    CHALLENGE_PHASE_ID = get_challenge_phase_id(challenge, challenge_phase, domain)
    PHASE_SPLIT_ID = ""

    # Fetching user's submission data.
    submissions_url = "{}/api/jobs/challenge/{}/challenge_phase/{}/submission/"
    submissions_url = submissions_url.format(domain, CHALLENGE_ID, CHALLENGE_PHASE_ID)
    response = requests.get(submissions_url, headers=AUTH_DETAILS)
    print response.text


def show_my_last_submission(challenge=None, challenge_phase=None, domain="http://localhost:8000"):
    """
    pretty prints all the submissions of a particular user.
    """
    pass


def get_position_leaderboard(challenge=None, challenge_phase=None, domain="http://localhost:8000"):
    """
    pretty prints all the submissions of a particular user.
    """
    pass


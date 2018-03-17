from evalai import auth, submissions


details = {
            'method_name': "CNN_01",
            'method_description': "First Iteration",
            'project_url': "N/A",
            'publication_url': "N/A",
          }

submissions.submit(
                   challenge="Oasis",
                   challenge_phase="Jeffrey Phase",
                   submission_file="results.csv",
                   submissions_details=details
                   )





# auth.login("user1", "passwor123")
# submissions.leaderboard("Oasis", "Jeffrey Phase")
# submissions.show_all_my_submissions("Oasis", "Jeffrey Phase")
submissions.show_my_last_submission("Oasis", "Jeffrey Phase")

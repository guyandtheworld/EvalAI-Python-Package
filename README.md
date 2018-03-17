# EvalAI-Python-Package

This package can be used connect to the EvalAI server to do a everything from viewing the leader-boards to making the submissions without ever leaving your terminal!

## Installation.

* Use pip to install it on your system.

     `pip install evalai.`


* Set up the package just after installation using your username and password.

    `evalai login -u <USERNAME> -p <PASSWORD>`

And that's it! It's all set-up! You're now ready to use EvalAI through your terminal.

## Usage.

### Making a submissions.

In your python script, import the submission module from the evalai package.

    from evalai import submissions
    
Within your script, pass the challenge name, challenge phase and the result file to this end-point.

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

    
Example : `submissions.submit("MNIST", "Phase 1", "results.csv")`
    
and just run the script and it will display the results on the terminal.
 
### Viewing the leaderboards.

View the common leaderboards.

    submissions.show_leaderboards("<CHALLENGE NAME>", "<CHALLENGE PHASE>")

View the result of your last submission.

    submissions.show_my_last_submissions("<CHALLENGE NAME>", "<CHALLENGE PHASE>")
    
View your all submissions.

    submissions.show_all_my_submissions("<CHALLENGE NAME>", "<CHALLENGE PHASE>")
    

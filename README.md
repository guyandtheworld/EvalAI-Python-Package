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

    `from evalai import submissions`
    
Within your script, pass the challenge name, challenge phase and the result file to this end-point.

    `submissions.submit("<CHALLENGE NAME>", "<CHALLENGE PHASE>", "<RESULT FILE>")`
    
Example : `submissions.submit("MNIST", "Phase 1", "results.csv")`
    
and just run the script and it will display the results on the terminal.
 
    
    

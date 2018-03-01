import logging

from cliff.command import Command


class LoginCLI(Command):
    "Login to EvalAI"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(LoginCLI, self).get_parser(prog_name)
        parser.add_argument('-u', '--username', help='username')
        parser.add_argument('-p', '--password', help='password')
        return parser

    def take_action(self, parsed_args):        
        self.log.info('sending greeting')
        self.log.info(parsed_args)
        self.log.debug('debugging')
        self.app.stdout.write('hi!\n')

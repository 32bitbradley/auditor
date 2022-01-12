import argparse
import logging
import json

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

def parse_cli_args():
    # Load Arguments from CLI
    arg_parser = argparse.ArgumentParser(
        description="Audit things, with auditor!",
        add_help=True,
        epilog="https://github.com/32bitbradley/auditor"
        )
    # Logging args
    logging_args=arg_parser.add_argument_group(
      'logging', 
      'Logging arguments'
    )
    logging_args.add_argument(
        '--verbose',
        '--v',
        dest='logging_verbose',
        action='store_true',
        help="Toggle logging in verbose debug mode",
        required=False,
    )
    # Test Args
    test_args=arg_parser.add_argument_group(
      'test', 
      'Test arguments'
    )
    logging_args.add_argument(
        '--file',
        '--f',
        dest='test_file',
        type=str
        action='store',
        help="The location of a test file",
        required=True,
    )
    args = arg_parser.parse_args()

 if __name__ == "__main__":

    parse_cli_args()
  
    # Set logging level
    if args.script_verbose:
        logger.setLevel("DEBUG")
    else:
        logger.setLevel("INFO")
    

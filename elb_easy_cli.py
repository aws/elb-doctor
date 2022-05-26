"""
Execute library commands from cli
"""

import argparse
from typing import Dict

from elb_easy.lib.get_elb import getElbs



def _execute_cli() -> None:
    """
    basic cli for testing
    """

    # setup the cli parameters
    parser = argparse.ArgumentParser(description='elb easy')
    parser.add_argument('--get-alb', action="store_true", help='retrieve all ALBs within an account', required=False)
    parser.add_argument('--get-nlb', action="store_true", help='retrieve all NLBs within an account', required=False)
        
    
    # cli parameters
    arguments = parser.parse_args()

    # find function to call    
    if arguments.get_alb is True:
        alb_cli()
    elif arguments.get_nlb is True:
        nlb_cli()


def alb_cli() -> Dict:
    get_elb = getElbs
    
    output = get_elb()

    print(output)

def main():
    _execute_cli()


if __name__ == "__main__":
    main()

"""
Execute library commands from cli
"""

import argparse
from argparse import Namespace
from typing import Dict

from elb_easy.lib.getElbs import getElbs
from elb_easy.lib.parseElbs import parseElbs
from elb_easy.lib.alb.parseAlbs import parseAlbs
from elb_easy.lib.nlb.parseNlbs import parseNlbs
from elb_easy.lib.tgs.getAllTgs import getAllTGs
from elb_easy.lib.tgs.parseTgs import parseTgs



def _execute_cli() -> None:
    """
    basic cli for testing
    """

    # setup the cli parameters
    parser = argparse.ArgumentParser(description='elb easy')
    subparsers = parser.add_subparsers()

    elb_cli_parser = subparsers.add_parser('all-elb',
                                            help='Run commands on ALL ELBs')
    elb_cli_parser.set_defaults(func=elb_cli)
    # all-tg set true, no argument required by default
    elb_cli_parser.add_argument('--all-tg',
                                help='retrieve ALL ELB target groups',
                                nargs="?",
                                const=True,
                                required=False)

    # alb subparser
    alb_cli_parser = subparsers.add_parser('get-alb',
                                            help='Run commands on ALBs')
    alb_cli_parser.set_defaults(func=alb_cli)
    alb_cli_parser.add_argument('--alb-arn',
                                type=str,
                                help='retrieve ALB by arn',
                                required=False)
    alb_cli_parser.add_argument('--tg',
                                type=str,
                                help='retrieve ALB target group',
                                required=False)
    # all-tg set true, no argument required by default
    alb_cli_parser.add_argument('--all-tg',
                                help='retrieve ALL ALB target groups',
                                nargs="?",
                                const=True,
                                required=False)

    # nlb subparser
    nlb_cli_parser = subparsers.add_parser('get-nlb',
                                            help='Run commands on NLBs')
    nlb_cli_parser.set_defaults(func=nlb_cli)
    nlb_cli_parser.add_argument('--nlb-arn',
                                type=str,
                                help='retrieve NLB by arn',
                                required=False)
    nlb_cli_parser.add_argument('--tg',
                                type=str,
                                help='retrieve NLB target group',
                                required=False)
    nlb_cli_parser.add_argument('--all-tg',
                                help='retrieve ALL NLB target groups',
                                required=False)

    # find function by name and call
    try:
        # cli parameters
        arguments = parser.parse_args()
        # catch zero parameters and print help
        if "elb_cli" in arguments.func.__name__:
            elb_cli(arguments)
        elif "alb_cli" in arguments.func.__name__:
            alb_cli(arguments)
        elif "nlb_cli" in arguments.func.__name__:
            nlb_cli()
    except AttributeError as no_arguments:
        arguments = parser.parse_args(['--help'])
        print(arguments.print_help())



def elb_cli(arguments: Namespace) -> Dict:
    get_elb = getElbs
    parse_elbs = parseElbs
    all_elbs = parse_elbs(get_elb())
    get_all_tgs = getAllTGs

    # all elbs and all tgs
    if arguments.all_tg:
        response = get_all_tgs(all_elbs)
        for key, value in response.items():
            print(f"\nELB Name: {key}")
            for x, y in value.items():
                print(f"Target Group Name: {x}\nTarget Group Data:\n{y}")
    # all elbs
    else:
        response = all_elbs
        for key, value in response.items():
            print(key, value)


def alb_cli(arguments: Namespace) -> Dict:
    """ALB commands """
    get_elb = getElbs
    get_alb = parseAlbs
    get_all_tgs = getAllTGs
    parse_tg = parseTgs

    # get all albs
    all_alb = get_alb(get_elb())

    if arguments.all_tg is True:
        # get all target groups from all albs
        for key, value in all_alb.items():
            response = get_all_tgs(value)
            #print(response)
            result = parse_tg(response)
            for tg_name, tg_arn in result.items():
                print(f"ALB Name: {key}\nTG Name: \
                        {tg_name}\nTG ARN:{tg_arn}\n")
    elif arguments.tg:
        print(f"Query for specific tg arn")
    else:
        for key, value in all_alb.items():
            print(f"ALB Name: {key}\nALB ARN: {value}")

def nlb_cli() -> Dict:
    get_elb = getElbs
    get_nlb = parseNlbs
    output = get_nlb(get_elb())

    print(output)



def main():
    _execute_cli()


if __name__ == "__main__":
    main()

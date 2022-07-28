"""
Execute library commands from cli
"""

import argparse
from argparse import Namespace
from typing import Dict

from elb_doctor.api.elb_doctor_api import ElbDoctorApi


def _execute_cli() -> None:
    """basic cli for testing"""

    # setup the cli parameters
    parser = argparse.ArgumentParser(description='elb easy')
    subparsers = parser.add_subparsers()

    clb_cli_parser = subparsers.add_parser('get-clb',
                                            help='Run commands on ALL CLBs')
    clb_cli_parser.set_defaults(func=clb_cli)
    # all-tg set true, no argument required by default
    clb_cli_parser.add_argument('--all-tg',
                                help='retrieve ALL CLB target groups',
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
        if "clb_cli" in arguments.func.__name__:
            clb_cli(arguments)
        elif "alb_cli" in arguments.func.__name__:
            alb_cli(arguments)
        elif "nlb_cli" in arguments.func.__name__:
            nlb_cli()
    except AttributeError as no_arguments:
        arguments = parser.parse_args(['--help'])
        print(arguments.print_help())


def clb_cli(arguments: Namespace) -> Dict:
    print("- All CLBs -")
    elb_doctor_api = ElbDoctorApi()
    all_clbs = elb_doctor_api.retrieve_clbs()
    for key, value in all_clbs.items():
        print(f"Name:\t{key}\nLB Name:{value}")

    return all_clbs


def alb_cli(arguments: Namespace) -> Dict:
    """ALB commands """
    print("- All ALBs -")
    elb_doctor_api = ElbDoctorApi()
    all_albs = elb_doctor_api.retrieve_albs()
    for key, value in all_albs.items():
        print(f"Name:\t{key}\nARN:\t{value}")

    return all_albs

"""
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
"""
def nlb_cli() -> Dict:
    print("- All NLBs -")
    elb_doctor_api = ElbDoctorApi()
    all_nlbs = elb_doctor_api.retrieve_nlbs()
    for key, value in all_nlbs.items():
        print(f"Name:\t{key}\nARN:\t{value}")

    return all_nlbs



def main():
    _execute_cli()


if __name__ == "__main__":
    main()

import unittest

from elb_easy.lib.parseElbs import parseElbs


class TestParseElbs(unittest.TestCase):
    """Test class for ELB getter"""
    def setUp(self):
        self.elb_parser = parseElbs

    def test_parse_elbs_one(self):

        elb_response = { "LoadBalancers": [
        {
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
            "858918832707:loadbalancer/net/nlb-elb-easy-test/7a79cd99dbd10456",
            "DNSName": "nlb-elb-easy-test-7a79cd99dbd10456.elb.ap-southeast-2"
            ".amazonaws.com",
            "CanonicalHostedZoneId": "ZCT6FZBF4DROD",
            "CreatedTime": "2022-05-31T22:35:45.032000+00:00",
            "LoadBalancerName": "nlb-elb-easy-test",
            "Scheme": "internet-facing",
            "VpcId": "vpc-9e6a97f8",
            "State": {
                "Code": "active"
            },
            "Type": "network",
            "AvailabilityZones": [
                {
                    "ZoneName": "ap-southeast-2b",
                    "SubnetId": "subnet-29c51361",
                    "LoadBalancerAddresses": []
                },
                {
                    "ZoneName": "ap-southeast-2c",
                    "SubnetId": "subnet-81efbbd9",
                    "LoadBalancerAddresses": []
                }
            ],
            "IpAddressType": "ipv4"
        }]}

        parse_elbs = self.elb_parser(elb_response)

        output = {"nlb-elb-easy-test":"arn:aws:elasticloadbalancing:ap-"
        "southeast-2:858918832707:loadbalancer/net/nlb-elb-easy-test/7a"
        "79cd99dbd10456" }

        self.assertEqual(parse_elbs, output)

    def test_parse_elbs_multiple(self):

        elb_response = { "LoadBalancers": [
        {
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
            "858918832707:loadbalancer/net/nlb-elb-easy-test/7a79cd99dbd10456",
            "DNSName": "nlb-elb-easy-test-7a79cd99dbd10456.elb.ap-southeast-"
            "2.amazonaws.com",
            "CanonicalHostedZoneId": "ZCT6FZBF4DROD",
            "CreatedTime": "2022-05-31T22:35:45.032000+00:00",
            "LoadBalancerName": "nlb-elb-easy-test",
            "Scheme": "internet-facing",
            "VpcId": "vpc-9e6a97f8",
            "State": {
                "Code": "active"
            },
            "Type": "network",
            "AvailabilityZones": [
                {
                    "ZoneName": "ap-southeast-2b",
                    "SubnetId": "subnet-29c51361",
                    "LoadBalancerAddresses": []
                },
                {
                    "ZoneName": "ap-southeast-2c",
                    "SubnetId": "subnet-81efbbd9",
                    "LoadBalancerAddresses": []
                }
            ],
            "IpAddressType": "ipv4"
        },
        {
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
            "858918832707:loadbalancer/app/elb-lab/3d427508418606ed",
            "DNSName": "elb-lab-308521398.ap-southeast-2.elb.amazonaws.com",
            "CanonicalHostedZoneId": "Z1GM3OXH4ZPM65",
            "CreatedTime": "2021-09-22T04:51:31.830000+00:00",
            "LoadBalancerName": "elb-lab",
            "Scheme": "internet-facing",
            "VpcId": "vpc-9e6a97f8",
            "State": {
                "Code": "active"
            },
            "Type": "application",
            "AvailabilityZones": [
                {
                    "ZoneName": "ap-southeast-2b",
                    "SubnetId": "subnet-29c51361",
                    "LoadBalancerAddresses": []
                },
                {
                    "ZoneName": "ap-southeast-2c",
                    "SubnetId": "subnet-81efbbd9",
                    "LoadBalancerAddresses": []
                }
            ],
            "SecurityGroups": [
                "sg-0a0af06a28acb36eb"
            ],
            "IpAddressType": "ipv4"
        }]}

        parse_elbs = self.elb_parser(elb_response)

        output = {"nlb-elb-easy-test":"arn:aws:elasticloadbalancing:ap-"
        "southeast-2:858918832707:loadbalancer/net/nlb-elb-easy-test/7a"
        "79cd99dbd10456", "elb-lab": "arn:aws:elasticloadbalancing:ap-southe"
        "ast-2:858918832707:loadbalancer/app/elb-lab/3d427508418606ed" }

        self.assertEqual(parse_elbs, output)

    def test_parse_elbs_none(self):

        elb_response = {}

        with self.assertRaises(KeyError):
            self.elb_parser(elb_response)

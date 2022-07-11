import unittest

from elb_doctor.elb.parse_elbs import ParseElbs


class TestParseElbs(unittest.TestCase):
    """Test class for ELB getter"""

    def setUp(self):
        # instantiate the class in order to call specific methods later
        self.parse_elbs = ParseElbs()

    def test_parse_nlbs_one(self):
        elb_response = {"LoadBalancers": [
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

        parse_nlbs = self.parse_elbs.parse_nlbs(elb_response)

        output = {"nlb-elb-easy-test": "arn:aws:elasticloadbalancing:ap-southeast-2:858918832707:"
                                       "loadbalancer/net/nlb-elb-easy-test/7a79cd99dbd10456"}

        self.assertEqual(parse_nlbs, output)

    def test_parse_nlbs_multiple(self):
        elb_response = {"LoadBalancers": [
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

        parse_nlbs = self.parse_elbs.parse_nlbs(elb_response)

        output = {"nlb-elb-easy-test": "arn:aws:elasticloadbalancing:ap-southeast-2:858918832707:"
                                       "loadbalancer/net/nlb-elb-easy-test/7a79cd99dbd10456"}

        self.assertEqual(parse_nlbs, output)

    def test_parse_nlbs_none(self):
        elb_response = {}

        with self.assertRaises(KeyError):
            self.parse_elbs.parse_nlbs(elb_response)

    def test_parse_albs_one(self):
        elb_response = {"LoadBalancers": [
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

        parse_albs = self.parse_elbs.parse_albs(elb_response)

        output = {"elb-lab": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                             "858918832707:loadbalancer/app/elb-lab/3d427508418606ed"}

        self.assertEqual(parse_albs, output)

    def test_parse_albs_multiple(self):
        elb_response = {"LoadBalancers": [
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

        parse_albs = self.parse_elbs.parse_albs(elb_response)

        output = {"elb-lab": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                             "858918832707:loadbalancer/app/elb-lab/3d427508418606ed"}

        self.assertEqual(parse_albs, output)

    def test_parse_albs_none(self):
        elb_response = {}

        with self.assertRaises(KeyError):
            self.parse_elbs.parse_albs(elb_response)

    def test_parse_clbs_one(self):
        elb_response = elb_response = {"LoadBalancerDescriptions": [
            {
                "LoadBalancerName": "test-classic-lb",
                "DNSName": "test-classic-lb-2007746508.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneName": "test-classic-lb-2007746508.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneNameID": "Z1GM3OXH4ZPM65",
                "ListenerDescriptions": [
                    {
                        "Listener": {
                            "Protocol": "HTTP",
                            "LoadBalancerPort": 80,
                            "InstanceProtocol": "HTTP",
                            "InstancePort": 80
                        },
                        "PolicyNames": []
                    }
                ],
                "Policies": {
                    "AppCookieStickinessPolicies": [],
                    "LBCookieStickinessPolicies": [],
                    "OtherPolicies": []
                },
                "BackendServerDescriptions": [],
                "AvailabilityZones": [
                    "ap-southeast-2c"
                ],
                "Subnets": [
                    "subnet-81efbbd9"
                ],
                "VPCId": "vpc-9e6a97f8",
                "Instances": [],
                "HealthCheck": {
                    "Target": "TCP:80",
                    "Interval": 30,
                    "Timeout": 5,
                    "UnhealthyThreshold": 2,
                    "HealthyThreshold": 10
                },
                "SourceSecurityGroup": {
                    "OwnerAlias": "858918832707",
                    "GroupName": "default"
                },
                "SecurityGroups": [
                    "sg-0839aa48"
                ],
                "CreatedTime": "2022-07-10T03:55:56.790000+00:00",
                "Scheme": "internet-facing"
            }]}

        parse_clbs = self.parse_elbs.parse_clbs(elb_response)

        output = {"test-classic-lb": "test-classic-lb"}

        self.assertEqual(parse_clbs, output)

    def test_parse_clbs_multiple(self):
        elb_response = {"LoadBalancerDescriptions": [
            {
                "LoadBalancerName": "test-classic-lb",
                "DNSName": "test-classic-lb-2007746508.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneName": "test-classic-lb-2007746508.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneNameID": "Z1GM3OXH4ZPM65",
                "ListenerDescriptions": [
                    {
                        "Listener": {
                            "Protocol": "HTTP",
                            "LoadBalancerPort": 80,
                            "InstanceProtocol": "HTTP",
                            "InstancePort": 80
                        },
                        "PolicyNames": []
                    }
                ],
                "Policies": {
                    "AppCookieStickinessPolicies": [],
                    "LBCookieStickinessPolicies": [],
                    "OtherPolicies": []
                },
                "BackendServerDescriptions": [],
                "AvailabilityZones": [
                    "ap-southeast-2c"
                ],
                "Subnets": [
                    "subnet-81efbbd9"
                ],
                "VPCId": "vpc-9e6a97f8",
                "Instances": [],
                "HealthCheck": {
                    "Target": "TCP:80",
                    "Interval": 30,
                    "Timeout": 5,
                    "UnhealthyThreshold": 2,
                    "HealthyThreshold": 10
                },
                "SourceSecurityGroup": {
                    "OwnerAlias": "858918832707",
                    "GroupName": "default"
                },
                "SecurityGroups": [
                    "sg-0839aa48"
                ],
                "CreatedTime": "2022-07-10T03:55:56.790000+00:00",
                "Scheme": "internet-facing"
            },
            {
                "LoadBalancerName": "test-classic-lb2",
                "DNSName": "test-classic-lb2-1091373944.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneName": "test-classic-lb2-1091373944.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneNameID": "Z1GM3OXH4ZPM65",
                "ListenerDescriptions": [
                    {
                        "Listener": {
                            "Protocol": "HTTP",
                            "LoadBalancerPort": 80,
                            "InstanceProtocol": "HTTP",
                            "InstancePort": 80
                        },
                        "PolicyNames": []
                    }
                ],
                "Policies": {
                    "AppCookieStickinessPolicies": [],
                    "LBCookieStickinessPolicies": [],
                    "OtherPolicies": []
                },
                "BackendServerDescriptions": [],
                "AvailabilityZones": [
                    "ap-southeast-2c"
                ],
                "Subnets": [
                    "subnet-81efbbd9"
                ],
                "VPCId": "vpc-9e6a97f8",
                "Instances": [],
                "HealthCheck": {
                    "Target": "TCP:80",
                    "Interval": 30,
                    "Timeout": 5,
                    "UnhealthyThreshold": 2,
                    "HealthyThreshold": 10
                },
                "SourceSecurityGroup": {
                    "OwnerAlias": "858918832707",
                    "GroupName": "default"
                },
                "SecurityGroups": [
                    "sg-0839aa48"
                ],
                "CreatedTime": "2022-07-10T05:10:21.310000+00:00",
                "Scheme": "internet-facing"
            }]}

        parse_clbs = self.parse_elbs.parse_clbs(elb_response)

        output = {"test-classic-lb": "test-classic-lb", "test-classic-lb2": "test-classic-lb2"}

        self.assertEqual(parse_clbs, output)

    def test_parse_clbs_none(self):
        elb_response = {}

        with self.assertRaises(KeyError):
            self.parse_elbs.parse_clbs(elb_response)

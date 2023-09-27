import unittest

from elb_doctor.lib.elb.parse_elbs import ParseElbs


class TestParseElbs(unittest.TestCase):
    """Test class for ELB getter"""

    def setUp(self):
        # instantiate the class in order to call specific methods later
        self.parse_elbs = ParseElbs()

    def test_parse_nlbs_one(self):
        elb_response = {"LoadBalancers": [
            {
                "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                                   "111111111111:loadbalancer/net/nlb-elb-test/11111111111111111111",
                "DNSName": "nlb-elb-test-11111111111111111111.elb.ap-southeast-2"
                           ".amazonaws.com",
                "CanonicalHostedZoneId": "ZZZZZZZZZZZZZ",
                "CreatedTime": "2022-05-31T22:35:45.032000+00:00",
                "LoadBalancerName": "nlb-elb-test",
                "Scheme": "internet-facing",
                "VpcId": "vpc-99999999",
                "State": {
                    "Code": "active"
                },
                "Type": "network",
                "AvailabilityZones": [
                    {
                        "ZoneName": "ap-southeast-2b",
                        "SubnetId": "subnet-11111111",
                        "LoadBalancerAddresses": []
                    },
                    {
                        "ZoneName": "ap-southeast-2c",
                        "SubnetId": "subnet-22222222",
                        "LoadBalancerAddresses": []
                    }
                ],
                "IpAddressType": "ipv4"
            }]}

        parse_nlbs = self.parse_elbs.parse_nlbs(elb_response)

        output = [{"name": "nlb-elb-test", "value": "arn:aws:elasticloadbalancing:ap-southeast-2:111111111111:"
                                       "loadbalancer/net/nlb-elb-test/11111111111111111111"}]

        self.assertEqual(parse_nlbs, output)

    def test_parse_nlbs_multiple(self):
        elb_response = {"LoadBalancers": [
            {
                "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                                   "111111111111:loadbalancer/net/nlb-elb-test/11111111111111111111",
                "DNSName": "nlb-elb-test-11111111111111111111.elb.ap-southeast-"
                           "2.amazonaws.com",
                "CanonicalHostedZoneId": "ZZZZZZZZZZZZZ",
                "CreatedTime": "2022-05-31T22:35:45.032000+00:00",
                "LoadBalancerName": "nlb-elb-test",
                "Scheme": "internet-facing",
                "VpcId": "vpc-99999999",
                "State": {
                    "Code": "active"
                },
                "Type": "network",
                "AvailabilityZones": [
                    {
                        "ZoneName": "ap-southeast-2b",
                        "SubnetId": "subnet-11111111",
                        "LoadBalancerAddresses": []
                    },
                    {
                        "ZoneName": "ap-southeast-2c",
                        "SubnetId": "subnet-22222222",
                        "LoadBalancerAddresses": []
                    }
                ],
                "IpAddressType": "ipv4"
            },
            {
                "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                                   "111111111111:loadbalancer/app/elb-test/bbbbbbbbbbbbbbbb",
                "DNSName": "elb-test-999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneId": "CCCCCCCCCCCCCC",
                "CreatedTime": "2021-09-22T04:51:31.830000+00:00",
                "LoadBalancerName": "elb-test",
                "Scheme": "internet-facing",
                "VpcId": "vpc-99999999",
                "State": {
                    "Code": "active"
                },
                "Type": "application",
                "AvailabilityZones": [
                    {
                        "ZoneName": "ap-southeast-2b",
                        "SubnetId": "subnet-11111111",
                        "LoadBalancerAddresses": []
                    },
                    {
                        "ZoneName": "ap-southeast-2c",
                        "SubnetId": "subnet-22222222",
                        "LoadBalancerAddresses": []
                    }
                ],
                "SecurityGroups": [
                    "sg-xx1xx1xx1xx1xx1xx1x"
                ],
                "IpAddressType": "ipv4"
            }]}

        parse_nlbs = self.parse_elbs.parse_nlbs(elb_response)

        output = [{"name": "nlb-elb-test", "value": "arn:aws:elasticloadbalancing:ap-southeast-2:111111111111:"
                                       "loadbalancer/net/nlb-elb-test/11111111111111111111"}]

        self.assertEqual(parse_nlbs, output)

    def test_parse_nlbs_none(self):
        elb_response = {}

        with self.assertRaises(KeyError):
            self.parse_elbs.parse_nlbs(elb_response)

    def test_parse_albs_one(self):
        elb_response = {"LoadBalancers": [
            {
                "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                                   "111111111111:loadbalancer/app/elb-test/bbbbbbbbbbbbbbbb",
                "DNSName": "elb-test-999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneId": "CCCCCCCCCCCCCC",
                "CreatedTime": "2021-09-22T04:51:31.830000+00:00",
                "LoadBalancerName": "elb-test",
                "Scheme": "internet-facing",
                "VpcId": "vpc-99999999",
                "State": {
                    "Code": "active"
                },
                "Type": "application",
                "AvailabilityZones": [
                    {
                        "ZoneName": "ap-southeast-2b",
                        "SubnetId": "subnet-11111111",
                        "LoadBalancerAddresses": []
                    },
                    {
                        "ZoneName": "ap-southeast-2c",
                        "SubnetId": "subnet-22222222",
                        "LoadBalancerAddresses": []
                    }
                ],
                "SecurityGroups": [
                    "sg-xx1xx1xx1xx1xx1xx1x"
                ],
                "IpAddressType": "ipv4"
            }]}

        parse_albs = self.parse_elbs.parse_albs(elb_response)

        output = [{"name": "elb-test", "value": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                             "111111111111:loadbalancer/app/elb-test/bbbbbbbbbbbbbbbb"}]

        self.assertEqual(parse_albs, output)

    def test_parse_albs_multiple(self):
        elb_response = {"LoadBalancers": [
            {
                "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                                   "111111111111:loadbalancer/net/nlb-elb-test/11111111111111111111",
                "DNSName": "nlb-elb-test-11111111111111111111.elb.ap-southeast-"
                           "2.amazonaws.com",
                "CanonicalHostedZoneId": "ZZZZZZZZZZZZZ",
                "CreatedTime": "2022-05-31T22:35:45.032000+00:00",
                "LoadBalancerName": "nlb-elb-test",
                "Scheme": "internet-facing",
                "VpcId": "vpc-99999999",
                "State": {
                    "Code": "active"
                },
                "Type": "network",
                "AvailabilityZones": [
                    {
                        "ZoneName": "ap-southeast-2b",
                        "SubnetId": "subnet-11111111",
                        "LoadBalancerAddresses": []
                    },
                    {
                        "ZoneName": "ap-southeast-2c",
                        "SubnetId": "subnet-22222222",
                        "LoadBalancerAddresses": []
                    }
                ],
                "IpAddressType": "ipv4"
            },
            {
                "LoadBalancerArn": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                                   "111111111111:loadbalancer/app/elb-test/bbbbbbbbbbbbbbbb",
                "DNSName": "elb-test-999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneId": "CCCCCCCCCCCCCC",
                "CreatedTime": "2021-09-22T04:51:31.830000+00:00",
                "LoadBalancerName": "elb-test",
                "Scheme": "internet-facing",
                "VpcId": "vpc-99999999",
                "State": {
                    "Code": "active"
                },
                "Type": "application",
                "AvailabilityZones": [
                    {
                        "ZoneName": "ap-southeast-2b",
                        "SubnetId": "subnet-11111111",
                        "LoadBalancerAddresses": []
                    },
                    {
                        "ZoneName": "ap-southeast-2c",
                        "SubnetId": "subnet-22222222",
                        "LoadBalancerAddresses": []
                    }
                ],
                "SecurityGroups": [
                    "sg-xx1xx1xx1xx1xx1xx1x"
                ],
                "IpAddressType": "ipv4"
            }]}

        parse_albs = self.parse_elbs.parse_albs(elb_response)

        output = [{"name": "elb-test", "value": "arn:aws:elasticloadbalancing:ap-southeast-2:"
                             "111111111111:loadbalancer/app/elb-test/bbbbbbbbbbbbbbbb"}]

        self.assertEqual(parse_albs, output)

    def test_parse_albs_none(self):
        elb_response = {}

        with self.assertRaises(KeyError):
            self.parse_elbs.parse_albs(elb_response)

    def test_parse_clbs_one(self):
        elb_response = elb_response = {"LoadBalancerDescriptions": [
            {
                "LoadBalancerName": "test-clb",
                "DNSName": "test-clb-9999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneName": "test-clb-9999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneNameID": "CCCCCCCCCCCCCC",
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
                    "subnet-22222222"
                ],
                "VPCId": "vpc-99999999",
                "Instances": [],
                "HealthCheck": {
                    "Target": "TCP:80",
                    "Interval": 30,
                    "Timeout": 5,
                    "UnhealthyThreshold": 2,
                    "HealthyThreshold": 10
                },
                "SourceSecurityGroup": {
                    "OwnerAlias": "111111111111",
                    "GroupName": "default"
                },
                "SecurityGroups": [
                    "sg-0000aaaa"
                ],
                "CreatedTime": "2022-07-10T03:55:56.790000+00:00",
                "Scheme": "internet-facing"
            }]}

        parse_clbs = self.parse_elbs.parse_clbs(elb_response)

        output = [{"name": "test-clb", "value": "test-clb"}]

        self.assertEqual(parse_clbs, output)

    def test_parse_clbs_multiple(self):
        elb_response = {"LoadBalancerDescriptions": [
            {
                "LoadBalancerName": "test-clb",
                "DNSName": "test-clb-9999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneName": "test-clb-9999999999.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneNameID": "CCCCCCCCCCCCCC",
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
                    "subnet-22222222"
                ],
                "VPCId": "vpc-99999999",
                "Instances": [],
                "HealthCheck": {
                    "Target": "TCP:80",
                    "Interval": 30,
                    "Timeout": 5,
                    "UnhealthyThreshold": 2,
                    "HealthyThreshold": 10
                },
                "SourceSecurityGroup": {
                    "OwnerAlias": "111111111111",
                    "GroupName": "default"
                },
                "SecurityGroups": [
                    "sg-0000aaaa"
                ],
                "CreatedTime": "2022-07-10T03:55:56.790000+00:00",
                "Scheme": "internet-facing"
            },
            {
                "LoadBalancerName": "test-clb-2",
                "DNSName": "test-clb-2-0000000000.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneName": "test-clb-2-0000000000.ap-southeast-2.elb.amazonaws.com",
                "CanonicalHostedZoneNameID": "CCCCCCCCCCCCCC",
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
                    "subnet-22222222"
                ],
                "VPCId": "vpc-99999999",
                "Instances": [],
                "HealthCheck": {
                    "Target": "TCP:80",
                    "Interval": 30,
                    "Timeout": 5,
                    "UnhealthyThreshold": 2,
                    "HealthyThreshold": 10
                },
                "SourceSecurityGroup": {
                    "OwnerAlias": "111111111111",
                    "GroupName": "default"
                },
                "SecurityGroups": [
                    "sg-0000aaaa"
                ],
                "CreatedTime": "2022-07-10T05:10:21.310000+00:00",
                "Scheme": "internet-facing"
            }]}

        parse_clbs = self.parse_elbs.parse_clbs(elb_response)

        output = [{"name": "test-clb", "value": "test-clb"}, {"name": "test-clb-2", "value": "test-clb-2"}]

        self.assertEqual(parse_clbs, output)

    def test_parse_clbs_none(self):
        elb_response = {}

        with self.assertRaises(KeyError):
            self.parse_elbs.parse_clbs(elb_response)

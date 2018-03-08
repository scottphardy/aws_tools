#!/usr/bin/env python3

import json
import pprint
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

sg = ec2.describe_security_groups(
    Filters=[
        {
            'Name': 'tag-value',
            'Values': [
                'java-app',
            ]
        },
    ]
)

ip_permissions = sg.get('SecurityGroups',[{}])[0].get('IpPermissions', '')
ip_permissions_egress = sg.get('SecurityGroups',[{}])[0].get('IpPermissionsEgress', '')
tags = sg.get('SecurityGroups',[{}])[0].get('Tags', '')

# print('IP Permissions: ')
# pprint.pprint(ip_permissions)
# print('\n')

# print('IP Permissions Egress: ')
# pprint.pprint(ip_permissions_egress)
# print('\n')

# print('Tags: ')
# pprint.pprint(tags)
# print('\n')

print('All the SG things: ')
pprint.pprint(sg)
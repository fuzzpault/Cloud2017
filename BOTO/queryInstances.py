# Author: Paul Talaga
#   Date: Feb 1, 2017
#   Desc: This uses the boto library to query the current EC2 instances
#         in your account.

import boto.ec2
import sys

conn = boto.ec2.connect_to_region("us-east-1",
	aws_access_key_id = 'key here',
	aws_secret_access_key = 'secret here')
	
if conn == None:
  print("Error connecting.")
  sys.exit(1)

# Start instances
#conn.run_instances(
#            'ami-0b33d91d',
#            key_name='UbuntuKey',   # your ssh keypair name
#            instance_type='t2.micro',
#            security_groups=['ssh-http']) # security group name
            
            # print instances
instances = conn.get_only_instances()
#instances = conn.get_all_reservations()
if len(instances) == 0:
  print("No instances running");
for i in instances:
    print("id", i.id, " DNS", i.dns_name," IP", i.ip_address)

# Shutdown all instances (terminate)

#instance_ids = map(lambda a:a.id,instances)

#conn.terminate_instances(instance_ids = instance_ids)


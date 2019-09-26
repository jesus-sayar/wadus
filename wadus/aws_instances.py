import boto3

class AwsInstances:
    def __init__(self, writer):
        self.ec2 = boto3.resource('ec2')
        self.writer = writer

    def list(self):
        filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
        instances = self.ec2.instances.filter(Filters=filters)

        table_headers = ['Name', 'ID', 'Type', 'Public IP', 'Private IP', 'Zone', 'Roles', 'Stages']
        table_data = []
        for i in instances:
            if i.tags:
                tags = dict(map((lambda x: [x['Key'],x['Value']]),i.tags))
                table_data.append([tags.get('Name'),
                                  i.id,
                                  i.instance_type,
                                  i.public_ip_address,
                                  i.private_ip_address,
                                  i.placement['AvailabilityZone'],
                                  tags.get('Roles'),
                                  tags.get('Stages')])


        self.writer.write(table_headers, table_data)

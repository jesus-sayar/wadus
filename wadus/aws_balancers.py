import boto3


class AwsBalancers:
    def __init__(self, writer):
        self.elb = boto3.client('elb')
        self.writer = writer

    def list(self):
        balancers_info = self.elb.describe_load_balancers().get('LoadBalancerDescriptions')
        table_headers = ['Name', 'DNS', 'Instances', 'Availability Zones']
        table_data = []
        for b in balancers_info:
            table_data.append([b.get('LoadBalancerName'),
                               b.get('DNSName'),
                               len(b.get('Instances')),
                               ', '.join(b.get('AvailabilityZones'))])

        self.writer.write(table_headers, table_data)
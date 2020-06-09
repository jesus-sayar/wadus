import boto3
from terminaltables import AsciiTable
from wadus.aws_sts import AwsSts

class AwsAmis:
    def __init__(self, writer):
        self.ec2 = boto3.client('ec2')
        self.writer = writer

    def list(self):
        aws_sts = AwsSts()
        sts_info = aws_sts.get_info()
        amis_info = self.ec2.describe_images(Filters=[{'Name':'owner-id', 'Values':[sts_info.get('Account')]}]).get('Images')

        table_headers = ['AMI ID', 'Creation date', 'AMI Name']
        table_data = []
        for i in amis_info:
            table_data.append([i.get('ImageId'),
                            i.get('CreationDate'),
                            i.get('Name')])
                            
        self.writer.write(table_headers, table_data)

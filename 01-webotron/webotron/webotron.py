import boto3
import click

session = boto3.Session(profile_name='python')
s3 = session.resource('s3')

@click.group()
def cli():
    "webotron deploys website to aws"
    pass

@cli.command('list-buckets')
def list_buckets():
    "list all s3 buckets"
    for bucket in s3.buckets.all():
       print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "list object in an s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
    

if __name__ == '__main__':
    cli()
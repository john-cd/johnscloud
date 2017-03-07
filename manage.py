#!/usr/bin/env python
"""
Manage 
- the configuration S3 bucket
- the CloudFormation stacks

INSTALL

$ pip install boto3
$ pip install click

BUCKET STRUCTURE


"""
import boto3
import click

@click.group()
def cli():
    pass
 
@cli.command()
def list_buckets():
    """Print out bucket names"""
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

@cli.command()
@click.argument('name_root', type=click.STRING)
def create_config_bucket(name_root: str):
    """"""
    # all bucket names should comply with DNS naming conventions
    # Bucket names must be at least 3 and no more than 63 characters long.
    # Bucket names must be a series of one or more labels. Adjacent labels are separated by a single period (.). Bucket names can contain lowercase letters, numbers, and hyphens. Each label must start and end with a lowercase letter or a number.
    # Bucket names must not be formatted as an IP address (e.g., 192.168.5.4).  
    bucket_name = "config."+ name_root.lower()
    assert (len(bucket_name) >= 3) and (len(bucket_name) <= 63)
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    response = bucket.create(ACL='private')
    return response



    

if __name__ == '__main__':
    cli()
    
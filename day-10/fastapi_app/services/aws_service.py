# services/aws_service.py
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Any

def get_bucket_info() -> Dict[str, Any]:
    """
    Get S3 buckets categorized by age (90+ days vs newer).
    Returns counts and names of old/new buckets.
    """
    try:
        s3_client = boto3.client("s3")
        buckets = s3_client.list_buckets()["Buckets"]
        current_date = datetime.now(timezone.utc).astimezone()
        new_buckets = []
        old_buckets = []
        
        days_ago_90 = current_date - timedelta(days=90)
        for bucket in buckets:
            bucket_name = bucket["Name"]
            creation_date = bucket["CreationDate"]
            if creation_date < days_ago_90:
                old_buckets.append(bucket_name)
            else:
                new_buckets.append(bucket_name)

        return {
            "total_buckets": len(buckets),
            "new_buckets": len(new_buckets),
            "old_buckets": len(old_buckets),
            "new_buckets_names": new_buckets,
            "old_buckets_names": old_buckets
        }
    except NoCredentialsError:
        return {"error": "AWS credentials not configured"}
    except ClientError as e:
        return {"error": f"AWS Error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

def show_instances() -> Dict[str, Any]:
    """
    Get running EC2 instances with basic info.
    """
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'instance_id': instance['InstanceId'],
                    'state': instance['State']['Name'],
                    'instance_type': instance.get('InstanceType', 'N/A'),
                    'launch_time': instance['LaunchTime'].isoformat() if instance['LaunchTime'] else 'N/A',
                    'public_ip': instance.get('PublicIpAddress', 'N/A')
                })
        
        return {
            "running_instances": instances, 
            "total": len(instances)
        }
    except NoCredentialsError:
        return {"error": "AWS credentials not configured"}
    except ClientError as e:
        return {"error": f"AWS Error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

def get_ec2_regions() -> Dict[str, Any]:
    """
    List all AWS regions.
    """
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_regions()
        regions = [{"name": region['RegionName'], "endpoint": region['RegionEndpoint']} 
                  for region in response['Regions']]
        return {"regions": regions, "total": len(regions)}
    except Exception as e:
        return {"error": f"Error fetching regions: {str(e)}"}

def get_account_info() -> Dict[str, Any]:
    """
    Get basic AWS account information.
    """
    try:
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
        user_id = sts_client.get_caller_identity()['UserId']
        arn = sts_client.get_caller_identity()['Arn']
        
        return {
            "account_id": account_id,
            "user_id": user_id,
            "arn": arn
        }
    except Exception as e:
        return {"error": f"Error fetching account info: {str(e)}"}

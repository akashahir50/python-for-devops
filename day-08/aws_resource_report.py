import boto3
import json

def connect_to_aws():
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    s3_client = boto3.client('s3')
    return ec2_client, s3_client


def get_ec2_instances(ec2_client):
    instances = []
    response = ec2_client.describe_instances()
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            name = 'N/A'
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break
            
            instances.append({
                'InstanceId': instance['InstanceId'],
                'Name': tag['Value']  
            })
    return instances


def get_s3_buckets(s3_client):
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return buckets


def show_report(instances, buckets):
    print(f"\nInstances ({len(instances)}):")
    if instances:
        for inst in instances:
            print(f"  Instance id: {inst['InstanceId']}, Instance name: {inst['Name']}")
    else:
        print("  No instances found")
    
    print(f"\nBuckets ({len(buckets)}):")
    if buckets:
        for bucket in buckets:
            print(f"  Bucket name: {bucket}")
    else:
        print("  No buckets found")


def save_json_report(instances, buckets, filename='aws_report.json'):
    report = {
        'ec2_instances': instances,
        's3_buckets': buckets
    }
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to {filename}")


def main():
    ec2, s3 = connect_to_aws()
    instances = get_ec2_instances(ec2)
    buckets = get_s3_buckets(s3)
    show_report(instances, buckets)
    save_json_report(instances, buckets)


if __name__ == "__main__":
    main()

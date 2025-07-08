import pandas as pd
import boto3
import os
import pymysql
from sqlalchemy import create_engine
from botocore.exceptions import ClientError

# ENV variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")
s3_bucket = os.getenv("S3_BUCKET")
csv_key = os.getenv("CSV_KEY")

rds_host = os.getenv("RDS_HOST")
rds_user = os.getenv("RDS_USER")
rds_pass = os.getenv("RDS_PASS")
rds_db = os.getenv("RDS_DB")
rds_table = os.getenv("RDS_TABLE")

# Step 1: Download CSV from S3
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key,
                  aws_secret_access_key=aws_secret_key,
                  region_name=region)

local_csv = '/tmp/data.csv'

try:
    s3.download_file(s3_bucket, csv_key, local_csv)
    print("✅ CSV downloaded from S3.")
except Exception as e:
    print(f"❌ Failed to download from S3: {e}")
    exit()

# Step 2: Parse CSV
df = pd.read_csv(local_csv)
print("✅ CSV parsed using pandas.")

# Step 3: Try to upload to RDS
try:
    engine = create_engine(f'mysql+pymysql://{rds_user}:{rds_pass}@{rds_host}/{rds_db}')
    df.to_sql(rds_table, con=engine, if_exists='replace', index=False)
    print("✅ Data uploaded to RDS successfully.")
except Exception as e:
    print(f"❌ Failed to upload to RDS. {e}")
    print("⚠️ Fallback to Glue will be implemented here.")

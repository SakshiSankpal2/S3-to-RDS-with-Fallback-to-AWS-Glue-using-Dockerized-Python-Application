# 🚀 Project: Data Ingestion from S3 to RDS with Fallback to AWS Glue using Dockerized Python Application

## 🧠 Objective
Build a **Dockerized Python Application** that:
- ✅ Reads a CSV file from an Amazon S3 bucket
- ✅ Pushes it into an **RDS (MySQL)** database
- ✅ Falls back to **AWS Glue** if the RDS upload fails

---

## 🛠️ Tech Stack Used
- **AWS Services:** S3, RDS (MySQL), Glue, IAM
- **Python 3.9+**
- **Docker**
- **boto3**, **pandas**, **pymysql**
- **Ubuntu EC2** instance (for running the container)

---

## 📁 Folder Structure

```
.
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔧 Step-by-Step Setup

### 1. 📦 Prerequisites
- AWS Account with admin access
- IAM role attached to EC2 with permissions for S3, RDS, Glue
- Ubuntu EC2 instance with Docker and AWS CLI installed

### 2. 🗂️ Create and Upload CSV to S3
- S3 Bucket: `sakshi-csv-bucket`
- Uploaded File: `sample.csv`

### 3. 🛢️ Create RDS MySQL DB
- Endpoint: `datadb.ctkkomg4kwww.ap-south-1.rds.amazonaws.com`
- DB Name: `datadb`
- Table: `user`
- Columns: `id, name, email, command, contacts`

### 4. 🧪 Prepare Python Script (main.py)
- Reads CSV from S3 using `boto3`
- Parses CSV using `pandas`
- Tries inserting into MySQL RDS via `pymysql`
- On failure → creates Glue table from S3

### 5. 🐳 Create Dockerfile

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### 6. 📜 requirements.txt

```
boto3
pandas
pymysql
```

### 7. 🛠️ Build Docker Image

```bash
sudo docker build -t s3-rds-glue-app .
```

### 8. 🚀 Run the Container

```bash
sudo docker run --rm \
-e AWS_ACCESS_KEY_ID=... \
-e AWS_SECRET_ACCESS_KEY=... \
-e AWS_REGION=ap-south-1 \
-e S3_BUCKET=sakshi-csv-bucket \
-e CSV_KEY=sample.csv \
-e RDS_HOST=datadb.ctkkomg4kwww.ap-south-1.rds.amazonaws.com \
-e RDS_USER=admin \
-e RDS_PASS='Pass$123' \
-e RDS_DB=datadb \
-e RDS_TABLE=user \
-e GLUE_DB=glue_test_db \
-e GLUE_TABLE=user_backup \
-e GLUE_S3_LOCATION=s3://sakshi-csv-bucket/ \
s3-rds-glue-app
```

---

## ✅ Output

- If RDS is reachable → inserts data into MySQL
- If RDS fails → fallback to AWS Glue and creates external table

---

## 📸 Screenshots (Add Your Own)

- [ ] S3 File
- [ ] RDS Table
- [ ] Docker Success Logs
- [ ] Glue Table Created

---

## 📚 Summary

| Feature               | Status |
|------------------------|--------|
| S3 → RDS               | ✅ Done |
| RDS Fails → Glue Fallback | ✅ Done |
| Dockerized             | ✅ Done |
| Reproducible Script    | ✅ Done |

---

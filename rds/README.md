# Amazon Relational Database Service (RDS)

Amazon Relational Database Service (RDS) is a managed service that makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.

## Steps that I followed to create an RDS instance:
- Create Security Group with inbound rules for PostgreSQL port 5432

- Sign in to the AWS Management Console
- Open the Amazon RDS console at https://console.aws.amazon.com/rds/
- In the navigation pane, choose Databases, and then choose Create database.
- I created a PostgreSQL database instance
- Select Free tier
- Master username: postgres
- Select AWS Secrets Manager to store the master password
- Choose Create database
- Public access: Yes (for testing purposes)
- Rest of the settings were default
- Choose Create database
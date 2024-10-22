import boto3
import json
from sqlalchemy import create_engine

# The secret name should be the same as the secret name in AWS Secrets Manager (Not in RDS, SECRETS MANAGER!!!)
SECRET_NAME = 'rds!db-3d70c27d-2ed6-416b-8f43-bb00ee5630df'
# The region name is swown in the top right corner of the AWS Console
REGION_NAME = 'us-east-2'
USERNSME = 'postgres'
PASSWORD = '}i>OcrjX>]O{un0W4E?>?em*vspt'
HOST = 'chrisdbinstance.czwswysc0j24.us-east-2.rds.amazonaws.com'
PORT = '5432'

# Global variables to store the connection
connection = None
cursor = None

def get_secret():
    """
    Get the secret from AWS Secrets Manager
    This is a most secure way to store the secret key
    """

    client = boto3.client('secretsmanager', region_name=REGION_NAME)
    response = client.get_secret_value(SecretId=SECRET_NAME)
    secret_data = json.loads(response['SecretString'])

    return secret_data

def get_connection():
    """
    Get the connection to the database
    """

    global connection, cursor

    if connection is None:
        secret_data = get_secret()
        connection_string = f'postgresql://{USERNSME}:{secret_data["password"]}@{HOST}:{PORT}/postgres'

        print(f'Connecting to the database using the connection string: {connection_string}')

        engine = create_engine(connection_string)

        connection = engine.connect()
        cursor = connection.connection.cursor()

def lambda_handler(event, context):
    """
    Lambda handler
    """

    try:
        get_connection()

        # Get all the tables in the database
        tables = connection.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        for table in tables:
            print(table)

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully connected to the database')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error connecting to the database: {str(e)}')
        }
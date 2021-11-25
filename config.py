from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['PSSQL_USER']
password = os.environ['PSSQL_PASSWORD']
host = os.environ['PSSQL_HOST']
database = os.environ['PSSQL_DATABASE']
port = os.environ['PSSQL_PORT']

DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
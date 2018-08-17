import splunklib.client as client
import config

#export PYTHONHTTPSVERIFY=0



import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context


HOST = config.DATABASE_CONFIG['host']
PORT = config.DATABASE_CONFIG['port']
USERNAME = config.DATABASE_CONFIG['username']
PASSWORD = config.DATABASE_CONFIG['password']

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print app.name

jobs = service.jobs

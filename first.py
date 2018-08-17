import splunklib.client as client

#export PYTHONHTTPSVERIFY=0



import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context





HOST = "localhost"
PORT = 8089
USERNAME = "admin"
PASSWORD = "Lak@1993"

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

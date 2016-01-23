import httplib2

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

# REPLACE WITH YOUR Project ID
PROJECT_NUMBER = 'reddit-corpus-browser'
# REPLACE WITH THE SERVICE ACCOUNT EMAIL FROM GOOGLE DEV CONSOLE
SERVICE_ACCOUNT_EMAIL = 'reddit-corpus-browser@reddit-corpus-analysis.iam.gserviceaccount.com'

f = file('../creds/Reddit Corpus Analysis-de89c8858ff2.json', 'rb')
key = f.read()
f.close()

credentials = SignedJwtAssertionCredentials(
    SERVICE_ACCOUNT_EMAIL,
    key,
    scope='https://www.googleapis.com/auth/bigquery.readonly')

http = httplib2.Http()
http = credentials.authorize(http)

service = build('bigquery', 'v2')
tables = service.tables()
response = tables.list(projectId=PROJECT_NUMBER, datasetId='fh-bigquery:reddit_comments').execute(http)

print(response)

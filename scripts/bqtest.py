#!/usr/bin/env python

from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

project_id='reddit-corpus-analysis'

# Grab the application's default credentials from the environment.
credentials = GoogleCredentials.get_application_default()
# Construct the service object for interacting with the BigQuery API.
bigquery_service = build('bigquery', 'v2', credentials=credentials)

fh_reddit_tables = """
[fh-bigquery:reddit_comments.2007],
[fh-bigquery:reddit_comments.2008],
[fh-bigquery:reddit_comments.2009],
[fh-bigquery:reddit_comments.2010],
[fh-bigquery:reddit_comments.2011],
[fh-bigquery:reddit_comments.2012],
[fh-bigquery:reddit_comments.2013],
[fh-bigquery:reddit_comments.2014],
[fh-bigquery:reddit_comments.2015_01],
[fh-bigquery:reddit_comments.2015_02],
[fh-bigquery:reddit_comments.2015_03],
[fh-bigquery:reddit_comments.2015_04],
[fh-bigquery:reddit_comments.2015_05],
[fh-bigquery:reddit_comments.2015_06],
[fh-bigquery:reddit_comments.2015_07],
[fh-bigquery:reddit_comments.2015_08]
"""

query_request = bigquery_service.jobs()

shakespeare = True

if shakespeare:
    query_data = {
        'query': (
            'SELECT TOP(corpus, 10) as title, '
            'COUNT(*) as unique_words '
            'FROM [publicdata:samples.shakespeare];')
    }
else:
    query_data = {'query': ('select count(*) from %s' % fh_reddit_tables)}

query_response = query_request.query(
    projectId=project_id,
    body=query_data).execute()

print('Query Results:')
for row in query_response['rows']:
    print('\t'.join(field['v'] for field in row['f']))

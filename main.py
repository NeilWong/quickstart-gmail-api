from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import auth

def get_labels():
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

authInst = auth.auth(SCOPES)

credentials = authInst.get_credentials()

service = build('gmail', 'v1', http=credentials.authorize(Http()))

get_labels()

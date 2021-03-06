#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple intro to using the Google Analytics API v3.

This application demonstrates how to use the python client library to access
Google Analytics data. The sample traverses the Management API to obtain the
authorized user's first profile ID. Then the sample uses this ID to
contstruct a Core Reporting API query to return the top 25 organic search
terms.

Before you begin, you must sigup for a new project in the Google APIs console:
https://code.google.com/apis/console

Then register the project to use OAuth2.0 for installed applications.

Finally you will need to add the client id, client secret, and redirect URL
into the client_secrets.json file that is in the same directory as this sample.

Sample Usage:

  $ python hello_analytics_api_v3.py

Also you can also get help on all the command-line flags the program
understands by running:

  $ python hello_analytics_api_v3.py --help
"""

__author__ = 'api.nickm@gmail.com (Nick Mihailovski)'

import argparse
import sys


from apiclient.errors import HttpError
from apiclient import sample_tools
from oauth2client.client import AccessTokenRefreshError

from datetime import *
from dateutil.relativedelta import *
import calendar

def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'analytics', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/analytics.readonly')

  today = date.today()
  #FIXME big leap year bug!
  #today = datetime(2012, 2, 29)
  amo = today - relativedelta(days = +31)
  ayo = today - relativedelta(months = +12)
  ayamo = ayo - relativedelta(days = +31)




  # Try to make a request to the API. Print the results or handle errors.
  try:
    first_profile_id = get_first_profile_id(service)
    if not first_profile_id:
      print 'Could not find a valid profile for this user.'
    else:

      results_ly = get_hits(service, first_profile_id, ayamo, ayo)
      results_ty = get_hits(service, first_profile_id, amo, today)

      #results = get_hits(service, first_profile_id, start_date, end_date)
      # print("LY:")
      # print_results(results_ly)
      # print("TY:")
      # print_results(results_ty)

      ## FIXME GIANT LEAP DAY BUG!!!
      print_results2(results_ly, results_ty)


  except TypeError, error:
    # Handle errors in constructing a query.
    print ('There was an error in constructing your query : %s' % error)

  except HttpError, error:
    # Handle API errors.
    print ('Arg, there was an API error : %s : %s' %
           (error.resp.status, error._get_reason()))

  except AccessTokenRefreshError:
    # Handle Auth errors.
    print ('The credentials have been revoked or expired, please re-run '
           'the application to re-authorize')


def get_first_profile_id(service):
  """Traverses Management API to return the first profile id.

  This first queries the Accounts collection to get the first account ID.
  This ID is used to query the Webproperties collection to retrieve the first
  webproperty ID. And both account and webproperty IDs are used to query the
  Profile collection to get the first profile id.

  Args:
    service: The service object built by the Google API Python client library.

  Returns:
    A string with the first profile ID. None if a user does not have any
    accounts, webproperties, or profiles.
  """

  accounts = service.management().accounts().list().execute()



  if accounts.get('items'):
    items = accounts.get('items')
    for item in items:
        if item.get('name') == "www.bioconductor.org":
            firstAccountId = item.get('id')
            webproperties = service.management().webproperties().list(
              accountId=firstAccountId).execute()
    if not firstAccountId:
        return None

    if webproperties.get('items'):
      firstWebpropertyId = webproperties.get('items')[0].get('id')
      profiles = service.management().profiles().list(
          accountId=firstAccountId,
          webPropertyId=firstWebpropertyId).execute()

      if profiles.get('items'):
        return profiles.get('items')[0].get('id')

  return None


def get_hits(service, profile_id, start_date, end_date):
  """Executes and returns data from the Core Reporting API.

  This queries the API for the top 25 organic search terms by visits.

  Args:
    service: The service object built by the Google API Python client library.
    profile_id: String The profile ID from which to retrieve analytics data.

  Returns:
    The response returned from the Core Reporting API.
  """

  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date="%s-%02d-%02d" %(start_date.year, start_date.month, start_date.day),
      end_date="%s-%02d-%02d" %(end_date.year, end_date.month, end_date.day),
      metrics='ga:visitors',
      dimensions='ga:date',
#      sort='-ga:visits',
#      filters='ga:medium==organic',
      start_index='1',
      max_results='40').execute() 


def print_results(results):
  """Prints out the results.

  This prints out the profile name, the column headers, and all the rows of
  data.

  Args:
    results: The response returned from the Core Reporting API.
  """

  #print
  #print 'Profile Name: %s' % results.get('profileInfo').get('profileName')
  #print

  # Print header.
  output = []
  for header in results.get('columnHeaders'):
    output.append('%s' % header.get('name'))
  #print '\t'.join(output)
  print("date\thits")

  # Print data table.
  if results.get('rows', []):
    for row in results.get('rows'):
      if (row[0] == "(not provided)"):
        continue
      output = []
      date = datetime.strptime(row[0], "%Y%m%d")
      output.append(datetime.strftime(date, "%m-%d"))
      output.append(row[1])
#      for cell in row:
        #print(cell.__class__.__name__)
#        output.append('%s' % cell)
      print '\t'.join(output)

  else:
    print 'No Rows Found'

def print_results2(results_ly, results_ty):
  """Prints out the results.

  This prints out the profile name, the column headers, and all the rows of
  data.

  Args:
    results: The response returned from the Core Reporting API.
  """

  #print
  #print 'Profile Name: %s' % results.get('profileInfo').get('profileName')
  #print

  # Print header.
  output = []
#  for header in results.get('columnHeaders'):
#    output.append('%s' % header.get('name'))
  #print '\t'.join(output)
  print("date\tlast year\tthis year")

  # Print data table.
  if results_ly.get('rows', []):
    rows_ly = results_ly.get('rows')
    rows_ty = results_ty.get('rows')
#    print(rows_ly.__class__.__name__)
#    print(len(rows_ly))
    for i in range(len(rows_ly)):
    #for row in results.get('rows'):
      row_ly = rows_ly[i]
      row_ty = rows_ty[i]
      if (row_ly[0] == "(not provided)"):
        continue
      output = []
      date = datetime.strptime(row_ly[0], "%Y%m%d")
      output.append(datetime.strftime(date, "%m-%d"))
      output.append(row_ly[1])
      output.append(row_ty[1])
#      for cell in row:
        #print(cell.__class__.__name__)
#        output.append('%s' % cell)
      print '\t'.join(output)

  else:
    print 'No Rows Found'



if __name__ == '__main__':
  main(sys.argv)

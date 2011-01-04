#!/usr/bin/env python
"""
This example shows how to iterate over last 100 django commits from the github.
"""

import urllib
import simplejson
import pagerator

def get_page(page):
    page -= 1 # on the github, pages numbers begin from 1
    data = urllib.urlopen('http://github.com/api/v2/json/commits/list/django/django/master?page=%s' % page).read()
    json = simplejson.loads(data)
    return json['commits']

def show_last_n(limit):
    all_commits = pagerator.IterableQuery(get_page, 35)
    for commit in all_commits[:100]:
        print '======= %s ======' % commit['id']
        print commit['message']
        print ''


if __name__ == '__main__':
    show_last_n(100)

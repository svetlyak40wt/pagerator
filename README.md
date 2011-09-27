Pagerator — iterates over pages.
================================

This is a helper to build iterables when you need to fetch results already
divided into the pages.

Quick example
-------------

This is example, how easy to fetch 100 latest commits from the Django's repository using pythonic way.

    :::python
    #!/usr/bin/env python
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


Features
--------

* Pagerator is able to create iterable objects to iterate over all pages.
* Or python slicing could be used:

        from pagerator import IterableQuery
        # ... define page getting routine
        query = IterableQuery(get_page, page_size = 20)
        for item in query[100:50]:
            do_somthing_with(item)

* Queries are immutable and you could use it many times:

        from pagerator import IterableQuery
        # ... define page getting routine
        query = IterableQuery(get_page, page_size = 20)
        first_page_iterator = query[:100]
        second_page_iterator = query[100:200]
        # ...

* You even may use subslicing and it will work correctly: `query[1000:][20:30]`.

Changes
-------

### 0.1.1
  * Fixed issue with [0:0] slice.

Author
------

Alexander Artemenko, <svetlyak.40wt@gmail.com>

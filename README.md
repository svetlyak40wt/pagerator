Pagerator — iterates over pages.
================================

This is a helper to build iterables when you need to fetch results already
divided into the pages.

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

See `example.py` for more details. It contains a short example, how to fetch
100 latest commits from the Django's repository using pythonic way.


Author
------

Alexander Artemenko, svetlyak.40wt@gmail.com.

GitHub Repo Search
==================

Command line searching of GitHub repos.

Installation
------------
Add your GitHub username and password to gitsearch.py
Select your default language to search for.
Make gitsearch.py executable and copy to your path.
    
    cp ./gitsearch/gitsearch.py /usr/local/bin/gitsearch
    chmod -x /usr/local/bin/gitsearch

Searching
---------

You can search using the specific flags -q and -l: 
    
    gitsearch -q "web frameworks" -l "python"

Or pass everything as arguments:
    
    gitsearch python web frameworks

The first argument will be checked against a list of languages
and filter the results if you select a valid language.
All non-lanugage arguments will be sent as the query.
Results are filtered to show only the most popular, unique repos.

Example
-------
    
    $ gitsearch python web frameworks
    
    >>> Results for "web frameworks" in python <<<
    >>> Next Result (n) / Open Link (o) / Load All (l) / Quit (q) <<<
    ------------------------------------------------------------
    django               | 5180 stars | github.com/django/django
    The Web framework for perfectionists with deadlines.
    ------------------------------------------------------------
    webpy                | 2195 stars | github.com/webpy/webpy
    web.py is a web framework for python that is as simple as it is powerful. 
    ------------------------------------------------------------

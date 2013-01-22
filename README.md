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

Results
-------

Results are filtered to show only the most popular, unique repos.
One repo at a time is shown, with the option to open a link to the repo.
Pressing l loads all the results.

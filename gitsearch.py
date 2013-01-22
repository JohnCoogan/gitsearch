#!/usr/bin/python

from github import Github
from optparse import OptionParser
from itertools import groupby
import subprocess

GITHUB_USERNAME = ''
GITHUB_PASSWORD = ''
LANGUAGES = ['javascript','ruby','python','java','shell','php','c','c++','perl','objective-c']
DEFAULT_LANGAUGE = 'python'

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def search_github(query, language):
    ''' Searches GitHub for repos matching the query and language.
        Fiters out duplicate repos & forks, then sorts by # of stars.
    '''
    getch = _Getch()
    g = Github(GITHUB_USERNAME,GITHUB_PASSWORD)
    search = g.legacy_search_repos(query, language)
    results = [f for f in search.get_page(0)]
    r_data = [{'forks':x._forks, 'stars':x._watchers, 'url':x._url, 'name':x._name, 'language':x._language, 'created_at':x._created_at, 'description':x._description} for x in results]
    r_alpha = sorted(r_data, key=lambda x: x['name'], reverse=True)
    r_uniques = [sorted(list(g), key=lambda x: x['stars'], reverse=True)[0] for k, g in groupby(r_alpha, lambda x: x['name'])]
    r_sorted = sorted(r_uniques, key=lambda x: x['stars'], reverse=True)

    print '>>> Results for "%s" in %s <<<' % (query, language)
    print '>>> Next Result (n) / Open Link (o) / Load All (l) / Quit (q) <<<'
    print '-' * 60
    load_all = False
    for s in r_sorted:
        gitlink = "https://github.com%s" % s['url'][6:]
        print "%-20.20s | %4s stars | %s" % (s['name'], s['stars'], gitlink[8:])
        print "%s" % s['description']
        if load_all == False:
            try:
                choice = getch().lower()
            except KeyboardInterrupt:
                return
            if choice == 'q':
                print "\n%s FINISHED %s" % ("-" * 20, "-" * 20)
                return
            elif choice == 'o':
                try:
                    subprocess.call(['open', gitlink])
                except:
                    print ">>> Sorry! Couldn't open that! <<<"
                print "-" * 60
            elif choice == 'l':
                print "-" * 60
                load_all = True
            else:
                print "-" * 60
        else:
            print "-" * 60


def main():
    parser = OptionParser(usage="usage: %prog [options] [language] [query (no quotes, spaces okay)]", version="%prog 1.1.0")
    parser.add_option("-q", "--qry", dest="qry", help="search term to query")
    parser.add_option("-l", "--lang", dest="lang", default=DEFAULT_LANGAUGE, help="language to search for")
    (options, args) = parser.parse_args()

    if GITHUB_USERNAME == '' or GITHUB_PASSWORD == '':
        print "Please add your GitHub credentials to the script."
        return

    if options.qry:
        search_github(options.qry, options.lang)
    elif len(args) > 0:
        if args[0].lower() in LANGUAGES and len(args) > 1:
            search_github(' '.join(args[1:]), args[0].lower())
        else:
            search_github(' '.join(args), options.lang)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
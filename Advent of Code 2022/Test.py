import urllib2  # the lib that handles the url stuff

data = urllib2.urlopen(https://adventofcode.com/2021/day/1/input) # it's a file like object and works just like a file
for line in data: # files are iterable
    print line
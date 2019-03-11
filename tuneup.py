#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "jayaimzzz"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper(*args, **kwargs):
        print "before"
        c = cProfile.Profile()
        c.enable()
        result = func(*args, **kwargs)
        c.disable()
        p = pstats.Stats(c)
        p.sort_stats('cumulative').print_stats()
        return result
    return wrapper



def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    imports = '''from __main__ import find_duplicate_movies'''
    code = '''find_duplicate_movies("movies.txt")'''
    t = timeit.Timer(setup=imports, stmt=code)
    results = t.repeat(repeat=7,number=5)
    print "Best time across 7 repeats of 5 runs per repeat: {}".format(min(results) / 5)


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    # timeit_helper()

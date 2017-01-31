#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------

from queue import Queue

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# ------------
# collatz_eval
# ------------

cache = dict()
queue = Queue()
max = 0

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    return the value that produces the max cycle length of the range [1, n]
    """
    # <your code>
    num = 0
    max = 0
    for i in reversed(range(1, n + 1)):
        c = cycle_length(i)
        if (c > max):
            max = c
            num = i
    return num

def cycle_length (n) :
    c = 1
    while n > 1:
        if n & 1 == 0:
            n = (n >> 1)
        else:
            n = (n << 1) + n + 1
        c += 1
    assert c > 0
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)

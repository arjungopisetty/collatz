#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        r = StringIO("10\n")
        n = collatz_read(r)
        self.assertEqual(n, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        m = collatz_eval(10)
        self.assertEqual(m, 9)

    def test_eval_2(self):
        m = collatz_eval(15)
        self.assertEqual(m, 9)

    def test_eval_3(self):
        m = collatz_eval(20)
        self.assertEqual(m, 19)

    def test_eval_4(self):
        m = collatz_eval(100)
        self.assertEqual(m, 97)

    def test_eval_5(self):
        m = collatz_eval(1000)
        self.assertEqual(m, 871)

    def test_eval_6(self):
        m = collatz_eval(10000)
        self.assertEqual(m, 6171)

    def test_eval_7(self):
        m = collatz_eval(100000)
        self.assertEqual(m, 77031)

    def test_eval_8(self):
        m = collatz_eval(5000000)
        self.assertEqual(m, 3732423)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 10)
        self.assertEqual(w.getvalue(), "10\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("8\n10\n15\n20\n100\n1000\n10000\n100000\n5000000")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "9\n9\n19\n97\n871\n6171\n77031\n3732423\n")

# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

FizzBuzz Yo!

-------------------------------------------------------------------------------------------------------------------
How to execute scenario:

>>> python fizzbuzz.py

-------------------------------------------------------------------------------------------------------------------

:author: Nevio Vesic <nevio.vesic@gmail.com>
:licence: use it as much as male teenager wishes to use "the other head"
"""

# Defining some global variables that we'll need during resistance process
fizz_buzz, fizz, buzz = 'FizzBuzz', 'Fizz', 'Buzz'

# Resistance is futile!
print map(
    lambda n: (n % 3 == 0 and n % 5 == 0) and fizz_buzz or n % 3 == 0 and fizz or n % 5 == 0 and buzz or n,
    range(1, 101)
)
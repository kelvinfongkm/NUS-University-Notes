#!/usr/bin/env python3
from grade_luminus import IGNORE, Range, grade

# each question is a tuple
# first in tuple is number of marks
# second in tuple is correct answer
# provide a tuple () for MRQ marking, treating each entry as a separate true/false
# provide also a tuple () for multi-FITB marking
# in tuples, you can use IGNORE/ANY
# use IGNORE for None of the above
# use ANY for voided options
# provide a string/int/float for simple comparison marking
# provide a function taking (answer, question worth, all answers) for more complex marking
def questions():
  return [
    (1, 'True'),
    (1, 1),
    (1, (False, True, True, True, True, True, False, False)),
    (1, (False, False, False, False, IGNORE)),
    (1, (False, True, False, False, IGNORE)), #bonus
  ]

grade(questions)

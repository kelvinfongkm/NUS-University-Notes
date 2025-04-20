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
    # 1 to 6
    (1, (False, False, True, False, True)),
    (1, 4),
    (2, (False, True, False, True, False, IGNORE)),
    (2, (True, False, True, False, False)),
    (2, (False, True, False, False, False, IGNORE)),
    (1, (True, False, True, True, IGNORE)),
    # 7 to 9
    (2, 29),
    (2, 11),
    (2, 220),
    # 10 to 12
    (3, (6, Range(2.66, 2.67))),
    (3, (Range(5.33, 5.33), 2)),
    (3, (Range(6.66, 6.67), Range(0.66, 0.67)))
  ]

grade(questions)
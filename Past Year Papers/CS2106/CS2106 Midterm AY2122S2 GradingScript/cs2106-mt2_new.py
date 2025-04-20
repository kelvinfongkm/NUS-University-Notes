#!/usr/bin/env python3
from grade_luminus import IGNORE, Range, GraderFunction, grade, mark_simple

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
    # 1 to 5
    (1, 1000),
    (1, (False, True, False, False, True, IGNORE)),
    (2, (False, True, False, True, True)),
    (2, (True, False, True, False, True, IGNORE)),
    (2, (False, False, False, False, True, IGNORE)),
    # 6 to 9
    (3, GraderFunction(gradeQ6, 4), True),
    (1, GraderFunction(gradeQ7, 1)),
    (2, (20, 15, 9, 90)),
    (2, (15, 17, 11)),
    # 10 to 14
    (1, 15),
    (2, GraderFunction(grade_interleave(4, {-1}), 4)),
    (1, GraderFunction(grade_interleave(4, {-5, 0, 1}), 4)),
    (2, 70),
    (2, 2),
  ]

def gradeQ6(answer, worth, all_answers):
  correct = (mark_simple(answer[0], 0.33) +
    (mark_simple(answer[1], 21) or mark_simple(answer[1], 20)) +
    mark_simple(answer[2], 13 if answer[1] == '21' else 15) +
    mark_simple(answer[3], 9)
  )
  return correct * worth / 4

def gradeQ7(answer, worth, all_answers):
  total_time = all_answers[5][1] # Q6 2nd field, turnaround of A, which is also the total exec time
  if total_time == 21:
    return worth if mark_simple(answer, Range(85, 86)) else 0
  elif total_time == 20:
    return worth if mark_simple(answer, 90) else 0
  else:
    return 0

def grade_interleave(num_fields, correct):
  num_correct_blanks = num_fields - len(correct)
  def grader(answer, worth, all_answers):
    num_answer_correct = len(set(int(a.strip()) for a in answer if a != '-999' and a.strip() != '') & correct)
    num_answer_blank = sum(1 if a == '-999' or int(a.strip()) == -999 else 0 for a in answer if a.strip() != '')
    num_answer_correct_blank = min(num_answer_blank, num_correct_blanks)
    return (num_answer_correct + num_answer_correct_blank) * worth / num_fields
  return grader

assert grade_interleave(4, {-1})(['-999', '-1', '-999', '-999'], 2, None) == 2

grade(questions)
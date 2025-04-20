#!/usr/bin/env python3
import sys, csv
from datetime import datetime

BONUS_UNTIL = None
BONUS_MULT = None
questions = None

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# low <= answer <= high
class Range:
  def __init__(self, low, high):
    if type(low) != type(high):
      raise Error("Type of low != type of high")
    self.low = low
    self.high = high

class GraderFunction:
  def __init__(self, f, fields):
    self.f = f
    self.fields = fields

IGNORE = object() # use IGNORE for None of the above
ANY = object() # use ANY for voided options

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
DATETIME_FORMAT = "%d-%b-%Y %I:%M %p" # "10-Feb-2021 10:21 PM"

def mark_simple(ans, sol):
  if sol is ANY or ans == sol:
    return True
  if isinstance(sol, str):
    return str(ans).casefold() == sol.casefold()
  if isinstance(sol, int):
    try:
      return int(ans) == sol
    except:
      pass
    try:
      return int(float(ans)) == sol
    except:
      pass
  if isinstance(sol, float):
    try:
      return float(ans) == sol
    except:
      pass
  if isinstance(sol, Range):
    if isinstance(sol.low, int):
      try:
        return sol.low <= int(ans) <= sol.high
      except:
        pass
      try:
        return sol.low <= int(float(ans)) <= sol.high
      except:
        pass
    if isinstance(sol.low, float):
      try:
        return sol.low <= float(ans) <= sol.high
      except:
        pass
  return False


def grade_question(anss, sols, worth):
  if isinstance(sols, tuple):
    if not isinstance(anss, list):
      eprint("Expected list of responses to question")
      sys.exit(1)
    if len(anss) != len(sols):
      eprint("Length of response and answer is different")
      sys.exit(1)

    correct = 0
    is_mrq = False
    mrq_positive = 0
    for ans, sol in zip(anss, sols):
      if ans != '':
        mrq_positive += 1
      if sol is IGNORE:
        continue
      if isinstance(sol, bool):
        is_mrq = True
        ans = ans != ''
      if mark_simple(ans, sol):
        correct += 1
    # handle MRQ question being left blank
    if is_mrq and mrq_positive == 0:
      return 0
    return correct * worth / sum(map(lambda i: 1 if i is not IGNORE else 0, sols))

  return worth if mark_simple(anss, sols) else 0

def grade_row(row):
  index = 9
  mark = 0
  remark = ''
  anss = []
  for question in question_data:
    sols = question[1]
    if isinstance(sols, tuple) or (isinstance(sols, GraderFunction) and sols.fields > 1):
      fields = len(sols) if isinstance(sols, tuple) else sols.fields
      anss.append(row[index:index + fields])
      index += fields + 1
    else:
      anss.append(row[index])
      index += 2
    if len(question) >= 3 and question[2]:
      index += 1
  for ans, question, qno in zip(anss, question_data, range(1, 1 + len(question_data))):
    worth = question[0]
    sols = question[1]
    this_mark = sols.f(ans, worth, anss) if isinstance(sols, GraderFunction) else grade_question(ans, sols, worth)
    this_mark = int(this_mark) if isinstance(this_mark, int) or this_mark.is_integer() else this_mark
    mark += this_mark
    remark += 'Q{}[{}] '.format(qno, round(this_mark, 2))
  try:
    completed_at = datetime.strptime(row[6], DATETIME_FORMAT)
    if completed_at <= BONUS_UNTIL:
      mark *= BONUS_MULT
      remark += 'x{} bonus for submission before {}'.format(BONUS_MULT, BONUS_UNTIL)
  except:
    pass
  return (row[2], int(mark) if isinstance(mark, int) or mark.is_integer() else round(mark, 2), remark.strip())

def grade(p_questions, p_BONUS_MULT = 1, p_BONUS_UNTIL = datetime(2000, 1, 1, 0, 0, 0)):
  global questions, BONUS_MULT, BONUS_UNTIL
  questions = p_questions
  BONUS_MULT = p_BONUS_MULT
  BONUS_UNTIL = p_BONUS_UNTIL

  # each row (as exported from LumiNUS) is
  # [nusnet id, name, matric no, LumiNUS score, duration, time, time, status, comment
  #  q1 answer(s), q1 mark, q2 answer(s), q2 mark, ...]
  # for an MRQ each choice is a column that is blank if unselected and filled
  # with the answer if selected
  # for mcq/open ended it is simply the answer
  rows = list(csv.reader(sys.stdin))[2:]
  out = csv.writer(sys.stdout)
  global question_data
  question_data = questions()

  out.writerow(["STUDENT_NUMBER", "MARKS", "MODERATION", "REMARKS"])
  for row in rows:
    if row[7] == "Not Taken":
      continue
    studentno, marks, remarks = grade_row(row)
    out.writerow([studentno, marks, '', remarks])
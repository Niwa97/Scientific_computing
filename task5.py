import os
import datetime
import random

#1
def find_pdf_size(top):
  pdf_size = 0
  for root, dirs, files in os.walk(top):
    for name in files:
        if name.endswith(".pdf"):
          pdf_size = pdf_size + os.path.getsize(os.path.join(root,name))
  return pdf_size

print(find_pdf_size('.'))

#2
def print_working_days(date1, date2):
  if(len(date1)!= 10 or len(date2)!= 10):
    return 0
  first_date = datetime.date(int(date1[:4]),int(date1[5:7]),int(date1[8:10]))
  second_date = datetime.date(int(date2[:4]),int(date2[5:7]),int(date2[8:10]))
  if first_date > second_date:
    return 0
  else:
    num_of_days = second_date - first_date
    all_days = [first_date + datetime.timedelta(i) for i in range(num_of_days.days)]
    num_of_workdays = 0
    for day in all_days:
      if day.weekday() < 5:
        num_of_workdays += 1
    return num_of_workdays

print(print_working_days('2024-03-01','2024-03-28'))

#3
def random_walk(start):
  random.seed()
  start = start + random.randrange(-1, 2, 2)
  return start


init = 0
for i in range(100):
  print(init)
  init = random_walk(init)

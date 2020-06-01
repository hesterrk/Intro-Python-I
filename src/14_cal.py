"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


# THE DATE  --> this is the default too if no user input after file name
yy = datetime.today().year  # year
mm = datetime.today().month    # month


# Prints out the name of the script
# print(sys.argv, 'This is name of script')

# Prints out number of arguments in name of script
# print(len(sys.argv))

# The first argument  (index 1) is month
# The second argument (index 2) is year


# IF there is no user input then print out the calender(finding out length of script), if its just 1 which means nothing has been added to it by user

if len(sys.argv) == 1:
    print(calendar.month(yy, mm),
          'default to current month and year because no user input')

 # If the user specifies one argument (length of 2), assume they passed in a month and render the calender for that month of the current year
elif len(sys.argv) == 2:
  # converting to integer from string and assigning month to the second argument 
    mm = int(sys.argv[1])
    # print(mm, 'printing the month ')
    print(calendar.month(yy, mm))

# If both month and year have been passed in there will be a length of 3, assigning month and year accordingly to the indexes
elif len(sys.argv) == 3:
    mm = int(sys.argv[1])
    yy = int(sys.argv[2])
    print(calendar.month(yy, mm))


# Else if not correct formatting --> print 'the format that your program expects arguments to be given.'
else:
    print('Wrong format')


# RESULT OF PROGRAM -->
    # print(calendar.month(yy, mm))

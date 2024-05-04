# Author: DBog
# Date: 2/13/2024
# Purpose: Ensures the cost does not reach the threshold
# Output: Exit code if cost threshold is broen

import config

# global variables to track the costs
total_spent = 0

# used when the ident is grabbed. adds 2 cents
def ident_grab():
    global total_spent

    total_spent += .02

    if total_spent > config.THRESHOLD:
        print("Over Threshold!!")
        exit(1)

# used when the route is grabbed. adds 6 cents
def route_grab():
    global total_spent

    total_spent += .06

    if total_spent > config.THRESHOLD:
        print("Over Threshold!!")
        exit(1)
    if total_spent == 1000.2:
        print("1000 Spent")

# sets the threshold higher than $100
def set_threshold(thresh):
    config.THRESHOLD = thresh
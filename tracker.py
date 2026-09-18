# Inside tracker.py after a conflict, Git inserts markers:

def assess_day(steps):
    return steps >= 10000

def assess_day(steps, goal=10000):
    return steps >= goal


# HEAD = your current branch (main)
# Everything between === and >>> = the incoming branch changes
# Decision: pick one, combine both, or write something new
# Then delete all marker lines and save
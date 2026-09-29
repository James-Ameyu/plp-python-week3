# Grade Reporter & Bug Hunt

`grade_reporter.py` calculates grades, counts passed and failed learners, and calculates the average score.

`bug_hunt.py` fixes three bugs in a while loop that calculates the sum of numbers 1 to 5.

The hardest bug to find was the `while count < 5` condition because the program could run without showing an error message, but it produced the wrong answer. I knew something was wrong because the program was supposed to add 1, 2, 3, 4, and 5 and give an answer of 15, but the condition stopped the loop before 5 was added.

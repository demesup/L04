# Bug reports for exercise2.py

Line: 3

Problem: The condition "True if the grade is 5 or more" requires grade >= 5, but the function uses grade > 5, which excludes 5. This fails the specification for a grade of exactly 5.

Example: is_passing(5) should return True, but it returns False.

Fix: return grade >= 5

Line: 8

Problem: The docstring specifies "at least 8 characters", which means length >= 8, but the code uses len(password) > 8, which means length > 8. This incorrectly excludes passwords of exactly 8 characters.

Example: is_valid_password("abcdefgh") should return True (8 characters, no digit), but it returns False because len(password) > 8 is false.

Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12

Problem: The clamp function incorrectly uses min(x, low) which will always return low, making the function return max(low, low) = low regardless of x. It should be min(x, high) to cap at high, and max(x, low) to cap at low.

Example: clamp(10, 0, 5) should return 5, but due to the error, it returns 0.

Fix: return max(low, min(x, high))

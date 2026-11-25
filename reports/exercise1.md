# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if a number is odd (n % 2 == 1) instead of even (n % 2 == 0), which is a logic error in the function's intended behavior.
Example: is_even(4) should return True (since 4 is even), but currently returns False because 4 % 2 == 0, not 1.
Fix: return n % 2 == 0

Line: 8
Problem: The function calculates the sum of width and height instead of the area of a rectangle, which should be width multiplied by height.
Example: rectangle_area(5, 3) should return 15, but currently returns 8.
Fix: return width * height

Line: 13
Problem: The function adds 2 to the input instead of doubling it, which is a logic error in the function's intended behavior.
Example: double(5) should return 10, but currently returns 7.
Fix: return n * 2

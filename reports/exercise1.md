# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if n % 2 == 1, which is incorrect for even numbers. Even numbers have a remainder of 0 when divided by 2, so the function should check for n % 2 == 0 to return true for even numbers.

Example: is_even(4) should return True, but currently returns False because 4 % 2 == 0, not 1.

Fix: return n % 2 == 0

Line: 8
Problem: The function calculates the area of a rectangle as the sum of width and height, which is incorrect. The correct formula for area is width multiplied by height.

Example: rectangle_area(5, 3) should return 15, but currently returns 8.

Fix: return width * height

Line: 13
Problem: The function doubles a number by adding 2, which is incorrect. To double a number, it should be multiplied by 2.

Example: double(5) should return 10, but currently returns 7.

Fix: return n * 2

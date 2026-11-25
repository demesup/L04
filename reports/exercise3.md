# Bug reports for exercise3.py

Line: 3

Problem: The function assumes the list is non-empty, but the docstring states that an empty list has an average of 0. The current code will raise a ZeroDivisionError when the input list is empty because len(numbers) will be 0, leading to division by zero.

Example: average([]) → raises ZeroDivisionError

Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8

Problem: The docstring specifies that if the text is empty, the function should return an empty string. However, text.split() on an empty string returns an empty list, and accessing [0] on an empty list raises an IndexError.

Example: first_word("") → raises IndexError

Fix: return text.split()[0] if text.split() else ""

Line: 12

Problem: The docstring explicitly states that if total is 0, the result is 0. However, the current code divides by total, which will raise a ZeroDivisionError when total is 0.

Example: percent(5, 0) → raises ZeroDivisionError

Fix: return part / total * 100 if total != 0 else 0

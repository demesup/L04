# Bug reports for exercise3.py

Line: 3

Problem: The function averages a list but fails when the list is empty because `len(numbers)` would be 0, leading to division by zero. The docstring states that an empty list has an average of 0, but the current implementation raises a ZeroDivisionError.

Example: average([])

Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8

Problem: The function returns the first word of the text, but if the text is empty or contains only whitespace, `split()` returns an empty list, and accessing `[0]` will raise an IndexError. The docstring specifies that it should return an empty string if the text is empty.

Example: first_word("   ") or first_word("")

Fix: return text.split()[0] if text.strip() else ""

Line: 12

Problem: The function computes part as a percentage of total, but if total is 0, it will raise a ZeroDivisionError. The docstring specifies that if total is 0, the result is 0, but the current implementation does not handle this case.

Example: percent(5, 0)

Fix: return part / total * 100 if total != 0 else 0

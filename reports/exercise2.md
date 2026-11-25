# Bug reports for exercise2.py

Line: 2
Problem: The docstring states "True if the grade is 5 or more", which means the grade should be greater than or equal to 5. However, the function uses `grade > 5`, which excludes 5 itself. This is a boundary error where "or more" is incorrectly implemented with `>` instead of `>=`.

Example: input grade = 5 → expected output = True, actual output = False

Fix: return grade >= 5

Line: 8
Problem: The docstring requires "at least 8 characters and at least one digit", but the function only checks the length and uses `len(password) > 8`, which fails for passwords of exactly 8 characters. It also does not check for the presence of at least one digit.

Example: password = "abcdefgh" (8 chars, no digits) → expected output = False, actual output = False (correctly fails on length), but password = "abc12345" (9 chars, has digit) → correct, but password = "abcdefgh" (8 chars, no digit) → should fail, but function returns False (fails to check digit requirement)

Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The function is supposed to clamp x to the range [low, high], but the implementation uses `min(max(x, low), low)`, which effectively reduces x to low regardless of its value. This is a logical error — it should be `min(max(x, low), high)` to ensure x is bounded below by low and above by high.

Example: x = 10, low = 5, high = 15 → expected output = 10, actual output = 5

Fix: return min(max(x, low), high)

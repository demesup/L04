---
name: bug-finder
description: Analyzes a numbered source code file to identify all logic, boundary, edge-case, and security bugs, outputting a structured report for each issue.
---

# Bug Finder

## Input
You will receive one source code file with line numbers included.

## Instructions
1. Inspect **every single line and function** in the file from top to bottom. Do not stop after finding the first bug.
2. Check for **all bug categories**:
   - **Logic errors:** Wrong operators (`+` instead of `*`, `% 2 == 1` instead of `== 0`), wrong formulas, or wrong return values.
   - **Boundary / off-by-one errors:** Compare docstrings carefully against comparison operators (`>=` vs `>`, `<=` vs `<`, `min`/`max` bounds).
   - **Edge-case crashes:** Empty lists or empty strings (`ZeroDivisionError`, `IndexError`), zero denominators.
   - **Security vulnerabilities:**
     - **Hardcoded secrets:** Passwords or secrets written directly as literals instead of `os.environ.get(...)`.
     - **SQL injection:** User inputs interpolated into SQL queries via f-strings, `%`, `+`, or `.format()` instead of parameterized queries (`?`).
3. **No false positives:** Do not flag valid defensive checks (such as `ADMIN_PASSWORD != ""`).
4. **Strict formatting:** Output a separate bug report for each bug using the exact plain-text prefixes below (`Line:`, `Problem:`, `Example:`, `Fix:`). Always place a **blank line** between every single field (`Line:`, `Problem:`, `Example:`, `Fix:`) so each starts on its own line. Do not use bullet points, bold formatting, or introductory text.

## Output Format
Line: <number>

Problem: <what is wrong and why>

Example: <input that demonstrates the bug and its true expected output>

Fix: <the corrected line>

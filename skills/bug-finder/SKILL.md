---
name: bug-finder
description: Analyzes a numbered source code file to identify all bugs, including boundary and off-by-one errors, and outputs a structured report for each issue.
---

# Bug Finder

## Input
You will receive one source code file with line numbers included.

## Instructions
1. Inspect **every single function** in the file from top to bottom. Do not stop after finding the first bug.
2. Compare each function's docstring or comments against its implementation to verify that the code matches the exact specification.
3. Explicitly check for **off-by-one and boundary condition errors**:
   - Phrases like "at least", "or more", "minimum", or "no less than" require `>=` (not `>`).
   - Phrases like "at most", "or less", "maximum", or "no more than" require `<=` (not `<`).
4. Check for logical flaws, wrong variable names, edge-case failures, and runtime bugs.
5. For each bug found, output a separate bug report using the exact plain-text prefixes below (`Line:`, `Problem:`, `Example:`, `Fix:`). Do not use bullet points or bold formatting on these labels.
6. Put an empty line between each field so Markdown renders every item on a separate line.
7. Do not include any introductory or conversational text.

## Output Format
Line: <number>

Problem: <what is wrong and why>

Example: <input that shows it>

Fix: <the corrected line>

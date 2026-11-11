---
name: bug-finder
description: Analyzes a numbered source code file to identify bugs and outputs a structured report for each issue.
---

# Bug Finder

## Input
You will receive one source code file with line numbers included.

## Instructions
1. Carefully read through the provided code line by line.
2. Identify any syntax errors, logical flaws, edge-case failures, or runtime bugs.
3. For each bug found, output a separate bug report using the exact plain-text prefixes below (`Line:`, `Problem:`, `Example:`, `Fix:`). Do not use bullet points or bold formatting on these labels.
4. Put an empty line between each field so Markdown renders every item on a separate line.
5. Do not include any introductory or conversational text.

## Output Format
Line: <number>

Problem: <what is wrong and why>

Example: <input that shows it>

Fix: <the corrected line>

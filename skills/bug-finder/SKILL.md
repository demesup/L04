---
name: bug-finder
description: Analyzes a numbered source code file to identify all logic, boundary, edge-case, and security bugs across every function, outputting a structured report for each issue.
---

# Bug Finder

## Input
You will receive one source code file with line numbers included.

## Instructions
1. **Systematic Function Scan:** Inspect **every single function** from top to bottom. Do not skip any function.
2. **Multiple Bugs Per Function:** A single function can contain **more than one bug** (e.g., both a boundary error *and* a completely missing feature/requirement mentioned in the docstring). Check every single clause of the docstring against the code implementation.
3. **Explicit Checks:** 
   - **Boundaries:** Check if terms like "at least" or "or more" use `>=` or `<=`.
   - **Missing Requirements:** Verify that every rule stated in the docstring (such as checking for digits, special characters, or specific logic) is actually implemented in the return statement or body.
   - **Edge Cases & Security:** Check for empty inputs, zero divisions, and vulnerabilities.
4. **Report Every Bug:** Write a separate bug report block for *every* bug found across all functions, even if multiple bugs belong to the same function or line.
5. **Strict Formatting:** Output a separate bug report for each bug using the exact plain-text prefixes below (`Line:`, `Problem:`, `Example:`, `Fix:`). Always place a **blank line** between every single field. Do not use bullet points or bold formatting.

## Output Format
Line: <number>

Problem: <what is wrong and why>

Example: <input that demonstrates the bug and its true expected output>

Fix: <the corrected line>

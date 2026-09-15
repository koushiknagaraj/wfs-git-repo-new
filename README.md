# Python LeetCode Practice

A self-testing project to build LeetCode-ready Python skills. Each problem is a
stub in `problems/` with a docstring (statement + examples). You implement the
function/class, then run the matching test file in `tests/` — it behaves like
LeetCode's judge: pass all cases and you're done.

## Setup

```bash
pip install -r requirements.txt
```

## How to work through it

1. Open a file in `problems/`, read the docstring, implement the function
   (replace `raise NotImplementedError`).
2. Run its test file:
   ```bash
   pytest tests/test_two_sum.py -v
   ```
3. Run everything at once:
   ```bash
   pytest -v
   ```
4. Green tests = solved. Red = keep iterating (read the failure message, it
   tells you the input and what was expected).

## Problem set (grouped by concept)

| # | Problem | File | Concepts practiced |
|---|---------|------|---------------------|
| 1 | Two Sum | `problems/two_sum.py` | dicts, loops, functions |
| 2 | Valid Palindrome | `problems/valid_palindrome.py` | strings, datatypes, loops |
| 3 | Reverse Integer | `problems/reverse_integer.py` | loops, int math, edge cases |
| 4 | Contains Duplicate | `problems/contains_duplicate.py` | `enumerate`, sets |
| 5 | Single Number | `problems/single_number.py` | loops, functions |
| 6 | Majority Element | `problems/majority_element.py` | dicts, functions |
| 7 | Group Anagrams | `problems/group_anagrams.py` | `lambda`, sorting, dicts |
| 8 | Merge Intervals | `problems/merge_intervals.py` | `lambda` sort key, loops |
| 9 | Valid Parentheses | `problems/valid_parentheses.py` | lists as stacks, loops |
| 10 | Min Stack | `problems/min_stack.py` | classes, OOP |
| 11 | Merge Two Sorted Lists | `problems/merge_two_sorted_lists.py` | classes (`ListNode`), functions |
| 12 | Implement Queue using Stacks | `problems/queue_using_stacks.py` | classes, OOP |

Work top to bottom, or jump to whatever concept you want to drill. Each test
file has 5-8 cases including edge cases (empty input, single element, etc.),
similar to what LeetCode itself checks.

## Tips

- Don't look at test internals to "reverse-engineer" the answer — try to solve
  from the docstring first, use tests only to verify.
- If stuck, re-read the constraints in the docstring; they often hint at the
  expected time complexity.
- `pytest -v -k two_sum` runs only tests matching a keyword.

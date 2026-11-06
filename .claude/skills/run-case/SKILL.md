---
name: run-case
description: Build the input for a LeetCode-style test case, run it against the algorithm in the user's solution file, and print only the result. Use when the user sends a test case (e.g. "[1,2] targetSum = 1") or invokes /run-case.
argument-hint: "<test case> [expected=<value>] [file=<path>]"
---

# run-case

The user sends a test case. Build that input, run it through the algorithm already in their file, and show the output. Nothing more.

## Hard rules

- **No commentary.** Don't explain why the result is right or wrong. Don't point out bugs, hint at fixes, or suggest improvements. The user asks follow-up questions when they want them.
- **Never touch the algorithm.** Don't edit the `Solution` class, the `sol` function, or whatever the user wrote. Only add input-building, printing and test-case code.
- The final reply is only the program's stdout, in a code block. If running the file fails, show the traceback the same way and say nothing else.

## Steps

1. **Pick the target file**, in this order:
   - `file=<path>` in the arguments,
   - the file the user has open in the IDE,
   - otherwise the most recently modified `.py` file under the repo (`ls -t`).
2. **Read the file.** Find the entry point: a `Solution` method (LeetCode style) or a top-level function such as `sol(...)`. Note its parameters and types (`TreeNode`, `ListNode`, list, int, str, ...).
3. **Map the test case onto the parameters.** LeetCode format: `[1,2]` with `targetSum = 1` means `root=[1,2], targetSum=1`. Use `null`/`None` for missing tree nodes.
4. **Make sure the helpers exist.** If they're already in the file, reuse them. Otherwise add only the ones this case needs, below the algorithm and above any calls:
   - `TreeNode` input → a `TreeNode` class (if missing), `build_tree(values)` (level-order list to tree), `print_tree(node)` (sideways, `L`/`R` labels).
   - `ListNode` input → a `ListNode` class (if missing), `build_list(values)`, `list_to_array(head)`.
   - A `run_case(...)` helper that builds the inputs, calls the algorithm, and prints:
     ```
     <param>=<value> <param>=<value>
     <tree/list printout, if structured input>
       got=<result> expected=<expected> -> PASS|FAIL
     ```
     If the user gave no expected value, print `  got=<result>` and leave out the expected part and PASS/FAIL.
     If the result is a `TreeNode`/`ListNode`, convert it back to a list before printing.
   - Keep the helpers typed and short (functions of 4–20 lines), with one-line docstrings.
   - Match how the file already does things: if it only calls `print(sol(...))` at the bottom, just add another `print(sol(...))` line.
   - If `Optional` or other typing imports are needed and missing, add them at the top.
5. **Add the case.** Append a `run_case(...)` call (or `print(...)` call) at the bottom. Keep the user's existing calls.
6. **Run it** from the file's directory: `python3 <file>`. It prints every case in the file, which is fine.
7. **Reply** with only the stdout (or traceback) in a code block.

## Example

Input: `[1,2] targetSum = 1 expected=false` for `leetcode/path-sum.py`

Appended line:

```python
run_case([1, 2], 1, False)
```

Reply:

````
```
root=[1, 2] targetSum=1
root: 1
    L: 2
  got=<result> expected=False -> PASS|FAIL
```
````

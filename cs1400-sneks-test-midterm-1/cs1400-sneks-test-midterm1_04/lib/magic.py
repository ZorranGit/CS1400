X={0: ["The string method `.startswith(pattern)` consumes a pattern (a string) and\nreturns a boolean indicating whether that pattern appears at the start of the\noriginal string", "The string method `.endswith(pattern)` consumes a pattern (a string) and\nreturns a boolean indicating whether that pattern appears at the end of the\noriginal string", "parentheses", "(", ")"], 1: ["The string method `.endswith(pattern)` consumes a pattern (a string) and\nreturns a boolean indicating whether that pattern appears at the end of the\noriginal string", "The string method `.startswith(pattern)` consumes a pattern (a string) and\nreturns a boolean indicating whether that pattern appears at the start of the\noriginal string", "square brackets", "[", "]"]}
def asdf(x,y):
    IT = """# Midterm 1) Question 4

To begin, make sure your name and D# are still in the proper assignment
statements found in `login.py` and then run the program `question4.py` (in
Thonny, click run while viewing the `question4.py` file). Your custom
instructions will appear below (if you are in Thonny, you will need to click
"Show instructions" again from the Codegrinder menu).

============================================================

{}.

{}.

Use these methods to implement a new function named `is_surrounded` that
consumes a sentence (a string) and returns a boolean indicating whether the
sentence has {} on both sides. In other words, the string begins
with `"{}"` and ends with `"{}"`.

You encouraged, but not required, to unit test your function.
""".format(*y(x))
    with open('doc/doc.md','w') as f:
        f.write(IT)
    IT = """<html><head></head><body><h1>Midterm 1) Question 4</h1>

<p>To begin, make sure your name and D# are still in the proper assignment
statements found in <code>login.py</code> and then run the program <code>question4.py</code> (in
Thonny, click run while viewing the <code>question4.py</code> file). Your custom
instructions will appear below (if you are in Thonny, you will need to click
"Show instructions" again from the Codegrinder menu).</p>

<p>============================================================</p>

<p>{}.</p>

<p>{}.</p>

<p>Use these methods to implement a new function named <code>is_surrounded</code> that
consumes a sentence (a string) and returns a boolean indicating whether the
sentence has {} on both sides. In other words, the string begins
with <code>"{}"</code> and ends with <code>"{}"</code>.</p>

<p>You encouraged, but not required, to unit test your function.</p>

</body></html>
""".format(*y(x))
    with open('doc/index.html','w') as f:
        f.write(IT)

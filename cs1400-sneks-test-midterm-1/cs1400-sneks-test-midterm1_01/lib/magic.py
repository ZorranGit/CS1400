X={0:[17,5,False,"Software"],1:[15,3,True,"Python"],2:[12,9,False,"Algorithm"],3:[6,15,True,"Expression"]}
def asdf(x,y):
    IT = """# Midterm 1) Question 1

To begin, make sure your name and D# are still in the proper assignment
statements found in `login.py` and then run the program `question1.py` (in
Thonny, click run while viewing the `question1.py` file). Your custom
instructions will appear below (if you are in Thonny, you will need to click
"Show instructions" again from the Codegrinder menu).

============================================================

In the file `question1.py`, print the following literal values (each on their
own line):

* The integer `{}`
* The float `{}`
* The boolean `{}`
* The string `"{}"`
* The special value `None`
""".format(*y(x))
    with open('doc/doc.md','w') as f:
        f.write(IT)
    IT = """<html><head></head><body><h1>Midterm 1) Question 1</h1>

<p>To begin, make sure your name and D# are still in the proper assignment
statements found in <code>login.py</code> and then run the program <code>question1.py</code> (in
Thonny, click run while viewing the <code>question1.py</code> file). Your custom
instructions will appear below (if you are in Thonny, you will need to click
"Show instructions" again from the Codegrinder menu).</p>

<p>============================================================</p>

<p>In the file <code>question1.py</code>, print the following literal values (each on their own line):</p>
<ul>
<li>The integer <code>{}</code></li>
<li>The float <code>{}</code></li>
<li>The boolean <code>{}</code></li>
<li>The string <code>"{}"</code></li>
<li>The special value <code>None</code></li>
</ul>
</body></html>
""".format(*y(x))
    with open('doc/index.html','w') as f:
        f.write(IT)

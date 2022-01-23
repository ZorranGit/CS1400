X={0: ["you are picking Spring courses to take", "check_courses", "the number of courses you want to take", "the maximum number of credits you are " "allowed to take", "whether you can take those courses", "multiplying the number of courses by 3 (as in the number of credits per " "course)\nand checking if the result is less than the maximum number of " "credits"], 1: ["you are responding to emails", "check_emails", "the number of emails you need to respond to", "the amount of time you have to answer emails (in minutes)", "whether you have enough time to answer all of the emails", "multiplying the number of emails by 10 (as in the number of minutes per " "email)\nand testing if the result is less than the amount of time you have"]}
def asdf(x,y):
    IT = """# Midterm 1) Question 2

To begin, make sure your name and D# are still in the proper assignment
statements found in `login.py` and then run the program `question2.py` (in
Thonny, click run while viewing the `question2.py` file). Your custom
instructions will appear below (if you are in Thonny, you will need to click
"Show instructions" again from the Codegrinder menu).

============================================================

For this problem, imagine {}. Create a function named
`{}` that consumes an integer that represents
{} and another integer that represents
{}. The function should
return a boolean that represents
{}.
Your function will determine this by
{}.

You are not required to unit test your function, but it is encouraged.
""".format(*y(x))
    with open('doc/doc.md','w') as f:
        f.write(IT)
    IT = """<html><head></head><body><h1>Midterm 1) Question 2</h1>

<p>To begin, make sure your name and D# are still in the proper assignment
statements found in <code>login.py</code> and then run the program <code>question2.py</code> (in
Thonny, click run while viewing the <code>question2.py</code> file). Your custom
instructions will appear below (if you are in Thonny, you will need to click
"Show instructions" again from the Codegrinder menu).</p>

<p>============================================================</p>

<p>For this problem, imagine {}. Create a function named
<code>{}</code> that consumes an integer that represents
{} and another integer that represents
{}. The function should
return a boolean that represents
{}.
Your function will determine this by
{}.</p>

<p>You are not required to unit test your function, but it is encouraged.</p>

</body></html>
""".format(*y(x))
    with open('doc/index.html','w') as f:
        f.write(IT)

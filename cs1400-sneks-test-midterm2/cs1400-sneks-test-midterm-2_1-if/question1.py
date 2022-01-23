def student_status(credits):
    if credits < 30:
        return "Freshman"
    elif credits >= 30 and credits <= 59:
        return "Sophomore"
    elif credits >= 60 and credits <= 89:
        return "Junior"
    else:
        return "Senior"

print(student_status(29))

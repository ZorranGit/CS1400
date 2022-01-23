def choose(listboi):
    choices=listboi
    print("You can:")
    for i in listboi:
        print(i)
    answer=input("What will you do?")
    while answer not in choices:
        answer=input("What will you do?")
    return answer
choose(['quit', 'nap', 'fight'])

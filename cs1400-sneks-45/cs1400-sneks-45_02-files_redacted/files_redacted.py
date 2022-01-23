secret=open("messages.txt")
for i in secret:
    i=i.replace("James Bond","[Redacted]")
    i=i=i.strip("\n")
    print(i)

secret.close()

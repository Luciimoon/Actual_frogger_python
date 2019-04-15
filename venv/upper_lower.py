data = input(str("What is the word"))
para = input(str("what is the parameter"))
para = bool(para)
if para is True:
    print(data.upper())
    if para is False:
        print(data.lower())
    else:
        print("complete")
else:
    print("complete")








s = 'smith, bob;jones, bill;doe, john'
for lname, fname, in [q.split(",") for q in s.split(";")]:
    # The split fuction defins fname and fname into a varible by slipting the data.
    print(fname, lname)
    # print the varibles fname lname 
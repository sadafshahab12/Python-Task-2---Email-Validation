email = input("Enter Your Email: ");  #g@g.in
k=0
j=0
d=0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):  #^ exor operator dono m se koi ek true hojae or dono true hoga to ye false krdega  
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d=1 
                if k == 1 or j==1 or d==1:
                    print("wrong email condition 5")
            else:
                print("Wrong email condition 4")

        else:
            print("wrong email condition 3")

    else:
        print("Wrong email condition 2")
else:
    print("Wrong email condition 1")
gmail = input("Enter you email: ")
k,j,p = 0,0,0
if len(gmail)>=6:
    if(gmail[0]).isalpha():
        if("@"in gmail) and (gmail.count("@")==1):
            if(gmail[-4]==".") ^ (gmail[-3]=="."):
                for i in gmail:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        p=1
                if k == 1 or j == 1 or p == 1:
                    print("Invalid email address")
                else:
                    print("Right email address")
            else:
                print("Invalid email address")
        else:
            print("Invalid email address") 
    else:
        print("Invalid email address")
else:
    print("Invalid email address")
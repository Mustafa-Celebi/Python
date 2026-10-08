
print("WELCOME TO YOUR PERSONAL SPACE.")
pwd = "myDiary."
txt = []
pwd_in = input("PLEASE ENTER YOUR PASSWORD: ")

def menu():
        print("MENU /n")
        print("PLEASE SELECT AN OPERATION.")
        print("[A] OPEN TODAY'S TEXTBOOK")
        print("[B] VIEW OLD TEXTBOOKS")
        print("[C] EDIT PASSWORD")
        print("[D] QUIT")

        def c():
            c = input("Do you want to continue?(y/n): ").lower()
            if c == "y":
                menu()
            else:
                print("HAVE A GOOD DAY!")
                    
        
        
        op = input().upper()
        
        
        if op == "A":
            txt_add = input()
            txt.append(txt_add)
            c()   
        
        elif op == "B":
            print(txt)
            c()
    
        elif op == "C":
            pwd = input("PLEASE ENTER YOUR NEW PASSWORD: ")
            print("YOUR NEW PASSWORD IS", pwd)
            c()
    
        elif op == "D":
            print("HAVE A GOOD DAY!")


while not pwd == pwd_in:
    print("WRONG PASSWORD. TRY AGAIN.")
    pwd_in = input("PLEASE ENTER YOUR PASSWORD: ")
    
if pwd == pwd_in:
    menu()
            
        
from datetime import date

print("WELCOME TO YOUR PERSONAL SPACE.")
pwd = "myDiary."
dt = str(date.today())
file_name = "C:\\Users\\lenovo\\Desktop\\Python\\Practice\\Diary\\Diary_Notes\\" + dt + ".txt"
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
            new_text = input()
            with open(file_name, "a") as file_variable:
                file_variable.write(new_text + "\n")
            c()   
        
        elif op == "B":
            try:
                dt_inp = input("Enter the date you want to read(YYYY-MM-DD): ")
                file_read = "C:\\Users\\lenovo\\Desktop\\Python\\Practice\\Diary\\Diary_Notes\\" + dt_inp + ".txt"
                with open(file_read, "r") as read_info:
                    read = read_info.read()
                    print(read)

                c()

            except FileNotFoundError:
                print("File could not find.")
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
            
        
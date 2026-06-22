# Password Vault (گاوصندوق رمزها)
vault=[]
while True:
    Menu=int(input("==== Password Vault ==== \n 1. Add Password \n 2. Show Saved Passwords \n 3. Search Password \n 4. Exit Enter your choice (1-4):"))
    match Menu:
        case 1:
            web=input("Website:")
            Pass=input("Password:")
            entry1={
                "website" : web,
                "pass" : Pass
            }
            vault.append(entry1)
        case 2:
            if len(vault)==0:
                print("no expenses recorded.")
            else:
                for i in range(len(vault)):
                    print(f"{vault[i]["website"]} - {vault[i]["pass"]} ")
        case 3:
            search=input("Search website:")
            found=False
            for i in range(len(vault)):
                if vault[i]["website"] == search :
                    print(f"{vault[i]["website"]} - {vault[i]["pass"]} ")
                    found=True
                else:
                    print("Not found")
            found=False
        case 4:
            print("Bye ")
            break
        case _:
            print("Enter Number 1-4")
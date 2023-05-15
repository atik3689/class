import sql1 
import smtplib
import random
import registration
import login

class Index(registration.Registr,login.Login):
    def __init__(self):
        while True:
            print("\n1.Registration \n2.Login \n3.Exit")
            x=int(input("Chose any one option:"))

            if x==1:
                self.registr()
                #break

            elif x==2:
                self.userlogin()
                break
            
            elif x==3:
                exit()
            
            else:
                print("Invalid Number....!")

#obj=Index()

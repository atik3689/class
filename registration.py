import smtplib
import random
import sql1 
import login

class Registr(login.Login):
    def registr(self):
        while True:   
            self.fname=input("Enter first Name:")
            self.a= self.fname.isalpha()
            if self.a==True:
                print("")
                break
            else:
                print("Only Characters are Allowed...!")
#last Name:
        while True:
            self.name1=input("Enter Last Name:")
            self.b= self.name1.isalpha()
            if self.b==True:
                print("")
                break
            else:
                print("Only Characters are Allowed...!")
#Email:
        while True:
            self.mail=input("Enter Email Id:")
            self.mail.endswith("@gmail.com")
            if (self.mail.endswith("@gmail.com")==True):
                print(" ")
                break
            else:
                print("Invalid Email...!")
#Phona Number:
        while True:
            try:
                self.contact=(input("Enter Mobile Number:"))
                self.x=len(self.contact)
                if self.x==10:
                    print("")
                    break
                else:
                    print("Contact Digit Should be 10...")
            except:
                print("Invalid Number...!")   
#Address:
        self.add=input("Enter Address:")

#Gender:
        while True:
            print("1.Male \n2.Female \n3.other")
            self.gender=int(input("Chose Gendar:"))
            if self.gender==1:
                self.gender1="Male"
                print("You Choose Male.")
                break
            elif self.gender==2:
                self.gender1="FeMale"
                print("You Chose Female..")
                break
            elif self.gender==3:
                self.gender1="Other"
                print("You Chose Other...")  
                break
            else:
                print("Wrong Option...!") 
                break
    
        self.email()
        self.chek_otp()

#Subbmit registration Data:
    def Regster_data(self):
        while True:
            print("Do You Want To Submit:")
            print("1.Yes 2.No")
            self.sub=int(input("Chose One:"))
            if self.sub==1:
                
                sql = "insert into registration(fname,name1,mail,contact,gendr,address) values(%s,%s,%s,%s,%s,%s)"
                val = (self.fname,self.name1,self.mail,self.contact,self.gender1,self.add)

                try:
                    sql1.mycur.execute(sql,val)
                    sql1.mydb.commit()
                    print("Data Inserted...")
                    self.login_data(self.user_name,self.password)
                    break
                    
                except:
                    print("Duplicate Id...!")
                    break
            
            elif self.sub==2:
                print("Your Data Not Submitted...!")
                break
            else:
                print("Invalid Number...!")

        
#Email OTP 
    def email(self):
    # random Password :  
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        self.password = ""
        for i in range(4):
            self.password += random.choice(characters)   
            
        s=smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()
        s.login('atiktamboli89@gmail.com','eyxxbadfxxjlihxn')
        self.otp =str(random.randrange(1000,9999))
        
        self.user_name=self.fname[0:2]+self.name1[0:2]
        all="Username is= "+ self.user_name +"\n Password is =" + self.password + "\n Otp is=" + self.otp  
        s.sendmail('atiktamboli89@gmail.com','atiktamboli89@gmail.com',all)

        s.quit()

#check addmin Otp: 
    def chek_otp(self):
        while True:
            self.user_otp=input("Enter otp:")
            if self.user_otp==self.otp:
                print("Otp Verify...")
                
                self.Regster_data()
                break
           
            else:
                print("Invalid Otp....!")


'''
obj =Registr()
obj.registr()
obj.email()
obj.chek_otp()'''

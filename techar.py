import sql1

class Techar:
    def techar_Registration(self):

#Student Name:
        while True:
                self.name=input("Enter Techar Name:")
                self.a= self.name.isalpha()
                if self.a==True:
                    print("")
                    break
                else:
                    print("Only Characters are Allowed...!")
        
#Student Email:
        while True:
                self.Email=input("Enter Techar Email Id:")
                self.Email.endswith("@gmail.com")
                if (self.Email.endswith("@gmail.com")==True):
                    print(" ")
                    break
                else:
                    print("Invalid Email...!")
#Student Phone Number:
        while True: 
            self.number=(input("Enter Techar Mobile Number:"))
            self.x=len(self.number)
            if self.x==10:
                print("")
                break
            else:
                print("Contact Digit Should be 10...")
#Student course:
        while True:    
            self.course=input("Enter Techar Subject:")
            self.c= self.course.isalpha()
            if self.c==True:
                print("")
                break
            else:
                print("Only Characters are Allowed...!")
#Student Fees:
        while True:
            self.salary=int(input("Enter Techar Salary:"))
            break
        ''' if self.fees==True:
                #print("")
                break
            else:
                print("Only Number Allowed...")'''
        try:
            self.techar_data()
             
        except:
            print("Error While Inserting techar Data...")     

#Data Insert in table:
    def techar_data(self):
        while True:
            print("Do You Want To Submit:")
            print("1.Yes 2.No")
            self.submit=int(input("Chose One:"))
            if self.submit==1:
       
                sql = "insert into techar(name,Email,number,course,fees) values(%s,%s,%s,%s,%s)"
                val = (self.name,self.Email,self.number,self.course,self.salary)
           
                try:
                    sql1.mycur.execute(sql,val)
                    sql1.mydb.commit()
                    print("techar Data Inserted...")
                    break
        
                except:
                    print("Duplicate Id...!")
                    break

            elif self.submit==2:
                print("Your Data Not Submitted...!")
                break
            else:
                print("Invalid Number...!")

#Techar Data Showing:
    def fetch_techar_Data(self):
        r_query = "select * from techar"
        sql1.mycur1.execute(r_query)
        result1 = sql1.mycur1.fetchall()
        #print(result1)
        for y in result1:
           # (r_id,r_fname,r_name1,r_mail,r_contact,r_gender,r_address)= y
            print(y)



'''obj=Techar()
obj.techar_Registration()
obj.fetch_techar_Data()'''
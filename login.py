import smtplib
import random
import sql1 
import student
import techar
import cors
import payfees
import student_date_updata
import techar_date_updata


class Login(techar.Techar,cors.Cors,payfees.Payfees,student_date_updata.Updata_student_date,techar_date_updata.Updata_techar_date):
    def userlogin(self):
            self.uname_user=(input("Enter User Name:"))
            self.password_user=(input("Enter Password:"))
            

            # selecting query
            query = "SELECT * from login where username=%s and password=%s"
            sql1.mycur.execute(query,(self.uname_user,self.password_user))
            
            myresult = sql1.mycur.fetchall()
            print(myresult)
            for x in myresult:
                (self.id,self.username_table,self.password_table)= x
                print(self.id)
              
                if self.uname_user == self.username_table and self.password_user == self.password_table:
                    self.login_id_to_register_mail(self.id)

                else:
                    print("Usernama or Password incorrect")
                    

#login details 
    def login_id_to_register_mail(self,id):
        r_query = "select * from registration where id=%s"
        sql1.mycur1.execute(r_query,(id,))
        result1 = sql1.mycur1.fetchall()
        print(result1)
        for y in result1:
            (r_id,r_fname,r_name1,r_mail,r_contact,r_gender,r_address)= y
            print(r_mail)
            
            s=smtplib.SMTP('smtp.gmail.com',587)

            s.starttls()
            s.login('atiktamboli89@gmail.com','eyxxbadfxxjlihxn')
            self.otp1 =str(random.randrange(1000,9999))
             
            s.sendmail('atiktamboli89@gmail.com',r_mail,self.otp1)
            

            s.quit()
            self.login_otp_Verify(self.otp1)  
        
        
        
#Inserting data in login table:          
    def login_data(self,uname_user,password_user):
        sql = "Insert into login(username,password) values(%s,%s)"
        val = (uname_user,password_user)
        try:
                sql1.mycur.execute(sql,val)
                sql1.mydb.commit()
                print("Login Data Inserted...")
                #self.userlogin()
                                    
        except:
                print("Something While Wrong...!")

#Student Data and Otp:

    def login_otp_Verify(self,otp):
            self.user_otp=input("Enter otp:")
            if self.user_otp==otp:
                print("Otp Verify...")
            
            while True:
                Studentinfo=int(input("\n1.Student Details \n2.Student Registration \n3.Student Data Updata \n4.Teacher Details \n5.Teacher Registration \n6.Teacher Data Updata \n7.Course Details  \n8.Pay Fees \n9.Exit \n\nChoose any one option:"))
                if Studentinfo==1:
                    print("Student Detalis")
                    self.fetch_Student_Data()
                    
                    
                elif Studentinfo==2:
                    print("Student Registration")
                    self.student_Registration()

                elif Studentinfo==3:
                    print("Student Data Updata")
                    self.updata_date()
                 
                    
                elif Studentinfo==4:
                    print("Teacher Details")
                    self.fetch_techar_Data()
                    
                    
                elif Studentinfo==5:
                    print("Teacher Registration")
                    self.techar_Registration()

                elif Studentinfo==6:
                    print("Teacher Data Updata")
                    self.techar_data_update()
                   
                elif Studentinfo==7:
                    print("Course Details")
                    self.fetch_cors_Data()
                   
                   
                elif Studentinfo==8:
                    print("Pay Fees")
                    self.pay_fees()

                elif Studentinfo==9:
                    exit()
                    
                else:
                    print("Invalid Number....!")
                    
            else:
                print("Otp Invalide...!")
              


#obj=Login()
#obj.userlogin()            
            
          


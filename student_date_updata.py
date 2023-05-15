import sql1
import student


class Updata_student_date(student.Student):
    def updata_date(self):
        while True:
                self.Email=input("Enter Email Id:")
                #self.Email.endswith("@gmail.com")
                #if (self.Email.endswith("@gmail.com")==True):
                r_query = "select * from student where Email=%s"
                sql1.mycur1.execute(r_query,(self.Email,))
                result1 = sql1.mycur1.fetchall()
                print(result1)
                for y in result1:
                    (self.r_id,self.r_name,self.r_Email,self.r_number,self.r_course,self.r_total_fees,self.r_Balance_fees,self.r_Paid_fees)= y
                break
                
        self.updata()
    
    def updata(self):
        while True:
                self.updata=int(input("\n1.Updata Name \n2.Updata Email \n3.Updata Number \n4.Updata Cors \n5.Exit \n\nChoose any one option:"))
                if self.updata==1:
                    self.a=input("Enter Updata Name:")

                    sql= "update student set name=%s where Email=%s" 
                    val=(self.a,self.Email)
                    
                    sql1.mycur2.execute(sql,val)
                    sql1.mydb.commit()
                
                
                elif self.updata==2:
                    self.b=input("Enter Updata Email:")

                    sql= "update student set Email=%s where Email=%s" 
                    val=(self.b,self.Email)
                    
                    sql1.mycur2.execute(sql,val)
                    sql1.mydb.commit()
                    

                elif self.updata==3:
                    self.c=input("Enter Updata Number:")

                    sql= "update student set mobile=%s where Email=%s" 
                    val=(self.c,self.Email)
                    try: 
                        sql1.mycur2.execute(sql,val)
                        sql1.mydb.commit()
                    except:
                            print("Mobile Update issue")

                    
                
                elif self.updata==4:
                    self.d=input("Enter Updata Your Cors:")

                    sql= "update student set course=%s where Email=%s" 
                    val=(self.d,self.Email)
                    
                    sql1.mycur2.execute(sql,val)
                    sql1.mydb.commit()
                    
                
                elif self.updata==5:
                    exit()
                
                else:
                    print("Plz Check Number.....")
                    break




obj=Updata_student_date()
obj.updata_date()
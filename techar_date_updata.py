import sql1
import student


class Updata_techar_date(student.Student):
    def techar_data_update(self):
        while True:
                self.Email=input("Enter Email Id:")
                #self.Email.endswith("@gmail.com")
                #if (self.Email.endswith("@gmail.com")==True):
                query = "select * from  techar where Email=%s"
                sql1.mycur1.execute(query,(self.Email,))
                result1 = sql1.mycur1.fetchall()
                print(result1)
                for y in result1:
                    (self.id,self.name,self.Email,self.number,self.course,self.total_fees)= y
                break
        
        self.updata()

    
    def updata(self):           
        while True:
            self.updata=int(input("\n1.Updata Name \n2.Updata Email \n3.Updata Number \n4.Updata Cors \n5.Exit \n\nChoose any one option:"))
            if self.updata==1:
                self.a=input("Enter Updata Name:")

                sql= "update  techar set name=%s where Email=%s" 
                val=(self.a,self.Email)
                
                sql1.mycur2.execute(sql,val)
                sql1.mydb.commit()
                
            
            elif self.updata==2:
                self.b=input("Enter Updata Email:")

                sql= "update  techar set Email=%s where Email=%s" 
                val=(self.b,self.Email)
                
                sql1.mycur2.execute(sql,val)
                sql1.mydb.commit()
                

            elif self.updata==3:
                self.c=input("Enter Updata Number:")

                sql= "update techar set number=%s where Email=%s" 
                val=(self.c,self.Email)
                
                sql1.mycur2.execute(sql,val)
                sql1.mydb.commit()
                
            
            elif self.updata==4:
                self.d=input("Enter Updata Your Cors:")

                sql= "update  techar set course=%s where Email=%s" 
                val=(self.d,self.Email)
                
                sql1.mycur2.execute(sql,val)
                sql1.mydb.commit()
                
            
            elif self.updata==5:
                exit()
                
            
            else:
                print("Plz Check Number.....")
                


'''
obj=Updata_techar_data()
obj.techar_data_updata()'''
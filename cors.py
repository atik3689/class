import sql1

class Cors:
#Corse Information:
    def cors(self):
        self.corsname=input("Enter Corsname:")
        self.corsduration=input("Enter cors Duration:")
        self.corsfees=input("Enter cors Fees:")
          
        try:
            self.cors_data()
             
        except:
            print("Error While Inserting techar Data...")  

#Data Insert in table:
    def cors_data(self):
        while True:
            print("Do You Want To Submit:")
            print("1.Yes 2.No")
            self.submit=int(input("Chose One:"))
            if self.submit==1:
       
                sql = "insert into cors(corsname,corsduration,corsfees) values(%s,%s,%s)"
                val = (self.corsname,self.corsduration,self.corsfees)
           
                try:
                    sql1.mycur.execute(sql,val)
                    sql1.mydb.commit()
                    print("cors Data Inserted...")
                    break
        
                except:
                    print("Duplicate Id...!")
                    break

            elif self.submit==2:
                print("Your Data Not Submitted...!")
                break
            else:
                print("Invalid Number...!")

#Cors Data Showing:
    def fetch_cors_Data(self):
        r_query = "select * from cors"
        sql1.mycur1.execute(r_query)
        result1 = sql1.mycur1.fetchall()
        #print(result1)
        for y in result1:
           # (r_id,r_fname,r_name1,r_mail,r_contact,r_gender,r_address)= y
            print(y)
        
#obj=Cors()     
#obj.cors_data()
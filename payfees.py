import sql1
import student

from fpdf import FPDF

class Payfees(student.Student):
    def pay_fees(self):
        while True:
                self.Email=input("Enter Email Id:")
                self.Email.endswith("@gmail.com")
                #if (self.Email.endswith("@gmail.com")==True):
                r_query = "select * from student where Email=%s"
                sql1.mycur1.execute(r_query,(self.Email,))
                result1 = sql1.mycur1.fetchall()
                print(result1)
                for y in result1:
                    (self.r_id,self.r_name,self.r_Email,self.r_number,self.r_course,self.r_total_fees,self.r_Balance_fees,self.r_Paid_fees)= y
                    print(self.r_total_fees,self.r_Balance_fees,self.r_Paid_fees)
                    
                
                self.fees=int(input("Enter Fees:"))
                if (self.fees<=self.r_total_fees): 
                    self.r_Paid_fees = self.r_Paid_fees + self.fees
                    self.r_Balance_fees = self.r_total_fees - self.r_Paid_fees
                    print(self.r_total_fees, self.r_Balance_fees, self.r_Paid_fees)
                    
                    sql="update student set Paid_fees=%s,Balance_fees=%s where Email=%s" 
                    val=(self.r_Paid_fees,self.r_Balance_fees,self.Email)
                    sql1.mycur1.execute(sql,val)
                    sql1.mydb.commit()
                    break
                
                else:
                    print("Issue in Fees....")

    '''  
    def pdf(self):
        ct = datetime.datetime.now()
        a = ct.strftime("%d%m%y_%H_%M_%S") 
        b = ("Atik " +a+ ".pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('helvetica', size=20)
        pdf.cell(200,10,txt="Atik",align='C')

        pdf.output(b)'''     

                
#obj=Payfees()
#obj.pay_fees()  
#obj.pdf()     
        
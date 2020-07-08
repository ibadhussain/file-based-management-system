from tkinter import* #import all from tkinter
from tkinter import ttk,messagebox
import os #import operating system
class File_App:  #class for file app
#----------------------------------------- making the window -----------------------------------------------------------------------------------------------------------    
    def __init__(self): 
        self.root=Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")
#----------------------------------------- making the window -----------------------------------------------------------------------------------------------------------
#---------------------------------------------- title and frame---------------------------------------------------------------------------------------------------------    
        title=Label(self.root,text="FILE BASED RECORD SYSTEM",bd=10,relief=GROOVE,pady=10,font=("Baskerville Old Face",35,"bold"),fg="snow",bg="dark blue").pack(fill=X)
        Student_Frame=Frame(self.root,bd=10,relief=GROOVE,bg="grey25")
        Student_Frame.place(x=20,y=115,height=500)

        stitle=Label(Student_Frame,text="EMPLOYEE DETAILS",font=("Baskerville Old Face",30,"bold"),fg="snow",bg="grey25").grid(row=0,columnspan=4,pady=20)
#---------------------------------------------- title and frame ---------------------------------------------- -------------------------------------------------

#-----------------------------ALL Variables--------------------------------------------------------------------
        self.s_id=StringVar()
        self.name=StringVar()
        self.address=StringVar()
        self.course=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()
#-----------------------------ALL Variables--------------------------------------------------------------------        
#------------------------------------ labe and entry field-----------------------------------------------------------------------------------------------------------------             
        lblsid=Label(Student_Frame,text="Employee Id",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.s_id,relief=GROOVE,width=22,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)
        
        lblconatct=Label(Student_Frame,text="Contact No",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=1,column=2,pady=10,padx=20,sticky="w")
        txtcontact=Entry(Student_Frame,bd=7,textvariable=self.contact,relief=GROOVE,width=22,font="arial 15 bold").grid(row=1,column=3,padx=20,pady=10)
        
        lblname=Label(Student_Frame,text="Full Name",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txtname=Entry(Student_Frame,bd=7,textvariable=self.name,relief=GROOVE,width=22,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)
        
        lbldate=Label(Student_Frame,text="Date(dd/mm/yyyy)",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=2,column=2,pady=10,padx=20,sticky="w")
        txtdate=Entry(Student_Frame,bd=7,textvariable=self.date,relief=GROOVE,width=22,font="arial 15 bold").grid(row=2,column=3,padx=20,pady=10)
        
        lblcourse=Label(Student_Frame,text="Departmet",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txtcourse=Entry(Student_Frame,bd=7,textvariable=self.course,relief=GROOVE,width=22,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)
        
        lbladdress=Label(Student_Frame,text="Address",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txtaddress=Entry(Student_Frame,bd=7,textvariable=self.address,relief=GROOVE,width=22,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)
        
        lblcity=Label(Student_Frame,text="City",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txtcity=Entry(Student_Frame,bd=7,textvariable=self.city,relief=GROOVE,width=22,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)
        
        lbldegree=Label(Student_Frame,text="Salary",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=3,column=2,pady=10,padx=20,sticky="w")
        lblproof=Label(Student_Frame,text="Id Proof",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=4,column=2,padx=10,pady=10,sticky="w")
        lbldegree=Label(Student_Frame,text="Religion",font=("Bahnschrift SemiCondensed",20,"bold"),fg="snow",bg="grey25").grid(row=5,column=2,padx=10,pady=10,sticky="w")
        
#------------------------------------ labe and entry field-----------------------------------------------------------------------------------------------------------------        
#------------------------------------ DROP DOWN MENU ---------------------------------------------------------------------------------------------------------------------
        
        degreecombo=ttk.Combobox(Student_Frame,textvariable=self.degree,width=21,state="readonly",font="arial 15 bold")
        degreecombo["values"]=("Below 20K","Above 25K","Below 50K","Above 50K","Above 100K")
        degreecombo.grid(row=3,column=3,padx=10,pady=10)
        
         
        idcombo=ttk.Combobox(Student_Frame,textvariable=self.proof,width=21,state="readonly",font="arial 15 bold")
        idcombo["values"]=("National Id Card","Passport","Company Id Card")
        idcombo.grid(row=4,column=3,padx=10,pady=10)
        
        paymentcombo=ttk.Combobox(Student_Frame,textvariable=self.payment,width=21,state="readonly",font="arial 15 bold")
        paymentcombo["values"]=("Islam","Christanity","Hinduism","Others")
        paymentcombo.grid(row=5,column=3,padx=10,pady=10)
        
        btnFrame=Frame(self.root,bd=10,bg="dark blue",relief=GROOVE)
        btnFrame.place(x=20,y=640)
#------------------------------------ DROP DOWN MENU ---------------------------------------------------------------------------------------------------------------------
        
#-------------------------------------------- BUTTONS ------------------------------------------------------------------------------------------------------------- 
        btnSave=Button(btnFrame,text="Save",font="arial 15 bold",bd=7,bg="LightSkyBLue1",width=22,command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btndelete=Button(btnFrame,text="Delete",font="arial 15 bold",bd=7,bg="LightSkyBLue1",width=22,command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnclear=Button(btnFrame,text="Clear",font="arial 15 bold",bd=7,bg="LightSkyBLue1",width=22,command=self.clear).grid(row=0,column=2,padx=12,pady=10)
        btnlog=Button(btnFrame,text="Log Out",font="arial 15 bold",bd=7,bg="LightSkyBLue1",width=22,command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnexit=Button(btnFrame,text="Exit",font="arial 15 bold",bd=7,bg="LightSkyBLue1",width=22,command=self.exit_fun).grid(row=0,column=4,padx=12,pady=10)
#---------------------------------------------- BUTTONS ------------------------------------------------------------------------------------------------------------
#--------------------------------------------- BUTTON FRAME ---------------------------------------------------------------------------------------------------------
        File_Frame=Frame(self.root,bd=10,bg="grey25",relief=GROOVE)
        File_Frame.place(x=1300,y=115,width=600,height=495)
#------------------------------------------------ BUTTON FRAME --------------------------------------------------------------------------------------------------------
#------------------------------------------------------------ FILE FRAME ----------------------------------------------------------------------------------------------        
        ftitle=Label(File_Frame,text="All Files",font="arial 16 bold",bg="grey25",fg="snow",bd=7,relief=GROOVE).pack(side=TOP,fill=X)
        
        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        self.root.mainloop() #the frame shows continously
#------------------------------------------------------------ FILE FRAME ----------------------------------------------------------------------------------------------        
#----------------------------------------- FILE SAVING --------------------------------------------------------------------------------------------------------------------------     
    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Studet must be required!!!")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present == "yes":
                    ask=messagebox.askyesno("Update","File already present \n do you want to update it?")
                    if ask>0:
                       self.save_file()
                       messagebox.showinfo("Update","Record as Updated Successfully")
                       self.show_files()
                        
                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record Has Been Saved Successfully")
                    self.show_files()                        
            else:
                self.save_file()
                messagebox.showinfo("Update","Record as Updated Successfully")
                self.show_files()
                

            
    def save_file(self):
        
            f=open("files/"+str(self.s_id.get())+".txt","w")
            f.write(
                str(self.s_id.get())+","+
                str(self.name.get())+","+
                str(self.address.get())+","+
                str(self.course.get())+","+
                str(self.city.get())+","+
                str(self.contact.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())
                )
            f.close()
#----------------------------------------- FILE SAVING --------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------- FUNCTION TO SHOW FILES -------------------------------------------------------------------------------------------------------            
    
    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)
#------------------------------------------------- FUNCTION TO SHOW FILES -------------------------------------------------------------------------------------------------------
#--------------------------------------------------- SAVING DATA FROM THE USER --------------------------------------------------------------------------------------------------                
    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        print(self.file_list.get(get_cursor))
        f1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")
            
        self.s_id.set(value[0])
        self.name.set(value[1])
        self.address.set(value[3])
        self.course.set(value[2])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])
#--------------------------------------------------- SAVING DATA FROM THE USER --------------------------------------------------------------------------------------------------
#------------------------------------------------------ FUNCTION FOR CLEAR BUTTON ------------------------------------------------------------------------------------------------
    def clear(self):
        
        self.s_id.set("")
        self.name.set("")
        self.address.set("")
        self.course.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")
#------------------------------------------------------ FUNCTION FOR CLEAR BUTTON ------------------------------------------------------------------------------------------------
#------------------------------------------------------ FUNCTION FOR DELETE BUTTON ------------------------------------------------------------------------------------------------        
    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Studet must be required!!!")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present == "yes":
                    ask=messagebox.askyesno("Delete","Do you really want to delete")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files()
                        
                else:
                    messagebox.showerror("Error","file not found")
#------------------------------------------------------ FUNCTION FOR DELETE BUTTON ------------------------------------------------------------------------------------------------
#------------------------------------------------------ FUNCTION FOR EXIT BUTTON --------------------------------------------------------------------------------------------------                    
    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Do You Really Want To Exit")
        if ask>0:
            self.root.destroy()
#------------------------------------------------------ FUNCTION FOR EXIT BUTTON --------------------------------------------------------------------------------------------------
#------------------------------------------------------- FUNCTION FOR LOGOUT BUTTON -----------------------------------------------------------------------------------------------            
    def logout(self):
        self.root.destroy()
        import login
        
#------------------------------------------------------- FUNCTION FOR LOGOUT BUTTON -----------------------------------------------------------------------------------------------        
        

'''root=Tk()
ob=File_App(root)
root.mainloop()'''


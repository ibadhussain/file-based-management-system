from tkinter import*
from tkinter import messagebox
class login:    #to make the login for the system
#------------------------------------------creating frame----------------------------------------------------------------------------------
    def __init__(self,root):
        self.root=root
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")
#------------------------------------------creating frame----------------------------------------------------------------------------------
#----------------------------------------------- frame colour and adjustment ---------------------------------------------------------------  
        F1=Frame(self.root,bd=10,relief=GROOVE,bg="dark blue")
        F1.place(x=450,y=150,width=700,height=400)
#----------------------------------------------- frame colour and adjustment --------------------------------------------------------------- 
        
        self.user=StringVar()
        self.password=StringVar()
        
                
#---------------------------------------------------user name label and title--------------------------------------------------------------------------------        
        title=Label(F1,text="LOGIN",font=("Times new roman",30,"bold"),bg="LightSkyBLue1",bd=2,relief=GROOVE).grid(row=0,columnspan=2,pady=20)
        
        lblusername=Label(F1,text="Username:",font=("Times new roman",25,"bold"),bg="LightSkyBLue1",bd=2).grid(row=1,column=0,padx=10)
    
        txtuser=Entry(F1,bd=7,relief=GROOVE,textvariable=self.user,width=30,font=("arial 15 bold")).grid(row=1,column=1,padx=10,pady=10)
#---------------------------------------------------user name label and title--------------------------------------------------------------------------------
#---------------------------------------------------password label and title--------------------------------------------------------------------------------
        
        lblpass=Label(F1,text="Password:",font=("Times new roman",25,"bold"),bg="LightSkyBLue1",bd=2).grid(row=2,column=0,padx=10)
        
        txtpass=Entry(F1,bd=7,relief=GROOVE,show="*",textvariable=self.password,width=30,font=("arial 15 bold")).grid(row=2,column=1,padx=10,pady=10)
#---------------------------------------------------user name label and title--------------------------------------------------------------------------------
#-------------------------------------- BUTTON SECTION ----------------------------------------------------------------------------------------------           
        btnlog= Button(F1,text="login",font="arial 15 bold",bg="LightSkyBLue1",fg="black",bd=7,width=11,command=self.logfun).place(x=10,y=300)
        btnreset= Button(F1,text="Reset",font="arial 15 bold",bg="LightSkyBLue1",fg="black",bd=7,width=11,command=self.reset).place(x=245,y=300)
        btnexit= Button(F1,text="Exit",font="arial 15 bold",bg="LightSkyBLue1",fg="black",bd=7,width=11,command=self.exit_fun).place(x=480,y=300)
#-------------------------------------- BUTTON SECTION ----------------------------------------------------------------------------------------------------    
##-------------------------------------- user name & pass ---------------------------------------------------------------------------            
    def logfun(self):
        if self.user.get()=="ibad" and self.password.get()=="61984":
            self.root.destroy()
            import software
            software.File_App()
            
        elif self.user.get()=="ssuet" and self.password.get()=="pf1234":
            self.root.destroy()                                            
            import software
            software.File_App()
        else:
            messagebox.showerror("Error","Invalid Username Or Password")
#-------------------------------------- user name and pass ---------------------------------------------------------------------------    
#-------------------------------------- RESET BUTTON ---------------------------------------------------------------------------            
    def reset(self):
        self.user.set("")
        self.password.set("")
#-------------------------------------- RESET BUTTON ---------------------------------------------------------------------------
#-------------------------------------- EXIT BUTTON ---------------------------------------------------------------------------    
    def exit_fun(self):
        opt=messagebox.askyesno("Exit","Do you really want to exit?")
        if opt>0:
            self.root.destroy()
        else:
            return
        
#-------------------------------------- EXIT BUTTON ---------------------------------------------------------------------------            
root=Tk()
ob=login(root)
root.mainloop() #the GUI dosen't executes on it's own

from tkinter import *
import sqlite3
import tkinter.messagebox


#conect to database
conn = sqlite3.connect('database.db')
c = conn.cursor()



#the first page with all the buttons
class Welcome():
    def __init__(self, master):
        self.master=master
        
        self.master.title('Welcome!')
        

        self.left = Frame(master, width=700, height=720, bg='lightblue')
        self.left.pack(side=LEFT)

        

        self.heading = Label(self.left, text = "Baza de date angajati", font=('arial 40 bold'),fg='white', bg='lightblue')
        self.heading.place(x=0,y=0)

        self.nume = Label(self.left,text="Adauga numele angajatului", font=('arial 18 bold'),fg='black',bg='lightblue')
        self.nume.place(x=0,y=100)

        self.cnp = Label(self.left,text="Adauga CNP-ul angajatului", font=('arial 18 bold'),fg='black',bg='lightblue')
        self.cnp.place(x=0,y=140)

        self.salar = Label(self.left,text="Adauga salarul angajatului", font=('arial 18 bold'),fg='black',bg='lightblue')
        self.salar.place(x=0,y=180)

        self.nume_ent = Entry(self.left, width=30)
        self.nume_ent.place(x=340,y=110)

        self.cnp_ent = Entry(self.left, width=30)
        self.cnp_ent.place(x=340,y=150)

        self.salar_ent = Entry(self.left, width=30)
        self.salar_ent.place(x=340,y=190)

        self.submit = Button(self.left, text = "Adauga angajat", width = 20, height=2, bg='steelblue',command=self.adauga_angajat)
        self.submit.place(x=350, y=220)

        self.retrive = Button(self.left, text = "Afiseaza lista angajatilor", width = 40, height=3, bg='steelblue',command=self.toate_datele)
        self.retrive.place(x=20, y=320)

        
        self.modifier = Button(self.left, text = "Modifica detalii angajat/ Sterge angajat", width = 40, height=3, bg='steelblue',command=self.modifica)
        self.modifier.place(x=20, y=400)

        self.fiver = Button(self.left, text = "Scade 5% din salarul angajatilor", width = 40, height=3, bg='steelblue',command=self.cinci)
        self.fiver.place(x=20, y=480)



    
            
            

        
        
          
        

    #add to the database
    def adauga_angajat(self):
        self.val1 = self.nume_ent.get()
        self.val2 = self.cnp_ent.get()
        self.val3 = self.salar_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '':
            tkinter.messagebox.showinfo("Atentie","Nu ati completat toate campurile")
        else:
            sql="INSERT INTO Angajati (Nume, CNP, Salar) VALUES (?,?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3))
            conn.commit()


    #5% off
    def cinci(self):
        sql="UPDATE Angajati SET Salar = Salar * 0.95"
        c.execute(sql)
        conn.commit()
        

        
        
    #the other two pages
    def toate_datele(self):
        root2=Toplevel(self.master)
        mygui=records(root2)
    
    def modifica(self):
        root3=Toplevel(self.master)
        mygui=modifica(root3)
        
#Getting the records from the database
class records():
     
    def __init__(self,master):
        self.master=master
        self.master.geometry('400x400+0+0')
        self.master.title('Lista angajatilor')
        self.connection = sqlite3.connect('database.db')
        self.cur = self.connection.cursor()
        self.dateLabel = Label(self.master, text="Nume", width=10)
        self.dateLabel.grid(row=0, column=0)
        self.BMILabel = Label(self.master, text="CNP", width=10)
        self.BMILabel.grid(row=0, column=1)
        self.stateLabel = Label(self.master, text="Salar", width=10)
        self.stateLabel.grid(row=0, column=2)
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.master, text=dat[1]).grid(row=index+1, column=0)
            Label(self.master, text=dat[2]).grid(row=index+1, column=1)
            Label(self.master, text=dat[3]).grid(row=index+1, column=2)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM Angajati")
        return self.cur.fetchall()

#search and modify records from database
class modifica():
    def __init__(self,master):
        self.master=master
        self.master.geometry("650x700+0+0")
        self.master.title('Modifica lista angajatilor')
        self.heading = Label(master, text="Modificati datele angajatului",  fg='steelblue', font=('arial 20 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name 
        self.name = Label(master, text="Introduceti numele angajatului", font=('arial 13 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        # search button
        self.search = Button(master, text="Cauta", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)
        # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 

        sql = "SELECT * FROM Angajati WHERE nume LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.nume = self.row[1]
            self.CNP = self.row[2]
            self.Salar = self.row[3]
            
        # creating the update form
        self.uname = Label(self.master, text="Nume", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="CNP", font=('arial 18 bold'))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Salar", font=('arial 18 bold'))
        self.ugender.place(x=0, y=220)

        

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.nume))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.CNP))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.Salar))

        
        # button to execute update
        self.update = Button(self.master, text="Modifica", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Sterge angajatul", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
       

        query = "UPDATE Angajati SET Nume=?, CNP=?, Salar=? WHERE Nume LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3,  self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Succes.", "Informatia a fost modificata")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM Angajati WHERE Nume LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Succes", "Stergere realizata")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
           




root = Tk()
b=Welcome(root)
root.geometry("550x600+0+0")
root.resizable(False,False)

root.mainloop()

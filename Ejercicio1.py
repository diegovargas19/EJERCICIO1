#Muestra widgets
#Vargas Gonzalez Diego Alejandro
#09 de marzo 2023

from tkinter import*
from tkinter import ttk


class Ejercicio1:
    #init es el tipo constructor de la clase
    def __init__(self, raiz):#raiz = root
        raiz.title("Ejercicio1")

        notebook = ttk.Notebook(raiz)
        notebook.pack()

        frameAdd = ttk.Frame(notebook, width=500, height=500)
        frameAdd.pack(fill='both', expand='1')
        frameDelete = ttk.Frame(notebook, width=500, height=500)
        frameDelete.pack(fill='both', expand='1')
        frameSearch = ttk.Frame(notebook, width=500, height=500)
        frameSearch.pack(fill='both', expand='1')
        frameServices = ttk.Frame(notebook, width=500, height=500)
        frameServices.pack(fill='both', expand='1')
        frameHelp = ttk.Frame(notebook, width=500, height=500)
        frameHelp.pack(fill='both', expand='1')

        notebook.add(frameAdd,  text="          Add          ")
        notebook.add(frameDelete, text="           Delete          ")
        notebook.add(frameSearch, text="           Search          ")
        notebook.add(frameServices, text="           Services          ")
        notebook.add(frameHelp, text="           Help          ")

        frame0 = ttk.Frame(frameAdd, padding="150 5 251 5", borderwidth=3, relief="raised")
        frame0.grid(column=0, row=0)

        frame1 = ttk.Frame(frameAdd, padding="33 10 147 10", borderwidth=3, relief="raised")
        frame1.grid(column=0, row=1)

        frame2 = ttk.Frame(frameAdd, padding="12 10 148 10", borderwidth=3, relief="raised")
        frame2.grid(column=0, row=2)

        frame3 = ttk.Frame(frameAdd, padding="20 10 136 10", borderwidth=3, relief="raised")
        frame3.grid(column=0, row=3)

        frame4 = ttk.Frame(frameAdd, padding="112 10 213 35", borderwidth=3, relief="raised")
        frame4.grid(column=0, row=4)

        firstnameLabel = ttk.Label(frame1, text="First Name: ")#,  font=("Arial", 8) )
        firstnameLabel.grid(column=0, row=0)

        firstnameEntry = ttk.Entry(frame1, width=12)
        firstnameEntry.grid(column=1, row=0)

        lastnameLabel = ttk.Label(frame1, text="Last Name: " )
        lastnameLabel.grid(column=2, row=0, padx=3)

        lastnameEntry = ttk.Entry(frame1, width=17)
        lastnameEntry.grid(column=3, row=0)

        birthdateLabel = ttk.Label(frame1, text="Birth Date:" )
        birthdateLabel.grid(column=0, row=1, pady=20)

        dayEntry = ttk.Entry(frame1, width=2)
        dayEntry.grid(column=1,row=1, sticky=W)

        monthEntry = ttk.Entry(frame1, width=2)
        monthEntry.grid(column=1,row=1)

        yearEntry = ttk.Entry(frame1, width=2)
        yearEntry.grid(column=1,row=1, sticky=E)

        countryLabel = ttk.Label(frame1, text="Country:" )
        countryLabel.grid(column=2, row=1, pady=20)

        countryEntry = ttk.Entry(frame1, width=12)
        countryEntry.grid(column=3,row=1, sticky=W)

        creditcardLabel = ttk.Label(frame2, text="Credit Card(if any):")
        creditcardLabel.grid(column=0, row=0)

        creditcardEntry = ttk.Entry(frame2, width=20)
        creditcardEntry.grid(column=1, row=0)

        creditcardtypeLabel = ttk.Label(frame2, text="Credit Card Type(if any):")
        creditcardtypeLabel.grid(column=0, row=1, pady=20)

        visa = Radiobutton(frame2, text="Visa")
        visa.grid(column=1, row=1)

        mastercard = Radiobutton(frame2, text="Mastercard")
        mastercard.grid(column=2, row=1)

        roomtypeLabel = ttk.Label(frame3, text="Room Type:")
        roomtypeLabel.grid(column=0, row=0)

        normal = Radiobutton(frame3, text="Normal")
        normal.grid(column=1, row=0)

        familiar = Radiobutton(frame3, text="Familiar")
        familiar.grid(column=1, row=1)

        special = Radiobutton(frame3, text="Special")
        special.grid(column=1, row=2)

        totalLabel = ttk.Label(frame3, text="Total Staying Time(days):")
        totalLabel.grid(column=2, row=0, padx=20)

        totalEntry = ttk.Entry(frame3, width=5)
        totalEntry.grid(column=3, row=0)

        button = ttk.Button(frame4, text="Submit",).grid(column=1, row=0)

        vacioframe0 = ttk.Label(frame0, text="")
        vacioframe0.grid(column=0, row=0, padx=50)

        vacioframe4= ttk.Label(frame4, text="")
        vacioframe4.grid(column=0, row=0, padx=50)









        


        

        
  
if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara este mensaje si es el principal")


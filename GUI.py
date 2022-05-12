from tkinter import *
from tkinter.scrolledtext import *


class SmartCartDisplay(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Smart Cart")
        self.geometry('800x480')
        self['bg'] = 'white'
        
        self.f = Frame(self,background='white')
        self.f.pack(side="top",expand=True,fill="both")
        

    def removeWidgets(self):
        for widget in self.f.winfo_children():
            widget.destroy()

    def refresh(self, item):
            
        items = []
        cost = []
        quantity = []
        
        for key in item:
            items.append(key)
            cost.append(item[key][0])
            quantity.append(item[key][1])
        
        for widget in self.f.winfo_children():
            widget.destroy()
            
        Label(self.f, text='Check Me Out!', font=("Helvetica", 25, 'bold'), fg='black', bg='white').place(x=300, y=10)
        Label(self.f, text='Item', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white').place(x=80, y=90)
        Label(self.f, text='Quantity', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white').place(x=450, y=90)
        Label(self.f, text='Price', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white').place(x=650, y=90)
        
        y_val = 150
        for i in items :
            if (len(i) > 30):
                i = i[0:30]
            Label(self.f, text=i, font=("Helvetica", 15), fg='black', bg='white').place(x=75, y=y_val)
            y_val += 30
        
        y_val1 = 150
        for i in quantity:
            
            Label(self.f, text=i, font=("Helvetica", 15), fg='black', bg='white').place(x=450, y=y_val1)
            y_val1 += 30
        
        y_val2 = 150
        for i in cost:
            
            Label(self.f, text=i, font=("Helvetica", 15), fg='black', bg='white').place(x=650, y=y_val2)
            y_val2 += 30
        
    
    def checkoutScreen(self):
        self.removeWidgets()
        Label(self.f, text='Checking out...', font=("Helvetica", 40, 'bold'), fg='red', bg='white').place(relx=0.5, rely=0.5, anchor=CENTER)
        
    def thankyou(self):
        self.removeWidgets()
        Label(self.f, text='Thank you!', font=("Helvetica", 40, 'bold'), fg='blue', bg='white').place(relx=0.5, rely=0.5, anchor=CENTER)

            

# def update(obj, window, item):
#     items = []
#     cost = []
#     quantity = []
    
#     for key in item:
#         items.append(key)
#         cost.append(item[key][0])
#         quantity.append(item[key][1])
    
    
    
#     Label(window, text='Check Me Out!', font=("Helvetica", 25, 'bold'), fg='black', bg='white').place(x=300, y=10)

    
#     Label(window, text='Item', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white').place(x=80, y=90)

    
#     Label(window, text='Quantity', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white').place(x=450, y=90)

  
#     Label(window, text='Price', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white').place(x=650, y=90)

    
#     y_val = 150
#     for i in items :
        
#         Label(window, text=i, font=("Helvetica", 15), fg='black', bg='white').place(x=75, y=y_val)
#         y_val += 20
    
#     y_val1 = 150
#     for i in quantity:
        
#         Label(window, text=i, font=("Helvetica", 15), fg='black', bg='white').place(x=450, y=y_val1)
#         y_val1 += 20
     
#     y_val2 = 150
#     for i in cost:
         
#          Label(window, text=i, font=("Helvetica", 15), fg='black', bg='white').place(x=650, y=y_val2)
#          y_val2 += 20
    

#     obj.after(1000,update(obj, window, item))
#     # for widgets in window.winfo_children():
#     #     widgets.destroy()
#     return

# def f1(item):
    
#     window = Tk()
#     window.title("Application")
#     window.geometry("800x480")
#     window.config(background='white')
#     f = Frame(window, background='white')
#     f.pack(side="top",expand=True,fill="both")
 
#     # text_1 = ScrolledText(window,height=35, width=40, border=2)
#     # text_1.place(x=150, y=150)
    
  
    
#     #text_2 = ScrolledText(window,height=35, width=40, border=2)
#     #text_2.place(x=550, y=150)
#     #
    
    
#     #text_3 = ScrolledText(window,height=35, width=40, border=2)
#     #text_3.place(x=950, y=150)
    
#     '''
#     remove_item_btn = Button(window, text='Remove Item', width=20, height=2, font=("Helvetica", 14), border=3, cursor='hand2')
#     remove_item_btn.place(x=170, y=750)
    
#     total_label = Label(window, text='Total: ', font=("Helvetica", 25, 'bold'), fg='black', bg='white')
#     total_label.place(x=1000, y=750)
    
#     under_line = Label(window, text='                  ', font=("Helvetica", 25, 'bold','underline'), fg='black', bg='white')
#     under_line.place(x=1100, y=750)
#     '''
#     window.after(0,update,window, f, item)
#     window.mainloop()

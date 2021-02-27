import requests
from tkinter import *
import tkinter as tk

#Constructor
class CurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = float(amount) / float(self.currencies[from_currency])
        amount = round(float(amount) * float(self.currencies[to_currency]),4)
    def dropdown(self, every_currency):
        every_currency = self.currencies
        return every_currency
    def myAmount(self):
        from_currency = clicked_from_currency.get()
        to_currency = clicked_to_currency.get()
        last_amount = float(amount_field.get())
        if from_currency != 'USD':
            last_amount = float(last_amount) / float(self.currencies[from_currency])
        last_amount = round(float(last_amount) * float(self.currencies[to_currency]), 4)
        converted_amount_field_label = Label(window, text=last_amount, fg='black', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)
        converted_amount_field_label.place(relx=0.55, rely=0.4, anchor='n')

#Main
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)

#User Interface
window = tk.Tk()
window.geometry("1200x800")

#Labels
label1 = tk.Label(window, text="Currency Converter", bg="white", relief=tk.RAISED, borderwidth=3)
label1.config(font=('Courier', 20, 'bold'))
label2 = tk.Label(window, text=f"1 Sterling Pound equals {converter.convert('GBP','USD',1)} United States Dollars \n Date: {converter.data['date']}", relief=tk.GROOVE, borderwidth=5)
label2.config(font=('Courier', 15, 'bold'))
converted_amount_field_label = Label(window, text="", fg='black', bg='white', relief=tk.RIDGE,justify=tk.CENTER, width=17, borderwidth=3)
converted_amount_field_label.place(relx=0.55, rely=0.4, anchor='n')
amount_field = Entry(window, bd=3, relief=tk.RIDGE, justify=tk.CENTER)
amount_field.place(relx=0.4, rely=0.4, anchor='n')

#Dropdown menu button
every_currency = list()
options = converter.dropdown(every_currency)

clicked_from_currency = StringVar()
clicked_to_currency = StringVar()

drop_from_currency = OptionMenu(window, clicked_from_currency, *options)
drop_from_currency.config(font=('Courier', 20, 'bold'))
drop_to_currency = OptionMenu(window, clicked_to_currency, *options)
drop_to_currency.config(font=('Courier', 20, 'bold'))

#Converter button
myButton = Button(window, text="Convert", command=converter.myAmount, font=('Courier', 15, 'bold'), bg="gray90")

#Packs
label1.pack()
label2.pack()
drop_from_currency.place(relx=0.4, rely=0.3, anchor='n')
drop_to_currency.place(relx=0.55, rely=0.3, anchor='n')
myButton.place(relx=0.475, rely=0.5, anchor='n')

#End
window.mainloop()



from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp:
    def __init__(self, master):
        # Initialize the GUI window
        self.master = master
        self.master.title("Currency Converter")

        # Label and entry for the amount
        self.amount_label = tk.Label(master, text="Enter amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and dropdown menu for the source currency
        self.from_currency_label = tk.Label(master, text="From currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_currency_var = tk.StringVar()
        self.from_currency_menu = ttk.Combobox(master, textvariable=self.from_currency_var)
        self.from_currency_menu['values'] = self.get_currency_list()
        self.from_currency_menu.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency_menu.set('USD')  # Set a default value

        # Label and dropdown menu for the target currency
        self.to_currency_label = tk.Label(master, text="To currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_currency_var = tk.StringVar()
        self.to_currency_menu = ttk.Combobox(master, textvariable=self.to_currency_var)
        self.to_currency_menu['values'] = self.get_currency_list()
        self.to_currency_menu.grid(row=2, column=1, padx=10, pady=10)
        self.to_currency_menu.set('EUR')  # Set a default value

        # Button to trigger the conversion
        self.convert_button = tk.Button(master, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Label to display the result
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def get_currency_list(self):
        # Fetch the list of currencies using forex-python
        c = CurrencyRates()
        return list(c.get_rates('USD').keys())  # Assuming USD as a base currency for the list

    def get_exchange_rate(self, from_currency, to_currency):
        # Get the exchange rate between two currencies
        c = CurrencyRates()
        return c.get_rate(from_currency, to_currency)

    def convert_currency(self):
        try:
            # Get user input
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get().upper()
            to_currency = self.to_currency_var.get().upper()

            # Perform the currency conversion
            exchange_rate = self.get_exchange_rate(from_currency, to_currency)
            converted_amount = amount * exchange_rate

            # Display the result
            result_text = f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
            self.result_label.config(text=result_text)
        except Exception as e:
            # Handle errors
            error_text = f"An error occurred: {e}"
            self.result_label.config(text=error_text)

def main():
    # Entry point of the program
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()

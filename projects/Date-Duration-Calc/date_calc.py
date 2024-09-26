from datetime import datetime, timedelta

#This project will allow the user to input two dates and the program
#will return the difference between the two dates

class Date:
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        self.request = 1

    def calculate_difference(self):
        time_difference = self.date2 - self.date1
        self.days = time_difference.days

    def calculate_years_weeks_days(self):
        self.years = self.days // 365
        self.remaining_days = self.days % 365
        self.weeks = self.remaining_days // 7
        self.days = self.remaining_days % 7

    def get_date_input(self):
        date1_str = input("Enter the first date (YYYY-MM-DD): ")
        date2_str = input("Enter the second date (YYYY-MM-DD): ")
        self.date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        self.date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    
    def display_result(self):
        print(f"Years: {self.years}")
        print(f"Weeks: {self.weeks}")
        print(f"Days: {self.days}")

    def calculate_and_display(self):
        self.calculate_difference()
        self.calculate_years_weeks_days()
        self.display_result()

date_calculator = Date(None, None)

date_calculator.get_date_input()
date_calculator.calculate_and_display()

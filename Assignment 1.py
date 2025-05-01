class Date_Calculator:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def find_date(self):
        return self.day, self.month, self.year


class Zeller(Date_Calculator):

    def __init__(self, day: int, month: int, year: int):
        super().__init__(day, month, year)

    def calculate_day_of_week(self):
        day, month, year = self.find_date()

        if month < 3:
            month += 12
            year -= 1

        k = year % 100  # Year within century
        j = year // 100  # Century component

        day_of_week = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7

        weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        return weekdays[day_of_week]


# Get user input for the date
day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

answer = Zeller(day, month, year)

print(f"The day of the week for {day}/{month}/{year} is: {answer.calculate_day_of_week()}")

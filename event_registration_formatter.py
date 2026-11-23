# Event Registration Formatter (Version 3: added date formatting)

from datetime import date

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

try:
    year = int(input("Enter event year: "))
    month = int(input("Enter event month: "))
    day = int(input("Enter event day: "))
    event_date = date(year, month, day)
except ValueError:
    print("\nInvalid date. Please enter numbers for a real calendar date.")
else:
    full_name = (first_name.strip() + " " + last_name.strip()).title()
    readable_date = event_date.strftime("%B %d, %Y").replace(" 0", " ")

    print("\nStudent Event Registration Summary")
    print("Name:", full_name)
    print("Name Code:", full_name.upper())
    print("Section:", section.strip().upper())
    print("Event:", event_name.strip().title())
    print("Event Date:", readable_date)
    print("Language Used: Python")
    print("String Feature Used: strip(), title(), upper()")
    print("Date/Time Feature Used: datetime")
    print("Registration record created successfully.")

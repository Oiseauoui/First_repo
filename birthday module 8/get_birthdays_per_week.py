import os
print("Current working directory:", os.getcwd())
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Get the current date
    current_date = datetime.now().date()

    # Calculate the date 7 days from now
    target_date = current_date + timedelta(days=7)

    # Find the next Monday from the target date
    days_until_monday = (7 - target_date.weekday()) % 7
    monday_date = target_date + timedelta(days=days_until_monday)

    # Initialize a dictionary to store birthdays for each day of the week
    birthdays_per_day = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Loop through each user's information
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        days_until_birthday = (birthday.replace(year=current_date.year) - monday_date).days

        if days_until_birthday >= 0 and days_until_birthday < 7:
            day_of_birthday = (monday_date + timedelta(days=days_until_birthday)).strftime("%A")
            if day_of_birthday in ["Saturday", "Sunday"]:
                day_of_birthday = "Monday"  # Users with weekend birthdays are congratulated on Monday
            birthdays_per_day[day_of_birthday].append(user["name"])

    # Print the birthdays for each day of the week
    for day, names in birthdays_per_day.items():
        if names:
            print(f"Happy birthday! {day}: {', '.join(names)}")

def read_users_data(file_path):
    users_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("name: ") and "birthday: " in line:
                name_start = line.find("name: ") + len("name: ")
                name_end = line.find(",", name_start)
                name = line[name_start:name_end].strip()

                birthday_start = line.find("birthday: ") + len("birthday: ")
                birthday = line[birthday_start:].strip(",").strip()

                users_data.append({"name": name, "birthday": birthday})
            else:
                print(f"Ignored line: {line}")
    return users_data


# Test list of users
users_file_path = r'E:\PYTHON\REPOSITORY PYTHON\First_repo\birthday module 8\users.txt'
users_data = read_users_data(users_file_path)

# Call the function with the test list of users
get_birthdays_per_week(users_data)
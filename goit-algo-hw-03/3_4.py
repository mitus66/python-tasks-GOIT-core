# Task 3.4.
# Displays a list of colleagues whose birthdays need to be celebrated one week in advance

from datetime import datetime, date, timedelta


def string_to_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d").date()


def date_to_string(date_obj):
    return date_obj.strftime("%Y.%m.%d")


def find_next_weekday(start_date, weekday):
    days_ahead = (weekday - start_date.weekday() + 7) % 7
    return start_date + timedelta(days=days_ahead or 7)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:  # Saturday or Sunday
        return find_next_weekday(birthday, 0)  # Move to Monday
    return birthday


def prepare_user_list(users):
    prepared_users = []
    for user in users:
        birth_date = string_to_date(user["birthday"])
        prepared_users.append({"name": user["name"], "birthday": birth_date})
    return prepared_users


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_difference = (birthday_this_year - today).days
        if 0 <= days_difference <= days:
            congratulation_date = adjust_for_weekend(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": "1955.4.8"},
    {"name": "Steve Jobs", "birthday": "1955.4.9"},
    {"name": "Jinny Lee", "birthday": "1956.4.6"},
    {"name": "Sarah Lee", "birthday": "1957.4.10"},
    {"name": "Jonny Lee", "birthday": "1958.4.11"},
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]

prepared_users = prepare_user_list(users)
print(get_upcoming_birthdays(prepared_users, 7))
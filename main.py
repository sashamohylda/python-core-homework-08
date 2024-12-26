from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(days=7)
    birthdays = defaultdict(list)

    for user in users:
        birthday = user["birthday"].replace(year=today.year)

        if birthday < today:
            birthday = user["birthday"].replace(year=today.year + 1)
        
        if today <= birthday < next_week:
            day_name = birthday.strftime('%A')  
            if birthday.weekday() >= 5:  
                birthdays["Monday"].append(user["name"])
            else:
                birthdays[day_name].append(user["name"])

    return birthdays

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14).date()},
        {"name": "Elon Musk", "birthday": datetime(1971, 6, 28).date()},
        {"name": "Jeff Bezos", "birthday": datetime(1964, 1, 12).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

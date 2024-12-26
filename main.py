from datetime import date, datetime

def get_birthdays_per_week(users):
    days_of_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    
    today = date.today()
    
    for user in users:
        birthday = user['birthday']
        
        if birthday.replace(year=today.year) < today:
            birthday = birthday.replace(year=today.year + 1)
        
        day_of_week = birthday.weekday()
        
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day_name = day_names[day_of_week]
        
        days_of_week[day_name].append(user['name'])
    
    return days_of_week

if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Kim", "birthday": datetime(1990, 4, 15).date()},
    ]
    
    result = get_birthdays_per_week(users)
    print(result)
    
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

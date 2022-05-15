from datetime import datetime, timedelta


WEEKDAYS = ("\nMonday", "\nTuesday", "\nWednesday", "\nThursday", "\nFriday")

USERS = [
    {
        "name": "Bill",
        "birthday": datetime(year=1990, month=8, day=17).date()
    },
    {
        "name": "Andrew",
        "birthday": datetime(year=1990, month=8, day=18).date()
    },
    {
        "name": "Jill",
        "birthday": datetime(year=1989, month=8, day=30).date()
    },
    {
        "name": "Till",
        "birthday": datetime(year=1979, month=8, day=18).date()
    },
    {
        "name": "Jan",
        "birthday": datetime(year=1979, month=8, day=20).date()
    }
]


def close_birthday_users(users, start, end):
    now = datetime.today().date()
    result = []
    for user in users:
        birthday = user["birthday"]
        birthday = birthday.replace(year=now.year)
        if start <= birthday <= end:
            result.append(user)
    return result


def congratulate(users):
    now = datetime.today().date()
    current_week_day = now.weekday()
    if current_week_day >= 5:
        start_date = now - timedelta(days=(7 - current_week_day))
    elif current_week_day == 0:
        start_date = now - timedelta(days=2)
    else:
        start_date = now
    days_ahead = 4 - current_week_day
    if days_ahead < 0:
        days_ahead += 7
    end_date = now + timedelta(days=days_ahead)
    birthday_users = close_birthday_users(users, start=start_date, end=end_date)
    weekday = None
    congratulation_day = {}
    for user in sorted(birthday_users, key=lambda x: x['birthday'].replace(year=now.year)):
        user_birthday = user['birthday'].replace(year=now.year).weekday()
        if WEEKDAYS[user_birthday] not in congratulation_day.keys():
            congratulation_day[WEEKDAYS[user_birthday]] = [user['name']]
        else:
            congratulation_day[WEEKDAYS[user_birthday]] += [user['name']]
    for k, v in congratulation_day.items():
        print(f'{k}: {", ".join(v)}')



if __name__ == '__main__':
    congratulate(USERS)
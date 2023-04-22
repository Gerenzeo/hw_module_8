from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": 'Paul Wrasker', "birthday": datetime(year=1997, month=4, day=21)},
    {"name": 'Bill Kinton', "birthday": datetime(year=1986, month=4, day=22)},
    {"name": 'Maria Sushko', "birthday": datetime(year=1999, month=4, day=23)},
    {"name": 'Max Cain', "birthday": datetime(year=1974, month=4, day=24)},
    {"name": 'John Week', "birthday": datetime(year=1990, month=4, day=25)},
    {"name": 'Sarah Connor', "birthday": datetime(year=1957, month=4, day=26)},
    {"name": 'Julia Mona', "birthday": datetime(year=1963, month=4, day=27)},
    {"name": 'Natalia Munic', "birthday": datetime(year=1987, month=4, day=28)},
    {"name": 'Max Scoot', "birthday": datetime(year=1994, month=5, day=29)},
    {"name": 'Robert Animil', "birthday": datetime(year=1991, month=4, day=30)}
]

def get_birthdays_per_week(users):
    Birthdays = defaultdict(list)
    today = datetime.now()
    start_date = datetime(year=today.year, month=today.month, day=today.day)
    end_date = today + timedelta(days=5)

    if today.weekday() == 0:
        start_date = start_date - timedelta(days=2)

    for user in users:
        user_date = user['birthday'].replace(year=today.year)
        if start_date <= user_date <= end_date:
            if user_date.weekday() == 5:
                user_date = user_date + timedelta(days=2)
            if user_date.weekday() == 6:
                user_date = user_date + timedelta(days=1)
            
            Birthdays[str(user_date.strftime('%A')).lower()].append(user['name'])

    for date, names in Birthdays.items():
        print(f'{date.title()}:', ', '.join(name for name in names))

if __name__ == '__main__':
    get_birthdays_per_week(users)

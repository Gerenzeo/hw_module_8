from datetime import datetime, timedelta

users = [
    {"name": 'Paul Wrasker', "birthday": datetime(year=1997, month=4, day=21)},
    {"name": 'Bill Kinton', "birthday": datetime(year=1986, month=4, day=23)},
    {"name": 'Maria Sushko', "birthday": datetime(year=1999, month=4, day=18)},
    {"name": 'Max Cain', "birthday": datetime(year=1974, month=4, day=29)},
    {"name": 'John Week', "birthday": datetime(year=1990, month=4, day=22)},
    {"name": 'Sarah Connor', "birthday": datetime(year=1957, month=4, day=21)},
    {"name": 'Julia Mona', "birthday": datetime(year=1963, month=4, day=16)},
    {"name": 'Natalia Munic', "birthday": datetime(year=1987, month=4, day=27)},
    {"name": 'Max Scoot', "birthday": datetime(year=1994, month=4, day=1)},
    {"name": 'Robert Animil', "birthday": datetime(year=1991, month=4, day=28)}
]

def get_birthdays_per_week(users):
    collected_birthdays = {
        (0, "monday"): [],
        (1, "tuesday"): [],
        (2, "wednesday"): [],
        (3, "thursday"): [],
        (4, "friday"): [],
        (5, "saturday"): [],
        (6, "sunday"): []
    }
    today = datetime.now()
    day = 0

    for _ in range(7):
        interval = timedelta(days=day)
        current_day = interval + today

        for users_list in users:
            if (users_list['birthday'].day == current_day.day and users_list['birthday'].month == current_day.month):
                current_weekday = current_day.weekday()
                day_of_week = list(collected_birthdays.keys())[current_weekday][1]
                
                collected_birthdays[current_weekday, day_of_week].append(users_list['name'])

        day += 1

    collected_birthdays[(0, "monday")].extend(collected_birthdays[(5, "saturday")])
    collected_birthdays[(0, "monday")].extend(collected_birthdays[(6, "sunday")])
    collected_birthdays[(5, "saturday")].clear()
    collected_birthdays[(6, "sunday")].clear()

    for key, values in collected_birthdays.items():
        if collected_birthdays[key] != []:
            print(f'{key[1].title()}:', ", ".join([value for value in set(values)]))
    
if __name__ == '__main__':
    get_birthdays_per_week(users)

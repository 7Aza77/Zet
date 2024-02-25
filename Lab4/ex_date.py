from datetime import datetime, timedelta


#task3
def drop_microseconds(date_mic):
    return date_mic.strftime("%Y-%m-%d %H-%M-%S")


#task4
def calculate_time_seconds(dat1, dat2):
    time_difference = dat2 - dat1
    return time_difference.total_seconds()


#task1
now_date = datetime.now()
result_date = now_date - timedelta(days=5)

print("Результат после вычитания пяти дней:", drop_microseconds(result_date))


#task2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера: ", drop_microseconds(yesterday))
print("Сегодня: ", drop_microseconds(today))
print("Завтра: ", drop_microseconds(tomorrow))

print("Разница между вчерашним и завтрешним в секундах: ", calculate_time_seconds(yesterday, tomorrow))
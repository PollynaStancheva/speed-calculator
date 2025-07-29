print("Въведете разстоянието между точка А и точка Б (в км):")
while True:
    dist_str = input()
    if dist_str.isdigit() and int(dist_str) > 0:
        distance = int(dist_str)
        break
    else:
        print("Моля, въведете цяло положително число за разстоянието:")

print("Въведете времето за пътуване (часове):")
while True:
    hours_str = input()
    if hours_str.isdigit() and int(hours_str) >= 0:
        hours = int(hours_str)
        break
    else:
        print("Моля, въведете цяло число за часове:")

print("Въведете времето за пътуване (минути):")
while True:
    minutes_str = input()
    if minutes_str.isdigit() and 0 <= int(minutes_str) < 60:
        minutes = int(minutes_str)
        break
    else:
        print("Моля, въведете цяло число от 0 до 59 за минути:")

total_time = hours + (minutes / 60)

if total_time == 0:
    print("Времето за пътуване не може да е 0.")
else:
    avg_speed = distance / total_time
    print(f"Средната скорост е {avg_speed:.2f} км/ч.")

    print("Въведете ограничението на скоростта (км/ч):")
    while True:
        limit_str = input()
        if limit_str.isdigit() and int(limit_str) > 0:
            speed_limit = int(limit_str)
            break
        else:
            print("Моля, въведете цяло положително число за ограничението:")

    if avg_speed > speed_limit:
        fine = (avg_speed - speed_limit) * 10  # 10 лв за всеки км/ч над
        print(f"Превишили сте ограничението със {avg_speed - speed_limit:.2f} км/ч.")
        print(f"Глобата е: {fine:.2f} лв.")
    else:
        print("Не сте превишили ограничението на скоростта.")

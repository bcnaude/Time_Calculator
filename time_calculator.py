def add_time(start_time, duration_time, weekday=""):

    split_time = start_time.replace(":", " ").split()
    split_duration = duration_time.split(":")

    # Calculate total hours and minutes
    total_hours = int(split_time[0]) + int(split_duration[0])
    total_minutes = int(split_time[1]) + int(split_duration[1])
    total_days = 0

    # If minutes are 60 or more convert them to hours
    if total_minutes > 59:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

    # If hours are 24 or more convert them to days
    if total_hours > 23:
        total_days = total_hours // 24
        total_hours = total_hours % 24

    # Calculate if suffix should be AM or PM
    time_suffix = split_time[2]
    if total_hours % 24 >= 12:
        if time_suffix == "AM":
            time_suffix = "PM"
        else:
            time_suffix = "AM"
            total_days += 1

    # Convert hours from 24 hour format to 12 hour format
    if total_hours > 12:
        total_hours = total_hours - 12

    # Build hour string
    total_hours = str(total_hours)

    # Build minute string
    total_minutes = str(total_minutes).zfill(2)

    # Build day string
    total_days = str(total_days)

    # Build string after the time
    after_the_time = ""
    if int(total_days) == 1:
        after_the_time = " (next day)"
    elif int(total_days) > 1:
        after_the_time = f" ({total_days} days later)"

    # Build return string
    if weekday:
        # Find value of weekday in weekdays and calculate value for the new day of week
        weekday = weekday.lower()
        weekdays = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6,
        }

        if weekday in weekdays:
            new_day_value = (weekdays[weekday] + int(total_days)) % 7
        # Use the new value to find the new weekday key
        weekday = (
            list(weekdays.keys())[list(weekdays.values()).index(new_day_value)]
        ).title()

        new_time = (
            f"{total_hours}:{total_minutes} {time_suffix}, {weekday}{after_the_time}"
        )
    else:
        new_time = f"{total_hours}:{total_minutes} {time_suffix}{after_the_time}"

    return new_time


# print(add_time("11:43 PM", "24:20", "tuesday"))

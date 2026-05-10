def minutes_to_full_time_display(minute):
    second = minute * 60
    hour = minute / 60
    output = print(f"{minute} min in sec is {second} and in hour is {hour}")
    return output


minutes_to_full_time_display(30)

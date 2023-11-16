def human_readable_duration(seconds):
    if seconds == 0:
        return "now"
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    years = days // 365
    days %= 365
    readble_time = ""
    time_list = [seconds, minutes, hours, days, years]
    ctr = len(time_list) - time_list.count(0) - 1
    time_dict = {'year':years, 'day':days, 'hour':hours, 'minute':minutes, 'second':seconds}
    for key, value in time_dict.items():
        if value != 0 and value > 1:
            readble_time += f"{value} {key}s"
            if ctr > 1:
                readble_time += ", "
                ctr -= 1
            elif ctr == 1:
                readble_time += " and "
                ctr -= 1
        elif value == 1:
            readble_time += f"{value} {key}"
            if ctr > 1:
                readble_time += ", "
                ctr -= 1
            elif ctr == 1:
                readble_time += " and "
                ctr -= 1
    
    return readble_time

print(human_readable_duration(73253252))
        



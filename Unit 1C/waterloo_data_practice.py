school_data = {}
# to comment a huge section highlight then do ctrl + /
with open ("waterloo-data.csv", "r") as csv_file:
    data = csv_file.readlines()
    columns = data[0]
    other_schools = data[1]
    data = data[2:]
    for line in data:
        current_line = line.replace('\n', '').split(",")
        school_name = current_line[0]
        location = current_line[1]
        school_data[school_name] = {'location':location}
        year_data = current_line[2:]
        i = 0
        for year in range(2017,2023):
            if not year_data[i]:
                school_data[school_name][year] = None
            else:
                school_data[school_name][year] = float(year_data[i])
            i += 1

# for key, value in school_data.items():
#     print(key)
#     print(value)
#     print('-'*10) 

# location_frequency = {}

# for table in school_data.values():
#     current_location = table['location']

#     if current_location in location_frequency:
#         location_frequency[current_location] += 1
#     else:
#         location_frequency[current_location] = 1

# location_tuple = sorted(location_frequency.items(), key=lambda x:x[1], reverse=True)
# for i in location:
#     print(i)

# 2017 Data
data_2017 = {}
for school,data in school_data.items():
    if data[2017]:
        data_2017[school] = data[2017]

# print(data_2022)
worst_2017 = sorted(data_2017.items(), key = lambda x:x[1], reverse = True)

for school, data in worst_2017:
    print(f"{school} had {data}% differential in 2017.")
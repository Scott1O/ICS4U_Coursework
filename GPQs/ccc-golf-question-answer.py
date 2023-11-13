target_dist = int(input())
num_clubs = int(input())
clubs_list = []
for club in range(num_clubs):
    clubs_list.append(int(input()))

dist_list = list(i for i in range(0,target_dist+1))

for dist in range(1, len(dist_list)):
    dist_list[dist] = 5281

for ctr in range(0,len(dist_list)):
    for club in clubs_list:
        travelled = ctr + club
        if travelled <= len(dist_list) - 1:
            if dist_list[travelled] > dist_list[ctr] + 1:
                dist_list[travelled] = dist_list[ctr] + 1

if dist_list[target_dist] == 5281:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {dist_list[target_dist]} strokes.")
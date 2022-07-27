number = int(input())
box = []
for i in range(number):
    get_num = []
    data = input().split(' ')
    name = data.pop(0)
    data = [int(i) for i in data]
    data.sort()
    while data.count(data[0]) != 1 and len(data) > 2:
        data.pop(0)
    get_num.append(name.capitalize())
    get_num.append(data[1])
    box.append(list(get_num))
for i in range(number):
    for k in range(i+1, number):
        if box[k][1] < box[i][1]:
            save = box[i]
            box[i] = box[k]
            box[k] = save
for i in range(number):
    if box[i][1] == box[1][1]:
        print("Name: %s, %s baht" %(box[i][0], box[i][1]))

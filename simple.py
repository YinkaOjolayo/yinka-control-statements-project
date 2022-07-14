for i in range(3):
    print("##########\n##########")
    for j in range(2):
        if(i != 2):
            print("###")

for k in range(10):
    if k <= 5:
        print("#" * k)
    else:
        print("#" * (10 - k))

z_list = ['#', '#', '#', '#', '#', '#', '#']

for l in range(6 , -1, -1):
    if l == 0 or l == 6:
        print('#######')
    else:
        print((' ' * l) + z_list[l] + (' ' * (6 - l)))

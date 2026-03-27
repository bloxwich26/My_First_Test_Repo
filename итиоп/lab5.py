f = open('znach.txt', 'r')
data_file = f.readlines()
f.close()

def counting(x, y):
    if not x:
        return True
    return all(z == y for z in x)

G1 = int(data_file[0].split(':')[1])
G2 = int(data_file[1].split(':')[1])

S1 = int(data_file[2].split(':')[1])
S2 = int(data_file[3].split(':')[1])
S3 = int(data_file[4].split(':')[1])
S4 = int(data_file[5].split(':')[1])
S5 = int(data_file[6].split(':')[1])

Vl1 = int(data_file[7].split(':')[1])
Vl2 = int(data_file[8].split(':')[1])

Kl1 = int(data_file[9].split(':')[1])
Kl2 = int(data_file[10].split(':')[1])
Kl3 = int(data_file[11].split(':')[1])

line1 = [G1, S1, Vl1, S2]
line2 = [G2, S5, Kl2, S3, Kl1, S2]
line3 = [G2, S5, Vl2, S4, Kl3, S3, Kl1, S2]
check = 1

if (counting(line1, check) and counting(line2, check) and counting(line3, check)) or (counting(line1, check) and counting(line2, check)) or (counting(line1, check) and counting(line3, check)):
    print('Питание от обоих генераторов')
elif (counting(line2, check) and counting(line3, check)) or counting(line2, check) or counting(line3, check):
    print('Питание от второго генератора')
elif counting(line1, check):
    print('Питание от первого генератора')
else:
    print('Нет питания') 

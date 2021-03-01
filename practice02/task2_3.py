def f23(data):
    k = 0
    for i in data:
        data[k] = list(dict.fromkeys([i.replace('/', '-') for i in i if i]))
        data[k][0] = data[k][0].split('[at]')[-1]
        temp = data[k][-1].split('-')
        temp.append(temp[-1][2:4])
        temp[-2] = temp[-2][:2]
        #print(temp)
        data[k][-1] = '({}) {}-{}-{}'.format(temp[0], temp[1], temp[2], temp[3])
        k += 1
    
    i = 0
    k = 0
    while i < len(data):
        k = i+1 
        while k < len(data):
            if data[i] == data[k]:
                del data[k]
            k += 1
        i += 1
    data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    return data


print(f23([
    [None, 'grigorij79[at]gmail.com', '21/09/00', None, '21/09/00', '051-375-5880'],
    [None, 'gadasuk60[at]mail.ru', '10/01/03', None, '10/01/03', '987-676-6223'],
    [None, 'aromir49[at]gmail.com', '02/11/01', None, '02/11/01', '555-742-9615'],
    [None, 'aromir49[at]gmail.com', '02/11/01', None, '02/11/01', '555-742-9615'],
    [None, 'anatolij87[at]mail.ru', '22/09/03', None, '22/09/03', '837-498-5263']
    ]))
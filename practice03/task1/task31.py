from struct import unpack

def A(data, initial):
    start = initial
    result = {}
    size, addr = unpack('>2I', data[start:start + 8])
    start += 8

    result['A1'] = list(unpack('>'+str(size)+'b', data[addr:addr+size]))
    size, addr = unpack('>2H', data[start:start+4])
    start += 4
    
    result['A2'] = []
    for i in range(0, size):
        result['A2'].append(B(addr, data))
        addr +=8
    
    addr = unpack('>I', data[start:start+4])
    start += 4
    result['A3'] = C(addr[0], data)
    
    result['A4'], result['A5'], result['A6'], result['A7'] = unpack('>iiBL', data[start:start + 13])
    start += 13
    
    addr = unpack('>H', data[start:start+2])[0]
    print(addr)
    result['A8'] = D(addr, data)
    print(result)
    

def B(start, data):
    result = {}
    # first, second = unpack('>2i', data[start:start + 8])
    # result['B1'] = first
    # result['B2'] = second
    result['B1'], result['B2'] = unpack('>2i', data[start:start + 8])
    return result


def C(start, data):
    result = {} 
    result['C1'], result['C2'] = unpack('>2i', data[start:start + 8])
    return result


def D(start, data):
    result = {}
    result['D1'], result['D2'] = unpack('>HQ', data[start:start + 10])
    start+=10
    result['D3'] = list(unpack('>3I', data[start:start + 12]))
    start += 12
    result['D4'] = unpack('>i', data[start:start + 4])
    start+=4
    result['D5'] = list(unpack('>5f', data[start:start + 20]))
    start += 20
    result['D6'] = unpack('>Q', data[start:start + 8])[0]
    return result


def f31(data):
    pattern_to_match = b'\xb9\x4b\x48\x4b\x54'
    start = data.find(pattern_to_match) + len(pattern_to_match)
    return A(data, start)
    
    


f31(b'\xb9KHKT\x00\x00\x00\x06\x00\x00\x00$\x00\x02\x00*\x00\x00\x00:{iX\x95\x02nD'
b'\xbdzlb|h\x00B\xe0\xbb\xbak\x94\xc4\xf7\xaah\xc10(\xab\xd1\xb5\xf9\x1dT\xa2v'
b'Se4\x06J\x0e\xce\xdf\x9f~\xe2\xe0M\x05\x0bs\x0f&q\xe4Az\x987\xc7\xf9\xa4K'
b'o\x9e\xe8\x97/\xa8\x18\xec>\xe4\x96s?R\x84G\xbfI\xe3\xfb?\x02\xd1\x17?fV\x1f'
b'\xa4(\x94\xec\xc1\xd5\x01\xc6')
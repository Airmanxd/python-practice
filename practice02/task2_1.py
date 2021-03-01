def f21(data):
    result = {
        2019 : 7,
        2003 : {
            2015 : 10,
            2004 : {
                1970 : 9,
                2015 : 8
            }
        },
        1966 : {
            'ncl' : 6,
            'twig' : {
                1970 : {
                    'org' : 3,
                    'uno' : 4,
                    'haxe' : 5
                },
                2015 : {
                    'org' : 1,
                    'uno' : 2,
                    'haxe' : 3
                }
            }
        }
    }
    indices = [data[3], [data[4], data[0]], data[2], data[1]]
    for i in indices:
        if type(i) is list:
            if type(list(result.keys())[0]) is int:
                i = i[1]
            else:
                i = i[0]
        result = result[i]
        if type(result) is int:
            return result
print(f21([2015, 'uno', 1970, 2003, 'twig']))
print(f21([2004, 'org', 1970, 2019, 'twig']))


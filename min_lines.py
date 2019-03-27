import re, itertools
with open('calcmemory')as file:((print(file.read())or 1)and all(print('Result:',str(print(sum([int(re.sub('\s','',i))for i in re.findall('(?:^[\-]?[0-9]+)|(?:[\+\-]\s*[0-9]+)',input('Calc>>>'))]),file=open('calcmemory', 'a')))[:0],file.readline())or 1 for _ in itertools.repeat(1)))

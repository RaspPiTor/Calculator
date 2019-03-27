import re #used for parsing input
with open('calcmemory') as file: # open calc history
    print(file.read()) # print current history
    while 1:print('Result:', #print result
                  # extract numbers and signs from input, strip whitespace
                  # then convert to ints, and finally apply sum, then print to
                  # a file to store result, then read last line of file and print
                  str(print(sum([int(re.sub('\s', '', i)) for i in re.findall('(?:^[\-]?[0-9]+)|(?:[\+\-]\s*[0-9]+)', input('Calc>>>'))]), file=open('calcmemory', 'a')))[:0],
                  file.readline())

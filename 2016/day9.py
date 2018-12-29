data = open('day9.txt','r').read()
decompressed1 = ''

i = 0
while (i < len(data)):

    if (data[i] == '('):
        end = data.index(')',i)
        length_time = data[i+1:end].split('x')
        length,times = int(length_time[0]),int(length_time[1])
        start_msg = end + 1
        skipto = start_msg + (length)
        decompressed1 += data[start_msg:start_msg + length] * times
        i = skipto 
       
    else:
        decompressed1 += data[i]
        i += 1


print "Part I"
print len(decompressed1)


def decompress(data):
    sub_decompressed_len = 0
    i = 0
    while (i < len(data)):

        if (data[i] == '('):
            end = data.index(')',i)
            length_time = data[i+1:end].split('x')
            length,times = int(length_time[0]),int(length_time[1])
            start_msg = end + 1
            skipto = start_msg + (length)
            sub_decompressed_len += decompress(data[start_msg:start_msg + length]) * times
            i = skipto 
       
        else:
            sub_decompressed_len += 1
            i += 1
    return sub_decompressed_len

print 'Part II'
print decompress(data)
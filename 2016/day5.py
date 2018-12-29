import time
import md5
import sys
start_time = time.time()
input_ = 'ugkcyxxp'

print 'Part I'
i = 0
password = ''
password2 = ['-'] * 8
recorded = 0
while(True):
    m = md5.new()
    m.update(input_ + str(i))
    hash = m.hexdigest()
    if hash[0:5] == '00000':
        if len(password) < 8:
            password += hash[5]
            sys.stdout.write(hash[5])
        
        try:
            pos = int(hash[5])
            if (password2[pos] == '-'):
                password2[pos] = hash[6]
                recorded += 1
        except:
            pass
        if recorded == 8:
            break
        
    i += 1

sys.stdout.write('\n')

print 'Part II'

print ''.join(password2)
total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."



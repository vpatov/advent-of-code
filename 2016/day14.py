# It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
# One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

from hashlib import md5

def get_hash(x):
    return md5(x).hexdigest()

salt = 'ihaygndm'
salt = 'abc'
index = 0

triplets = {}
quintuplets = {}
keys = []

def get_nlet(digest,index):
    len_nlet = 1
    prev = digest[0]
    for i in range(1,len(digest) - 5):
        if digest[i] == prev:
            prev = digest[i]
            len_nlet += 1
        else:
            if len_nlet == 3:
                triplets[index] = prev
            elif len_nlet == 5:
                quintuplets[index] = prev
                for ind in triplets:
                    if triplets[ind] == prev and index - 1000 < ind:
                        keys.append(get_hash(salt + str(ind)))
                        print(keys,index)
                        exit()
            len_nlet = 1
            prev = digest[i]




while (len(keys) < 64):
    cur_hash = get_hash(salt + str(index))
    if index == 18 or index == 39:
        print(cur_hash)
    if index == 1039:
        break
    get_nlet(cur_hash,index)
    index += 1
    
print(keys)
print(index)


print(get_hash(salt + str(index)))
from collections import Counter
import operator

rooms = open('day4.txt','r').read().split('\n')

def is_real(room):
    cnt = Counter()
    encrypted = room[:room.index('[') - 3]
    sector_id = int(room[room.index('[') - 3 : room.index('[')])
    checksum = room[room.index('[') + 1: -1]
    for ch in encrypted:
        if ch == '-':
            continue
        if ch.isalpha():
            cnt[ch] += 1
    i = 0
    letters = sorted(cnt.items(), key=lambda x: ((x[1] * 100) + ord('z') - ord(x[0])),reverse=True)

    while (i < 5 and i < len(cnt)):
        if letters[i][0] != checksum[i]:
            return False
        i+=1
    return sector_id


def decrypt_room(room):
    encrypted = room[:room.index('[') - 3]
    sector_id = int(room[room.index('[') - 3 : room.index('[')])
    decrypted = []
    for ch in encrypted:
        if ch == '-':
            decrypted.append(' ')
            continue
        decrypted.append(chr((((ord(ch) - ord('a')) + sector_id) % 26) + ord('a')))

    return ''.join(decrypted),sector_id

print 'Part I'
real_rooms = filter(is_real,rooms)
print sum(is_real(room) for room in real_rooms)

print 'Part II'
decrypted_rooms = [decrypt_room(room) for room in real_rooms]

for room_name,sector_id in decrypted_rooms:
    if 'northpole' in room_name or 'north pole' in room_name:
        print sector_id





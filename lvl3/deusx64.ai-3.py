import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

dct = ["memory", 
    "address", 
    "randomization", 
    "hexadecimal", 
    "system",
    "intelligence",
    "sandbox", 
    "cyber",
    "cybernetic",
    "architecture"]
    
mtrx = []

def iter_mtrx(w):
    for y in range (0, 20):
        for x in range (0, 20):
            r = check_word(w, x, y)
            if r[0]:
                return (True, x, y, r[1], r[2])
    return (False, 0)

def check_word (w, x, y):
    r = (False, 0)
    try:
        for i in range(0, len(w)):
            print 
            if w[i] != mtrx[y][x+i].lower():
                break
        if i==len(w)-1:
            return (True, x+i, y)
    except:
        pass
    
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y][x-i].lower():
                break
        if i==len(w)-1:
            return (True, x-i, y)
    except:
        pass
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y+i][x].lower():
                break
        if i==len(w)-1:
            return (True, x, y+i)
    except:
        pass
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y-i][x].lower():
                break
        if i==len(w)-1:
            return (True, x, y-i)
    except:
        pass
    
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y-i][x-i].lower():
                break
        if i==len(w)-1:
            return (True, x-i, y-i)
    except:
        pass
    
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y+i][x-i].lower():
                break
        if i==len(w)-1:
            return (True, x-i, y+i)
    except:
        pass
    
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y-i][x+i].lower():
                break
        if i==len(w)-1:
            return (True, x+i, y-i)
    except:
        pass
    
    try:
        for i in range(0, len(w)):
            if w[i] != mtrx[y+i][x+i].lower():
                break
        if i==len(w)-1:
            return (True, x+i, y+i)
    except:
        pass
    return (False, 0)
    
p = interact.Process()
data = p.readuntil('Press enter to continue...')
p.sendline('\n')
data = p.readuntil('+-----------------------------------------+')


data = p.readuntil('+-----------------------------------------+')
p.sendline('1')

data = p.readuntil('+-----------------------------------------+')
p.readline()

for i in range (0, 20):
    l = p.readline()
    print (l)
    mtrx.append (l[27:66].split(' '))


for w in dct:
    
    r = iter_mtrx(w)
    if r[0]:
        p.readuntil('Provide Starting x,y Coordinate:')
        print (str(r[1])+','+str(r[2]))
        p.sendline(str(r[1])+','+str(r[2]))
        p.readuntil('Provide Ending x,y Coordinate:')
        p.sendline(str(r[3])+','+str(r[4]))
        p.readuntil('Continue Playing (y/n)')
        #if w == dct[-1]:
        #    p.sendline('n')
        #else:
        p.sendline('y')
    else:
        print (w, 'not found')

p.interactive()
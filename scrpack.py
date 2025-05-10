import struct, os
game = 'Love Split ～5番目の季節～'
folder = './RIO\\'
newarc = 'rio.GBK'
def rot_right(byte, bits):
    """对单个字节右旋指定的位数"""
    return (byte >> bits) | ((byte << (8 - bits)) & 0xFF)

if not os.path.exists(folder):
    os.mkdir(folder)
files = os.listdir(folder)
filecont = len(files)
f = open(newarc, 'wb')
h = bytes.fromhex('01 00 00 00 53 43 52 00')
f.write(h)
f.write(struct.pack('i', filecont))
h = bytes.fromhex('10 00 00 00')
f.write(h)
pos = 16+filecont*17
data = b''
for file in files:
    size = os.stat(folder + file).st_size
    file = file.replace('.scr','').upper()
    nl = len(file.encode('CP932'))
    null = (9 - nl) * b'\x00'
    data = data + file.encode('cp932')
    data = data + null
    data = data + struct.pack('i', size)
    data = data + struct.pack('i', pos)
    pos = pos + size + 0
f.write(data)
for file in files:
    f1 = open(folder + file, 'rb')
    b = f1.read()
    f1.close()
    for a in b:
        a = rot_right(a,6)
        a = struct.pack('B',a)
        f.write(a)

f.close()

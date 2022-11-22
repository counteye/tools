import os
import os.path

def incrementByteArray(arr, count):
    j = 0
    fakeElements = []
    for a in arr:
        fakeElements.append(0)
    finalArr = bytearray(fakeElements)
    for byte in arr:
        for i in range(count):
            if byte == 255:
                byte = 0
            byte += 1
        finalArr[j] = byte
        j += 1
    return finalArr

name = input("AXfile name: ") or "Container"
mypath = "./contents/"

files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

wf = open(name + ".AX", "wb")
# header
wf.write("AXfile00".encode("ascii"))
wf.write(b'\x20\x20\x00')
# files
for f in files:
    a = open(mypath + f, "rb")
    wf.write("C:/axfile/contents/".encode("ascii") + f.encode("ascii") + b'\x00\x00')
    while (bt := a.read(60)):
        wf.write(incrementByteArray(bt, 5))
        wf.write(b'\x00\x20\x00')
    a.close()
    wf.write(b'\x00\x00\x00\x00')
wf.close()

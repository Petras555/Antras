# a ='36895150566'
# print(a[11])

def asm_kodas(asm):
    if len(asm) != 11:
        return False
    if asm[0] not in range(3,7):
        return False
    if asm[3:4] > 12:
        return
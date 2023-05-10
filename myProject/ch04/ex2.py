a = ord('a')

print(a)

a=ord('A')
print(a)

mask = 0x0F
print("%x & %x = %x" %(a, mask,a&mask))
print("%x | %x = %x" %(a, mask,a|mask))

mask = ord('a')-ord('A')
# print(mask) # 32

b = a^mask
print("%c ^ %d = %c" %(a,mask,b))   #  %c = 문자
a = b^mask
print("%c ^ %d = %c" %(b,mask,a))


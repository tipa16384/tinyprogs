for i in range(256):
    print(f"{i} \033[38;5;{i}mHello, World!\033[0m")

for i in range(16):
    print(f"{i} \033[{i}mHello, World!\033[0m")

for i in range(1,81):
    # print the tens digit
    print (''.join(str(int(i/10))), end='')
print ()
for i in range(1,81):
    # print the tens digit
    print (''.join(str(int(i%10))), end='')
print ()

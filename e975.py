password = input().lower()
l = ord('l')
o = ord('o')
v = ord('v')
e = ord('e')
for i in range(len(password)-3):
    if (ord(password[i]) - ord(password[i+1])) % 26 == (l-o) % 26:
        if (ord(password[i+1]) - ord(password[i+2])) % 26 == (o-v) % 26:
            if (ord(password[i+2]) - ord(password[i+3])) % 26 == (v-e) % 26:
                print((l - ord(password[i])) % 26)
                break    

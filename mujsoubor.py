aaa = 15
bbb = 10

print("aaa = \t", aaa, "\tbbb = \t", bbb)

if aaa < bbb:
    print(" aaa je mensi nez bbb")
else:
    print("bbb je mensi nez aaa")
    
i = 1
while i <= aaa:
    print(i)
    i += 1  # Zvýšíme hodnotu i o 1
    
odpoved = ""
while odpoved != "ano":
    odpoved = input("zadejte 'ano' pro pokracovani")
print("pokracujeme")

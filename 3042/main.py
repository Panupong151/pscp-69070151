"""โปรแกรมหาค่าที่หาร10ลงตัว"""
number = int(input())
list = []
for i in range(number,-1,-1):
    if i % 10 == 0:
        list.append(i)
print(*list)

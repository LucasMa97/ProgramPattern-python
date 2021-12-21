# type use
age = 24
money = 10.3
name = "LucasMa"

print("age:" , age)
age = name + age
print("new age:", age)

# base container
l1 = [age, money, name]
l2 = [23, 100, "wang"]
print("链表1", l1)
print("第二个元素：", l1[1])
l1[2] = "ma"
l1.append("huawei")
print("添加修改元素后：", l1)
l3 = l1 + l2
print("合并链表：", l3)
print("指定输出2-3：", l3[1:2])

# tuple = read-only list
l1 = (age, money, name)
l2 = [23, 100, "wang"]
print("链表1", l1)
print("第二个元素：", l1[1])
l1[2] = "ma"
l1.append("huawei")
print("添加修改元素后：", l1)
l3 = l1 + l2
print("合并链表：", l3)
print("指定输出2-3：", l3[1:2])

name = "banana" # maybe change this to explore how looping works

# a = name[0:1]
# b = name[0:2]
# c = name[0:3]
# d = name[0:4]
# e = name[0:5]
# f = name[0:6]

# print a, b, c, d, e, f



# a = name[0:3]
# b = name[3:]
# c = a + b
# print c

# answer = name[0:3]
# answer += name[3:6]

# answer = name[0:3]
# answer += name[3:]


# print("i")
# i = 0
# while i < len(name):
# 	print(i)
# 	i += 1
# print("Final value of i:", i)

# print("i")
# i = len(name)
# while i > 0:
# 	print(i)
# 	i -= 1
# print("Final value of i:", i)

# print("i")
# i = 0
# for x in name:
# 	i += 1
# 	print(i)
# print("Final value of i:", i)

# print("i", "j")
# i = 0
# j = 0
# for x in name:
# 	if x == "a": # maybe change this to explore how looping works
# 		j += 1
# 	i += 1
# 	print(i, j, x)


print("i", "j", "c")
i = 0
c = 0
for x in name:
	j = 0
	while j < len(name):
		c += 1
		j += 1
		print(i, j, c)
	i += 1

print("Final", i, j, c)








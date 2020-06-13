all_info = [('1', 'faruk', 26), ('2', 'nahid', 25), ('3', 'araf', 24), ('4', 'forhad', 23)]
unzip_all_info = list(zip(*all_info))
print(unzip_all_info)

serial = unzip_all_info[0]
name = unzip_all_info[1]
age = unzip_all_info[2]

print(serial)
print(name)
print(age)
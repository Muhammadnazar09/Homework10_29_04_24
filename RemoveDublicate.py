# my_list=[{"Green":"##008000"},{"Black":"#000000"},{"Blue":"#0000FF"},{"Green":"##008000"}]
# new_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

my_list=[{"Green":"##008000"},{"Black":"#000000"},{"Blue":"#0000FF"},{"Green":"##008000"}]
new_lest = []
for i in range(len(my_list)):
    if my_list[i] not in my_list[i+1:]:
        new_lest.append(my_list[i])
print(new_lest)

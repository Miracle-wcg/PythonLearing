# # -*- coding: utf-8 -*-
# print(45678 + 0x12fd2);
# print('Learn Python in imooc');
# print(100 < 99);
# print(0xff == 255);
# print (u'''静夜思
# 床前明月光，
# 疑是地上霜，
# 举头望明月，
# 低头思故乡.''');
sum = 0;
x = 1;
n = 1;
while True:
    sum += x;
    n += 1;
    x = 2**n;
    if n > 19:
        break
print(sum);

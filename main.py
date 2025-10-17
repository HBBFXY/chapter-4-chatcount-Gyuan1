# 初始化四类字符的计数器
letter_num = 0
digit_num = 0
space_num = 0
other_num = 0
# 获取用户输入的一行字符
input_str = input()
# 遍历每个字符进行统计
for char in input_str:
    if char.isalpha():  # 判断是否为英文字符（字母）
        letter_num += 1
    elif char.isdigit():  # 判断是否为数字
        digit_num += 1
    elif char.isspace():  # 判断是否为空格
        space_num += 1
    else:  # 其他字符
        other_num += 1

# 按要求格式输出结果
print(f"英文字符: {letter_num}")
print(f"数字: {digit_num}")
print(f"空格: {space_num}")
print(f"其他字符: {other_num}")input_str = input()
english_count = 0
digit_count = 0
space_count = 0
other_count = 0
for char in input_str:
    if char.isalpha():
        english_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1
print(f"英文字符:{english_count}")
print(f"数字: {digit_count}")
print(f"空格:{space_count}")
print(f"其他字符:{other_count}")

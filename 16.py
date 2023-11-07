user_input = input("请输入一个整数：")
try:
    user_integer = int(user_input)
    print("您输入的整数是：", user_integer)
except ValueError:
    print("无法将输入转换为整数。")
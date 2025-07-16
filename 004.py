age = input("你的年龄是？")
age = int(age)
if age >= 18:
    num1 = age - 18
    print(f"您已成年，请补票{ num1 }")
else:
    print("您已免票")
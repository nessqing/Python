# 每年固定存一筆錢給孩子, n 年後總共會多少錢
total = 24000
perYear = 12000 * 2 ## 父母親
rate = 1.6 / 100
year_input = int(input())
for i in range(1,year_input+1):
    if i > 1:
        total += perYear + total * rate
    print(f"第 {i:2} 年, 總共 ${total:.2f}")

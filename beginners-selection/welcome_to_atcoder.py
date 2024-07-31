a = int(input()) # 与えられた値の1行目のint型のものをaに格納
b, c = map(int, input().split()) #与えられた値の2行目のint型をb, cに格納
s = input() #与えられた値の3行目のStringをsに格納

print("{} {}".format(a+b+c, s))
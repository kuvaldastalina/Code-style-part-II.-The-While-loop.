mu_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0

while x < len(mu_list):
    if mu_list[x] > 0:
      print(mu_list[x])
    elif 0 > mu_list[x]:
    # print(mu_list[x])
      break
    x += 1


# 4x - 5y + 33 = 0
# 5y = 4x + 33
# y = (4/5)x + 33/5
slope1 = 4 / 5

# 20x - 9y - 107 = 0
# 9y = 20x - 107
# y = (20/9)x - 107/9
slope2 = 9 / 20

sigma_x = 3 ** 2
sigma_y = slope1 * sigma_x / slope2

print(int(sigma_y))
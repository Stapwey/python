import math


def main(n):
    res = (0.01 - 71 * n[0] * n[0] - 69 * (n[7]) ** 3)**2
    res = res + (0.01 - 71 * n[0] * n[0] - 69 * (n[7]) ** 3)**2
    res = res + (0.01 - 71 * n[0] * n[0] - 69 * (n[7]) ** 3)**2
    res = res + (0.01 - 71 * n[1] * n[1] - 69 * (n[6]) ** 3)**2
    res = res + (0.01 - 71 * n[1] * n[1] - 69 * (n[6]) ** 3)**2
    res = res + (0.01 - 71 * n[1] * n[1] - 69 * (n[6]) ** 3)**2
    res = res + (0.01 - 71 * n[2] * n[2] - 69 * (n[5]) ** 3)**2
    res = res + (0.01 - 71 * n[2] * n[2] - 69 * (n[5]) ** 3)**2
    return 29 * res


print(main([-0.21, -0.97, 0.34, -0.03, -0.01, 0.86, -0.65, 0.65]))

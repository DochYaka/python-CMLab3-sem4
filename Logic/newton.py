def newton(x, x_points, coef):
    n = len(coef)
    result = coef[0]
    product = 1

    for i in range(1, n):
        product *= (x - x_points[i-1])
        result += coef[i] * product

    return result

def divided_differences(x_points, y_points):
    n = len(x_points)
    coef = y_points.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x_points[i] - x_points[i-j])

    return coef
# 11. NEWTON FORWARD DIFFERENCE
def newton_forward(x_data, y_data, x):
    n = len(x_data); h = x_data[1] - x_data[0]
    p = (x - x_data[0]) / h
    delta = [y_data[:]]
    for j in range(1, n):
        delta.append([delta[-1][i+1] - delta[-1][i] for i in range(len(delta[-1])-1)])
    y = delta[0][0]; term = 1
    for i in range(1, n):
        term *= (p - (i-1)) / i
        y += term * delta[i][0]
    return y
x_data = [0,1,2,3]; y_data = [1,2,4,8]
print(newton_forward(x_data, y_data, 1.5))
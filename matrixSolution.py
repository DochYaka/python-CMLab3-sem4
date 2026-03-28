def gauss_with_pivot(A, b):
    n = len(A)

    A = [row[:] for row in A]
    b = b[:]

    col_perm = list(range(n))

    for k in range(n):
        max_val = 0
        max_row = k
        max_col = k

        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    max_row = i
                    max_col = j

        A[k], A[max_row] = A[max_row], A[k]
        b[k], b[max_row] = b[max_row], b[k]

        for i in range(n):
            A[i][k], A[i][max_col] = A[i][max_col], A[i][k]

        col_perm[k], col_perm[max_col] = col_perm[max_col], col_perm[k]

        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]

            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

            b[i] -= factor * b[k]

    x = [0] * n

    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i][j] * x[j]

        x[i] = (b[i] - s) / A[i][i]

    x_final = [0] * n
    for i in range(n):
        x_final[col_perm[i]] = x[i]

    return x_final
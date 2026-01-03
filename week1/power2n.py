n = 25

# 方法 a
def power2n_a(n):
    return 2**n

print("方法一", power2n_a(n))

# 方法 b：用遞迴 （慢）
def power2n_b(n):
    if n == 0:
        return 1
    return power2n_b(n-1) + power2n_b(n-1)

print("方法二",power2n_b(n))

# 方法 c：用遞迴 (快)
def power2n_c(n):
    if n == 0:
        return 1
    return 2*power2n_c(n-1)

print("方法三", power2n_c(n))

# 方法 d：用遞迴+查表
num = [None]*10000
num[0] = 1
def power2n_d(n):
    if n < 0:
        raise
    if not num[n] is None:
        return num[n]
    
    num[n] = power2n_d(n-1) + power2n_d(n-1)

    return num[n]

print("方法四",power2n_d(n))
        
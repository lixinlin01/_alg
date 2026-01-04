import random

def monte_carlo_n_dim(f, bounds, iterations=100000):
    """
    n 維蒙地卡羅積分實作
    :param f: 目標函數 f([x1, x2, ..., xn])
    :param bounds: 積分範圍 [(a1, b1), (a2, b2), ..., (an, bn)]
    :param iterations: 隨機取樣次數 (N)
    """
    n = len(bounds)
    
    # 1. 計算超矩形的總超體積 (Volume)
    total_volume = 1.0
    for a, b in bounds:
        total_volume *= (b - a)
    
    total_sum = 0.0
    
    # 2. 開始隨機取樣
    for _ in range(iterations):
        # 在每個維度的範圍內生成一個隨機座標
        random_point = [random.uniform(a, b) for a, b in bounds]
        
        # 加總函數值
        total_sum += f(random_point)
    
    # 3. 計算平均值並乘以總體積
    average_value = total_sum / iterations
    return total_volume * average_value

# --- 測試範例 ---

# 測試：五維積分 f(x1,x2,x3,x4,x5) = x1 + x2 + x3 + x4 + x5
# 範圍皆為 [0, 1]，理論值應為 0.5 * 5 = 2.5
test_f5 = lambda p: sum(p)
bounds_5d = [(0, 1)] * 5

# 執行積分
result = monte_carlo_n_dim(test_f5, bounds_5d, iterations=500000)
print(f"5D 蒙地卡羅積分結果: {result:.6f} (理論值: 2.5)")

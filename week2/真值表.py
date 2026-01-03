import itertools
import string

def print_truth_table(n):
    # 自動取 A, B, C... 作為變數名稱
    headers = list(string.ascii_uppercase[:n])
    
    print(" | ".join(headers))
    print("-" * (n * 6))
    
    # 產生所有組合
    for row in itertools.product([1, 0], repeat=n):
        print(" | ".join(map(str, row)))

# 產生 4 個變數的真值表輸入
print_truth_table(4)

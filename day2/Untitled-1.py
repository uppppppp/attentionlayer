def longest_palindrome(s):
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]  # 初始化二维动态规划数组
    print(dp)
    start = 0  # 记录最长回文子串的起始位置
    max_length = 1  # 记录最长回文子串的长度
    
    # 所有长度为1的子串都是回文
    for i in range(n):
        dp[i][i] = True
    
    # 检查长度为2的子串
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # 检查长度大于2的子串
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

# 示例用法
s = "babad"
result = longest_palindrome(s)
print(result)  # 输出 "bab" 或 "aba"

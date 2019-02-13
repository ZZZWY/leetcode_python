"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    n, l = map(int, line.split())
    if l < n/2:
        if l % 2 != 1:
            if (n-l) % 2 != 0:
                return "Impossible"
            else:
                return n-l
        else:
            return l
    else:
        if (n-l) % 2 != 0:
            if l % 2 != 1:
                return "Impossible"
            else:
                return l
        else:
            return n-l

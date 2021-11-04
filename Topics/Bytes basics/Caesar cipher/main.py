s = input().encode('utf-8')  # output is bytes type
s_2 = bytes([i + 1 for i in s])
s_3 = s_2.decode('utf-8')
print(s_3)

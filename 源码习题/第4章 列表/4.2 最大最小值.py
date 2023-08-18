pool = []
while True:
    input_number = input('输入数字（空结束）:')
    if input_number == '':
        break
    pool.append(float(input_number))
print("输入了%d个数字"%len(pool))
print("最大值：%f，最小值%f"%(max(pool),min(pool)))
# 读取 csv/txt 文件
with open(r"test_file.csv", "r") as file:
    for line in file:
        print(line)
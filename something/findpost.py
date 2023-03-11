import os
# 指定文件夹
folder_path = '/root/tmp/111/Vuze_3.1.1.0_source'
# 指定后缀
suffix = '.java'
# 初始化行数
lines = 0
# 遍历文件夹下所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 判断是否为指定后缀的文件
        if os.path.splitext(file)[1] == suffix:
            # 将文件路径拼接成绝对路径
            filename = os.path.join(root, file)
            # 遍历文件并统计行数
            try:
                for line in open(filename, encoding='utf-8'):
                    lines += 1
            except:
                continue

print(f"Total lines:{lines}")

# 或者
# from glob import glob
# import os
# target_dir = '/root/tmp'
# suffix = '*.py'
# lines = 0
# filenames = [filename for file in os.walk(target_dir) for filename in glob(os.path.join(file[0], suffix))]
# for filename in filenames:
#     for line in open(filename, encoding='utf-8'):
#         lines += 1
# print(lines)


# 输入参数
# import argparse
# parser = argparse.ArgumentParser(description='Test for argparse')
# parser.add_argument('--target_dir', '-dir', help='文件目录', required=True)
# parser.add_argument('--suffix', '-sfx', help='后缀类型', default="py")
# args = parser.parse_args()
# target_dir = args.target_dir
# suffix = "*." + args.suffix

# import sys
# target_dir, suffix = sys.argv[1:3]
import os

# 导入xlsxwriter库，用于创建excel
import xlsxwriter

# 设置保存路径
script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
project_root = os.path.dirname(os.path.dirname(script_dir))  # 获取项目根目录
save_folder = os.path.join(project_root, "demo")
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
file_path = os.path.join(save_folder, "demo.xlsx")

# 创建一个名为demo.xlsx的工作薄
workbook = xlsxwriter.Workbook(file_path)

# 在工作薄中添加一个名为sheet1的工作表
worksheet = workbook.add_worksheet(name='sheet1')

# 在B1单元格写入数值500
worksheet.write("B1",500)

# 在第0行第1列等价于B1单元格写入数值600
worksheet.write(0,1,600)

# 在B2单元格写入公式，计算B1单元格数值的平方
worksheet.write_formula("B2","{=SUM(B1*B1)}")

# 设置A列的宽度为40
worksheet.set_column("A:A",40)

# 创建两个格式对象，分别设置缩进级别为1和2
indent1 = workbook.add_format({'indent': 1}) 
indent2 = workbook.add_format({'indent': 2})

# 使用不同的缩进格式在A1和A2单元格写入文本，并设置相应的缩进
worksheet.write("A1","这是缩进一格", indent1)
worksheet.write("A2","这是缩进2格", indent2)

# 关闭并保存工作薄
workbook.close()
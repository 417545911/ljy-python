import os

# 导入xlsxwriter库，用于创建excel
import xlsxwriter

# 设置保存路径
script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
project_root = os.path.dirname(os.path.dirname(script_dir))  # 获取项目根目录
save_folder = os.path.join(project_root, "demo")
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
file_path = os.path.join(save_folder, "demo1.xlsx")

# 创建一个名为demo1.xlsx的工作薄
workbook = xlsxwriter.Workbook(file_path)

# 在工作薄中添加一个名为sheet1的工作表
worksheet = workbook.add_worksheet(name='sheet1')

# 定义表格的表头信息以及相关数据
headings = ["Number","Batch 1","Batch 2"]
data = [
    [2,3,4,5,6,7],
    [40,40,50,30,25,50],
    [30,25,30,10,5,10]
]
# 创建一个加粗格式样式以突出显示表头
bold = workbook.add_format({"bold": 1})
# 将表头信息写入到第一行（从A1开始）
worksheet.write_row("A1", headings, bold)

worksheet.write_column("A2", data[0])
worksheet.write_column("B2", data[1])
worksheet.write_column("C2", data[2])


# 关闭并保存工作薄
workbook.close()
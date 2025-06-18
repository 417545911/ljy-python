import os

# 显示条件格式图
from openpyxl import Workbook
from openpyxl.formatting.rule import DataBarRule
from openpyxl.styles.colors import Color

# 设置保存路径
script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
project_root = os.path.dirname(os.path.dirname(script_dir))  # 获取项目根目录
save_folder = os.path.join(project_root, "demo")
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
file_path = os.path.join(save_folder, "demo2.xlsx")

# 1. 创建一个新的Excel工作薄
workbook = Workbook()
# 2. 选择或获取工作薄的第一个工作表，并设置其标题
worksheet = workbook.active
worksheet.title = 'Color Scale Test'
# 3. 假设有如下一列测试数据
data = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]
# 4. 将测试数据写入Excel工作表的A列，从第二行开始（Excel表格的第一行默认为表头）
for row_index, value in enumerate(data, 1):
    worksheet.cell(row=row_index, column=1, value=value)
# 5. 定义数据所在的区域，即A2到A10这一列（由于enumerate()）从1开始
data_range = 'A1:A10'  # 直接定义范围字符串
# 6. 创建一个DataBarRule实例，用于在指定范围内应用数据条（颜色条）条件格式
rule = DataBarRule(
    start_type="min", # 数据条的起点基于该列的最小值
    end_type="max", #  数据条的终点基于该列的最大值
    color=Color(rgb='00FF00'), # 数据条的颜色为绿色
    showValue=True, # 显示数据条旁边的实际数值
    minLength=None, # 数据条的最小长度将由程序自动计算，保持默认值
    maxLength=None  # 数据条的最大长度将由
)
# 7. 将数据条条件格式规则应用到指定的单元格区域
worksheet.conditional_formatting.add('A1:A10', rule) # 将规则应用到A1到A10这一列
# 8. 保存已应用条件格式的工作薄至Excel文件
workbook.save(file_path) 
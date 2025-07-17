
log_file = 'logs/console.20250626.log'
keyword = 'sxzq机器人'

count = 0
# TODO: 测试TODO
with open(log_file,"r",encoding='utf-8') as f:
    for line in f:
        if keyword in line:
            print(line.strip())
            count += 1

print(f"\n共找到 {count} 行包含'{keyword}'的日志")
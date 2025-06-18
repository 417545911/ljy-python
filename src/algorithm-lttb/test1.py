import numpy  as np

def my_lttb_downsample(data, threshold):

    n = len(data)
    if n <= threshold:
        return data
    

    # 确定每个桶的边界
    m = threshold - 2  # 中间需要选的桶数
    bucket_size = (n - 2) // m
    remainder = (n - 2 ) % m 
    
    # 初始化桶的索引范围
    buckets = []
    start = 1 # 跳过第一个点
    for i in range(m):
        # 计算当前桶的大小
        if i < remainder:
            size = bucket_size + 1
        else:
            size = bucket_size
        
        end = start + size
        buckets.append((start, end))
        start = end  
    
    # 预计算每个桶的平均值
    avg_points = []
    for bucket_start, bucket_end in buckets:
        avg_x = np.mean(data[ bucket_start:bucket_end, 0])
        avg_y = np.mean(data[ bucket_start:bucket_end, 1])
        avg_points.append((avg_x, avg_y))

    # 初始化采样结果，保留第一个点
    sampled = [data[0]]
    
    # 处理每个桶
    for i in range(m):
        bucket_start, bucket_end = buckets[i]
        bucket_data = data[bucket_start:bucket_end]

        # 计算所有点形成的三角形面积
        
        # 向量化计算面积
        areas = calculate_triangle_area(data[i-1],avg_points[i])
        

def calculate_triangle_area(p1, p2, p3):
    # 将点转换为向量
    v1 = p2 - p1
    v2 = p3 - p1

    # 计算叉积的模
    cross_product = np.abs(np.cross(v1,v2))
    
    # 三角形面积 = 叉积模 / 2
    return cross_product / 2
    


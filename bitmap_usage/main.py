from bitarray import bitarray
import mmh3
from pybloom_live import ScalableBloomFilter


# 直接使用bitmap做去重。优势：对存储进行了进一步压缩，缺陷:碰撞概率增加
offset = 2147483647     # 2^31-1，32位机器上最大的offset(正数)
bit_array = bitarray(4 * 1024 * 1024 * 1024)     # 2的32次方大小的bitmap
bit_array.setall(0)
index = mmh3.hash(r'https://www.baidu.com/', 42) + offset    # 将hash的结果映射到0到2的32次方之间
bit_array[index] = 1
index = mmh3.hash(r'https://www.google.com/', 42) + offset
bit_array[index] = 1
print(bit_array.count())

# 使用Bloom Filter，减少碰撞概率
bloom_filter = ScalableBloomFilter(1000000, 0.001)  # 创建一个capacity等于100万，error rate等于0.001的bloomfilter对象
for x in range(1000000):
    bloom_filter.add(str(x))
error_in = 0
for x in range(2000000):
    if str(x) in bloom_filter and x > 1000000:
        error_in += 1
print("error_rate:%s" % (error_in * 1.0 / 1000000))
print(bloom_filter.count)
print(bloom_filter.capacity)

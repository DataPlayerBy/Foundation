from simhash import Simhash, SimhashIndex

# simhash
str0 = 'The Apache Hadoop software library is a framework that allows for the distributed processing large data'
str1 = 'The Apache Hadoop software library is a framework that allows for the distributed processing big data'
sh0 = Simhash(str0)
sh1 = Simhash(str1)
print(sh0.distance(sh1))    # 计算海明距离
features = [('Apache', 10), ('Hadoop', 15), ('framework', 3), ('distributed', 10), ('data', 6)]
sh0.build_by_features(features)
sh1.build_by_features(features)
print(sh0.distance(sh1))

# build a simhash index
data = {
    1: u'How are you? I Am fine. blar blar blar blar blar Thanks.',
    2: u'How are you i am fine. blar blar blar blar blar than',
    3: u'This is simhash test.',
}
objs = [(str(k), Simhash(v)) for k, v in data.items()]
index = SimhashIndex(objs, k=3)
print(index.bucket_size())
s1 = Simhash(u'How are you i am fine. blar blar blar blar blar thank')
print(index.get_near_dups(s1))
index.add('4', s1)
print(index.get_near_dups(s1))

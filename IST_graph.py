import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#csv_data['8_CST'] = np.where(csv_data['8_From_shardNum'] == csv_data['8_To_shardNum'], False, True)

shard8_CST = [1029318, 958466, 935511, 1054607, 992467, 959687, 751850, 865508, 1024742, 994328, 946494, 1046314, 1145961, 1048796, 984374, 1062717, 1014244, 925910, 975941, 862041, 764655, 761202, 763718, 914566, 782141, 810139, 691754, 843907, 899672, 941012, 834329, 813485, 731375, 726377, 643651, 590858, 658399, 726744, 789313, 730171, 798851, 701547, 866799]
shard16_CST = [1114218, 1031300, 1007803, 1128683, 1062382, 1023177, 799890, 922343, 1087279, 1049576, 1002595, 1112713, 1220191, 1113978, 1044924, 1125483, 1076037, 981524, 1035836, 917640, 812376, 814060, 816507, 976672, 837144, 874302, 742054, 906201, 970468, 1015601, 894732, 871196, 782057, 772193, 688596, 625572, 700540, 773186, 842670, 782005, 853971, 749190, 925869]
shard32_CST = [1151967, 1070253, 1036276, 1161582, 1097630, 1060774, 822869, 949221, 1126235, 1079870, 1030923, 1145645, 1263198, 1149653, 1079756, 1169380, 1110742, 1009921, 1065955, 954633, 836056, 835748, 839331, 1015929, 864061, 900119, 764166, 934988, 1001612, 1057847, 921528, 897808, 807193, 797626, 710522, 645301, 724925, 797533, 870554, 807098, 881813, 773923, 958137]
shard64_CST = [1166863, 1085280, 1048257, 1177514, 1112357, 1083830, 834431, 964493, 1141421, 1096838, 1043109, 1163162, 1282709, 1165931, 1094295, 1183762, 1127782, 1022806, 1080493, 968267, 848069, 847187, 852409, 1031331, 878024, 911695, 774560, 946947, 1017197, 1076448, 933789, 908815, 817812, 808007, 719579, 652900, 733969, 807800, 882488, 817062, 893244, 783654, 970185]

shard8_IST = [0]*43
shard16_IST = [0]*43
shard32_IST = [0]*43
shard64_IST = [0]*43

csv_data = pd.read_csv('./CST_result.csv')

'''
for i in range(0,10):
    print(csv_data['category'])
'''

# Epoch 당 IST 측정 (8, 16, 32, 64 shard 별로 그래프 합치기)
Epoch = 10000
IST_8_Epoch = [0] * int(500000 / Epoch)
IST_16_Epoch = [0] * int(500000 / Epoch)
IST_32_Epoch = [0] * int(500000 / Epoch)
IST_64_Epoch = [0] * int(500000 / Epoch)

csv_mid = csv_data[csv_data['8_CST'] == False]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        IST_8_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(IST_8_Epoch)

csv_mid = csv_data[csv_data['16_CST'] == False]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        IST_16_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(IST_16_Epoch)

csv_mid = csv_data[csv_data['32_CST'] == False]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        IST_32_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(IST_32_Epoch)

csv_mid = csv_data[csv_data['64_CST'] == False]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        IST_64_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(IST_64_Epoch)

# 그래프 출력
x = np.arange(500000 / Epoch)
Epoch = list(range(50))

plt.plot(Epoch, IST_8_Epoch, Epoch, IST_16_Epoch, Epoch, IST_32_Epoch, Epoch, IST_64_Epoch)
plt.legend(['8shard', '16shard', '32shard', '64shard'])
plt.xlabel('Epoch')
plt.ylabel('Number of CST')
plt.title('Number of CSTs per number of shards???')
plt.show()
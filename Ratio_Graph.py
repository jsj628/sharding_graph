import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Epoch = 10000

#CST
CST_y1 = [1029318, 958466, 935511, 1054607, 992467, 959687, 751850, 865508, 1024742, 994328, 946494, 1046314, 1145961, 1048796, 984374, 1062717, 1014244, 925910, 975941, 862041, 764655, 761202, 763718, 914566, 782141, 810139, 691754, 843907, 899672, 941012, 834329, 813485, 731375, 726377, 643651, 590858, 658399, 726744, 789313, 730171, 798851, 701547, 866799]
CST_y2 = [1114218, 1031300, 1007803, 1128683, 1062382, 1023177, 799890, 922343, 1087279, 1049576, 1002595, 1112713, 1220191, 1113978, 1044924, 1125483, 1076037, 981524, 1035836, 917640, 812376, 814060, 816507, 976672, 837144, 874302, 742054, 906201, 970468, 1015601, 894732, 871196, 782057, 772193, 688596, 625572, 700540, 773186, 842670, 782005, 853971, 749190, 925869]
CST_y3 = [1151967, 1070253, 1036276, 1161582, 1097630, 1060774, 822869, 949221, 1126235, 1079870, 1030923, 1145645, 1263198, 1149653, 1079756, 1169380, 1110742, 1009921, 1065955, 954633, 836056, 835748, 839331, 1015929, 864061, 900119, 764166, 934988, 1001612, 1057847, 921528, 897808, 807193, 797626, 710522, 645301, 724925, 797533, 870554, 807098, 881813, 773923, 958137]
CST_y4 = [1166863, 1085280, 1048257, 1177514, 1112357, 1083830, 834431, 964493, 1141421, 1096838, 1043109, 1163162, 1282709, 1165931, 1094295, 1183762, 1127782, 1022806, 1080493, 968267, 848069, 847187, 852409, 1031331, 878024, 911695, 774560, 946947, 1017197, 1076448, 933789, 908815, 817812, 808007, 719579, 652900, 733969, 807800, 882488, 817062, 893244, 783654, 970185]


#IST
y1 = [158070, 144972, 133275, 140826, 138966, 141778, 95195, 114135, 135859, 119793, 112801, 136910, 158038, 136394, 126231, 138657, 130695, 111844, 120989, 120986, 97523, 98228, 102887, 140618, 112374, 115744, 94968, 117014, 134871, 151721, 115226, 109410, 98519, 94610, 88280, 72917, 88520, 93361, 107602, 100271, 108110, 98253, 122194]
y2 = [73170, 72138, 60983, 66750, 69051, 78288, 47155, 57300, 73322, 64545, 56700, 70511, 83808, 71212, 65681, 75891, 68902, 56230, 61094, 65387, 49802, 45370, 50098, 78512, 57371, 51581, 44668, 54720, 64075, 77132, 54823, 51699, 47837, 48794, 43335, 38203, 46379, 46919, 54245, 48437, 52990, 50610, 63124]
y3 = [35421, 33185, 32510, 33851, 33803, 40691, 24176, 30422, 34366, 34251, 28372, 37579, 40801, 35537, 30849, 31994, 34197, 27833, 30975, 28394, 26122, 23682, 27274, 39255, 30454, 25764, 22556, 25933, 32931, 34886, 28027, 25087, 22701, 23361, 21409, 18474, 21994, 22572, 26361, 23344, 25148, 25877, 30856]
y4 = [20525, 18158, 20529, 17919, 19076, 17635, 12614, 15150, 19180, 17283, 16186, 20062, 21290, 19259, 16310, 17612, 17157, 14948, 16437, 14760, 14109, 12243, 14196, 23853, 16491, 14188, 12162, 13974, 17346, 16285, 15766, 14080, 12082, 12980, 12352, 10875, 12950, 12305, 14427, 13380, 13717, 16146, 18808]
Epoch = list(range(43))

'''
#전체 그래프
plt.plot(Epoch, y1, Epoch, y2, Epoch, y3, Epoch, y4)
plt.legend(['8shard', '16shard', '32shard', '64shard'])
plt.xlabel('Epoch')
plt.ylabel('Number of IST')
plt.title('Number of ISTs per number of shards???')
plt.show()
'''

'''
#일부 그래프
plt.plot(Epoch, CST_y1, Epoch, y1, Epoch, CST_y1/y1)
plt.legend(['8shard_CST', '8shard_IST', 'Ratio'])
plt.xlabel('Epoch')
plt.ylabel('Number of Transaction')
plt.show()
'''

ratio = [0]*43
for i in range(43):
    ratio[i] = CST_y1[i] / CST_y1[i] + y1[i]

plt.plot(Epoch, ratio)
plt.legend(['Ratio'])
plt.xlabel('Epoch')
plt.ylabel('Number of Transaction')
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#shardnum별 CST
shard8_shardnum = [5526632, 3817918, 5079533, 4627039, 4847649, 4553307, 3432545, 5479360]
shard16_shardnum = [3325451, 2474851, 2211150, 1911780, 2554886, 2763060, 2337899, 2562347, 2797118, 2352504, 2832125, 1984492, 1980725, 2036516, 2924990, 2834882]
shard32_shardnum = [2084020, 1379611, 1444645, 1089461, 991761, 1270248, 895921, 1078502, 1120286, 1482179, 1599252, 1231480, 1015519, 1417037, 1361639, 1244581, 1412807, 1555518, 1063484, 1344658, 1579967, 1314204, 998263, 1029147, 924943, 1099198, 1351261, 883055, 884466, 2133575, 1266922, 1632733]
shard64_shardnum = [1359199, 746801, 640554, 750257, 768347, 707948, 487625, 614014, 415951, 582967, 738193, 548382, 438329, 467186, 489050, 628089, 546611, 583906, 509161, 985670, 997866, 624518, 697561, 550387, 453176, 570543, 786688, 650449, 715458, 667393, 601243, 661758, 727806, 700854, 805593, 770956, 494315, 581512, 901883, 457332, 496974, 1098497, 712288, 614630, 589827, 417753, 519880, 524645, 433484, 501038, 504149, 607353, 774930, 600263, 487663, 462373, 448740, 445734, 1474241, 682080, 546375, 736155, 815058, 837152]

x = np.arange(8)

plt.bar(x, shard8_shardnum)
plt.xticks(x, fontsize=12)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('8 Shard')
plt.show()

x = np.arange(16)

plt.bar(x, shard16_shardnum)
plt.xticks(x, fontsize=12)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('16 Shard')
plt.show()

x = np.arange(32)

plt.bar(x, shard32_shardnum)
plt.xticks(x, fontsize=12)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('32 Shard')
plt.show()


x = np.arange(64)

plt.bar(x, shard64_shardnum)
plt.xticks(x, fontsize=12)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('64 Shard')
plt.show()
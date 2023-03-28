import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_data = pd.read_csv('./CST_result.csv')

# 8 샤드 별(From Field 기준) CST 수 확인
cstOfShard = [0] * 8
csv_mid = csv_data[csv_data['8_CST'] == True]
for CST in csv_mid['8_From_shardNum']:
    cstOfShard[CST - 1] += 1

print(cstOfShard)
x = np.arange(8)
shard = ['1', '2', '3', '4', '5', '6', '7', '8']

plt.bar(x, cstOfShard)
plt.xticks(x, shard)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('8 Shard')
plt.show()

# 16 샤드 별(From Field 기준) CST 수 확인
cstOfShard = [0] * 16
csv_mid = csv_data[csv_data['16_CST'] == True]
for CST in csv_mid['16_From_shardNum']:
    cstOfShard[CST - 1] += 1

print(cstOfShard)
x = np.arange(16)
shard = ['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13', '14', '15', '16']

plt.bar(x, cstOfShard)
plt.xticks(x, shard)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('16 Shard')
plt.xticks(rotation = 45)
plt.show()

# 32 샤드 별(From Field 기준) CST 수 확인
cstOfShard = [0] * 32
csv_mid = csv_data[csv_data['32_CST'] == True]
for CST in csv_mid['32_From_shardNum']:
    cstOfShard[CST - 1] += 1

print(cstOfShard)
x = np.arange(32)
shard = list(range(32))

plt.bar(x, cstOfShard)
plt.xticks(x, shard)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('32 Shard')
plt.xticks(rotation = 45)
plt.show()

# 64 샤드 별(From Field 기준) CST 수 확인
cstOfShard = [0] * 64
csv_mid = csv_data[csv_data['64_CST'] == True]
for CST in csv_mid['64_From_shardNum']:
    cstOfShard[CST - 1] += 1

print(cstOfShard)
x = np.arange(64)
shard = list(range(64))

plt.bar(x, cstOfShard)
plt.xticks(x, shard)
plt.xlabel('Shard Number')
plt.ylabel('Number of CST')
plt.title('64 Shard')
plt.xticks(rotation = 45)
plt.show()


# Epoch 당 CST 측정 (8, 16, 32, 64 shard 별로 그래프 합치기)
Epoch = 10000
CST_8_Epoch = [0] * int(500000 / Epoch)
CST_16_Epoch = [0] * int(500000 / Epoch)
CST_32_Epoch = [0] * int(500000 / Epoch)
CST_64_Epoch = [0] * int(500000 / Epoch)

csv_mid = csv_data[csv_data['8_CST'] == True]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        CST_8_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(CST_8_Epoch)

csv_mid = csv_data[csv_data['16_CST'] == True]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        CST_16_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(CST_16_Epoch)

csv_mid = csv_data[csv_data['32_CST'] == True]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        CST_32_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(CST_32_Epoch)

csv_mid = csv_data[csv_data['64_CST'] == True]

i = 9000000
j = 0

for NUM in csv_mid['block_number']:
    if NUM < i + Epoch:
        CST_64_Epoch[j] += 1
    else:
        i += Epoch
        j += 1

print(CST_64_Epoch)

# 그래프 출력
x = np.arange(500000 / Epoch)
Epoch = list(range(50))

plt.plot(Epoch, CST_8_Epoch, Epoch, CST_16_Epoch, Epoch, CST_32_Epoch, Epoch, CST_64_Epoch)
plt.legend(['8shard', '16shard', '32shard', '64shard'])
plt.xlabel('Epoch')
plt.ylabel('Number of CST')
plt.title('Number of CSTs per number of shards???')
plt.show()
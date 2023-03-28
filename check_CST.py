import pandas as pd
import numpy as np
import matplotlib as plt

csv_data = pd.read_csv('./result.csv')

### 8 shard 시작
# 8 From Field용 빈 배열 생성
From_shardNum_8 = []

# 8 shard 0x0~0x1/0x2~0x3/0x4~0x5/..., shard 분류
for adr in csv_data['from_address']:
    adr = int(adr[2:3], 16)
    j = 0
    for i in range(8):
        if j <= adr < j+2:
            From_shardNum_8.append(i + 1)
            break
        else:
            j = j+2

# 8 From field ShardNum 열 추가
csv_data['8_From_shardNum'] = From_shardNum_8

# 8 To field용 빈 배열 생성
To_shardNum_8 = []

# 8 shard 0x0~0x1/0x2~0x3/0x4~0x5/..., shard 분류
for adr in csv_data['to_address']:
    adr = int(adr[2:3], 16)
    j = 0
    for i in range(8):
        if j <= adr < j+2:
            To_shardNum_8.append(i + 1)
            break
        else:
            j = j+2

# 8 To field ShardNum 열 추가
csv_data['8_To_shardNum'] = To_shardNum_8

# 8 CST 여부 추가
csv_data['8_CST'] = np.where(csv_data['8_From_shardNum'] == csv_data['8_To_shardNum'], False, True)

### 16 shard 시작
# 16 From Field용 빈 배열 생성
From_shardNum_16 = []

# 16 shard 0x0~/0x1~/0x2~/..., shard 분류
for adr in csv_data['from_address']:
    adr = int(adr[2:3], 16)
    j = 0
    for i in range(16):
        if j <= adr < j+1:
            From_shardNum_16.append(i + 1)
            break
        else:
            j = j+1

# 16 From field ShardNum 열 추가
csv_data['16_From_shardNum'] = From_shardNum_16

# 16 To field용 빈 배열 생성
To_shardNum_16 = []

# 16 shard 0x0~/0x1~/0x2~/..., shard 분류
for adr in csv_data['to_address']:
    adr = int(adr[2:3], 16)
    j = 0
    for i in range(16):
        if j <= adr < j+1:
            To_shardNum_16.append(i + 1)
            break
        else:
            j = j+1

# 16 To field ShardNum 열 추가
csv_data['16_To_shardNum'] = To_shardNum_16

# 16 CST 여부 추가
csv_data['16_CST'] = np.where(csv_data['16_From_shardNum'] == csv_data['16_To_shardNum'], False, True)

### 32 shard 시작
# 32 From Field용 빈 배열 생성
From_shardNum_32 = []

# 32 shard 0x00~0x07/0x08~0x0f/0x10~0x17/... shard 분류
for adr in csv_data['from_address']:
    adr = int(adr[2:4], 16)
    j = 0
    for i in range(32):
        if j <= adr < j+8:
            From_shardNum_32.append(i + 1)
            break
        else:
            j = j+8

# 32 From field ShardNum 열 추가
csv_data['32_From_shardNum'] = From_shardNum_32

# 32 To field용 빈 배열 생성
To_shardNum_32 = []

# 32 shard 0x00~0x07/0x08~0x0f/0x10~0x17/... shard 분류
for adr in csv_data['to_address']:
    adr = int(adr[2:4], 16)
    j = 0
    for i in range(32):
        if j <= adr < j+8:
            To_shardNum_32.append(i + 1)
            break
        else:
            j = j+8

# 32 To field ShardNum 열 추가
csv_data['32_To_shardNum'] = To_shardNum_32

# 32 CST 여부 추가
csv_data['32_CST'] = np.where(csv_data['32_From_shardNum'] == csv_data['32_To_shardNum'], False, True)

### 64 shard 시작
# 64 From Field용 빈 배열 생성
From_shardNum_64 = []

# 64 shard 0x00~ ~<0x04/0x05~0x08/0x10~0x17/... shard 분류
for adr in csv_data['from_address']:
    adr = int(adr[2:4], 16)
    j = 0
    for i in range(64):
        if j <= adr < j+4:
            From_shardNum_64.append(i + 1)
            break
        else:
            j = j + 4

# 64 From field ShardNum 열 추가
csv_data['64_From_shardNum'] = From_shardNum_64

# 64 To field용 빈 배열 생성
To_shardNum_64 = []

# 64 shard
for adr in csv_data['to_address']:
    adr = int(adr[2:4], 16)
    j = 0
    for i in range(64):
        if j <= adr < j+4:
            To_shardNum_64.append(i + 1)
            break
        else:
            j = j+4

# 64 To field ShardNum 열 추가
csv_data['64_To_shardNum'] = To_shardNum_64

# 64 CST 여부 추가
csv_data['64_CST'] = np.where(csv_data['64_From_shardNum'] == csv_data['64_To_shardNum'], False, True)


# 결과 파일 저장하기
csv_data.to_csv("./CST_result.csv", index=True)
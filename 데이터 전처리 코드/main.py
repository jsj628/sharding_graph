import pandas as pd


# 몇개 행만 가져오려면 nrows 사용
col = [3,5,6]
csv_data = pd.read_csv('./transactions.csv', usecols=col)


# block_number가 9429999보다 큰 행은 제거. inplace는 원본 데이터 변경 여부.
index_for_delete = csv_data[csv_data['block_number'] > 9429999].index
csv_data.drop(index_for_delete, inplace=True)


# 'to_address'에 NaN값이 있으면 그 행 삭제
csv_data.dropna(subset=['to_address'], inplace=True)


# 인덱스 reset하기
csv_data.reset_index(drop=True, inplace=True)

# csv파일로 저장하기
csv_data.to_csv("./result.csv", index=True)


# 마지막 행 출력하기 (block number 확인)
num = csv_data.shape[0]
print(csv_data.loc[num-1])


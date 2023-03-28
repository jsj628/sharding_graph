import pandas as pd


csv_data = pd.read_csv('./result.csv')

num = csv_data.shape[0]
print("<트랜잭션 수>")
print(num)
print("")
print(csv_data.loc[num-1])

sum_of_account = 0

# from, to address가 둘 다 같은 경우 중복된 것 삭제
first = csv_data.drop_duplicates(subset=['from_address','to_address'])

# 딕셔너리 생성
account_dict = dict()

# from address에 있는 계정들 중복 없이 딕셔너리에 추가
for adr in first["from_address"]:
    if(account_dict.get(adr,None)==None):
        account_dict[adr] = True
        sum_of_account += 1
    else:
        continue


# to address를 탐색하면서 딕셔너리에 없는 계정이면 딕셔너리에 추가하고 sum 증가
for adr in first["to_address"]:
    if(account_dict.get(adr,None)==None):
        account_dict[adr] = True
        sum_of_account += 1
    else:
        continue
   
print("")
print("<account 수> ")
print(sum_of_account)
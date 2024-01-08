import pandas as pd

double_list = [
             [1000, '과자','2019-12-31','반품'],
             [2000, '음료', '2020-03-02', '정상'],
             [3000, '아이스크림', '2020-02-03','정상'],
             [1000,'과자','2019-12-31','반품']
            ]
double_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(data=double_list, columns=double_columns)
pass

def concate_word(words):
    return words

df_saledays['가격종류'] = df_saledays['가격'].apply(str) + "-" + df_saledays['종류']
print(df_saledays['가격종류'])

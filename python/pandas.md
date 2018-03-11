# pandas
## 改变列属性 astype, apply

```
import pandas as pd
a = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]
df = pd.DataFrame(a, columns=['one', 'two', 'three'])
df
Out[16]: 
  one  two three
0   a  1.2   4.2
1   b   70  0.03
2   x    5     0

df.dtypes
Out[17]: 
one      object
two      object
three    object
# method1 astype
df[['two', 'three']] = df[['two', 'three']].astype(float)  # int, str

df.dtypes
Out[19]: 
one       object
two      float64
three    float64
# method2 apply
df['two'] = df['two'].apply(lambda x: float(x))
df['three'] = df['three'].apply(lambda x: float(x))
```


## IO
```python
# read with header
df = pd.read_csv('./data/sep_by_tab_with_header.txt', sep='\t')

# read without header
df = pd.read_csv('./data/sep_by_tab_without_header.txt', sep='\t', names=['date', 'class', 'name'])

# write .csv .txt
df.to_csv('output/df.csv', encoding='gbk', index=True)
df.to_csv('output/df.txt', sep='\t', index=False)

# write .xls
ew = pd.ExcelWriter('output/df.xls', encoding='utf-8')
df.to_excel(ew, sheet_name='sheet1')
df2.to_excel(ew, sheet_name='sheet2')
ew.save()
```
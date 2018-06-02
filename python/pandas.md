# pandas
## 常用命令
在实际处理数据时，有时需要创建一个空的DataFrame，可以这么做：
df = DataFrame()


pd.concat([a, b], axis=1)
df = pd.concat([df, a], axis=0)
其中的axis=1表示按列进行合并，axis=0表示按行合并

可调用dataframe.sort_index，指定axis=0表示按索引（行名）排序，axis=1表示按列名排序，并可指定升序或者降序：

 df.sort(columns=['secID', 'tradeDate'], ascending=[True, False])

若想要保留最老的数据，可以在降序排列后取最后一个记录，通过指定take_last=True（默认值为False，取第一条记录）可以实现：
df2.drop_duplicates(subset='secID', take_last=True)



## 对列进行操作
```
db_all["sid"] = db_all.sid.str.replace("_con", "_zcon") #为了字典排序的原因
db["sid"] = db.sid.map(sid_dict)
```


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



## from pandas.core import format
```python
import pandas as pd
from pandas.core import format
from StringIO import StringIO
buf = StringIO()
df = pd.DataFrame({'correlation':[0.5, 0.1,0.9], 'p_value':[0.1,0.8,0.01]})
fmt = format.DataFrameFormatter(df,
          formatters={'p_value':lambda x: "*%f*" % x if x < 0.05 else str(x)})
format.HTMLFormatter(fmt).write_result(buf)

```


## transform求累计和
```python
start_date = '20161112'
end_date = '20170101'
date_list = myutils.gen_date_list(start_date, end_date)
files = ['sid_traffic_daily/%s_sid_traffic.txt' %date for date in date_list]
df = myutils.get_df_from_files(files)
df = df.sort_values(by=['search_date', 'pv'])
df.loc[:, 'sid_num'] = 1
df.loc[:, 'sid_num_cumsum'] = df.groupby('search_date')['sid_num'].transform(pd.Series.cumsum)
df.loc[:, 'sid_num_cumsum_percent'] = df.groupby('search_date')['sid_num_cumsum'].transform(lambda x: x / x.iloc[-1])
df.loc[:, 'pv_cumsum'] = df.groupby('search_date')['pv'].transform(pd.Series.cumsum)
df.loc[:, 'pv_cumsum_percent'] = df.groupby('search_date')['pv_cumsum'].transform(lambda x: x / x.iloc[-1])
```

##Pandas中DataFrame类型与TimeSeries类型进行二元运算的广播警示
提示如下:
>FutureWarning: TimeSeries broadcasting along DataFrame index by default is deprecated. Please use DataFrame.<op> to explicitly broadcast arithmetic operations along the index 

意思是说broadcasting现在还用, 但是以后可能取消, 让你最好用二元操作符, 如下:
|  方法    |    说明 |
| :-------- |: --------|
| DataFrame.add(other[, axis, level, fill_value])    |Binary operator add with support to substitute a fill_value for missing data in|
| DataFrame.sub(other[, axis, level, fill_value])   | Binary operator sub with support to substitute a fill_value for missing data in|
|  DataFrame.mul(other[, axis, level, fill_value])  |  Binary operator mul with support to substitute a fill_value for missing data in|
|  DataFrame.div(other[, axis, level, fill_value])  |  Binary operator truediv with support to substitute a fill_value for missing data in|
|...|...|

**参考链接:**
1. Getting warning “TimeSeries broadcasting along DataFrame index by default is deprecated”
http://stackoverflow.com/questions/23122362/getting-warning-timeseries-broadcasting-along-dataframe-index-by-default-is-dep

2.  pandas 0.16.1 documentation  --> Data alignment and arithmetic
http://pandas.pydata.org/pandas-docs/stable/dsintro.html?highlight=broadcasting#data-alignment-and-arithmetic

3. pandas 0.16.1 documentation  --> Binary operator functions
http://pandas.pydata.org/pandas-docs/stable/api.html#id4


## panda命令介绍
### DataFrame.iteritems(), DataFrame.iterrows()
**DataFrame.iteritems()**:  Iterator over (column, series) pairs
**DataFrame.iterrows()**    :  Iterate over rows of DataFrame as (index, Series) pairs.

建个数据集df：
```python
In [113]: %paste
rng = pd.date_range('2015-01-01', periods=4)
df = pd.DataFrame({"col1": range(1, 5), "col2": range(11, 15)}, index = rng)
df.index.name = "date"

## -- End pasted text --

In [114]: df
Out[114]: 
            col1  col2
date                  
2015-01-01     1    11
2015-01-02     2    12
2015-01-03     3    13
2015-01-04     4    14
```
- **DataFrame.iteritems()**:    Iterator over (column, series) pairs
```python
In [116]: a = df.iteritems()

In [117]: a
Out[117]: <generator object iteritems at 0x7f24c11dcaf8>

In [118]: aa = list(a)

In [119]: aa
Out[119]: 
[('col1', date
  2015-01-01    1
  2015-01-02    2
  2015-01-03    3
  2015-01-04    4
  Freq: D, Name: col1, dtype: int64), ('col2', date
  2015-01-01    11
  2015-01-02    12
  2015-01-03    13
  2015-01-04    14
  Freq: D, Name: col2, dtype: int64)]

In [120]: aa[0]
Out[120]: 
('col1', date
 2015-01-01    1
 2015-01-02    2
 2015-01-03    3
 2015-01-04    4
 Freq: D, Name: col1, dtype: int64)

In [121]: aa[0][0]
Out[121]: 'col1'

In [122]: aa[0][1]
Out[122]: 
date
2015-01-01    1
2015-01-02    2
2015-01-03    3
2015-01-04    4
Freq: D, Name: col1, dtype: int64

In [123]: type(aa[0][1])  #看一看它的类型
Out[123]: pandas.core.series.Series
```
- **DataFrame.iterrows()**  :  Iterate over rows of DataFrame as (index, Series) pairs.
```python
In [124]: b = df.iterrows()

In [125]: b
Out[125]: <generator object iterrows at 0x7f24c11dcc60>

In [126]: bb = list(b)

In [127]: bb
Out[127]: 
[(Timestamp('2015-01-01 00:00:00', offset='D'), col1     1
  col2    11
  Name: 2015-01-01 00:00:00, dtype: int64),
 (Timestamp('2015-01-02 00:00:00', offset='D'), col1     2
  col2    12
  Name: 2015-01-02 00:00:00, dtype: int64),
 (Timestamp('2015-01-03 00:00:00', offset='D'), col1     3
  col2    13
  Name: 2015-01-03 00:00:00, dtype: int64),
 (Timestamp('2015-01-04 00:00:00', offset='D'), col1     4
  col2    14
  Name: 2015-01-04 00:00:00, dtype: int64)]

In [128]: bb[0]
Out[128]: 
(Timestamp('2015-01-01 00:00:00', offset='D'), col1     1
 col2    11
 Name: 2015-01-01 00:00:00, dtype: int64)

In [129]: bb[0][0]
Out[129]: Timestamp('2015-01-01 00:00:00', offset='D')

In [130]: bb[0][1]
Out[130]: 
col1     1
col2    11
Name: 2015-01-01 00:00:00, dtype: int64

In [131]: type(bb[0][1])  #看一看它的类型
Out[131]: pandas.core.series.Series
```
###巧用pandas.Series.pct_change(),  pandas.Series.cumprod()计算比率
- `Series.pct_change(periods=1, fill_method='pad', limit=None, 
freq=None, **kwargs)`
- `Series.cumprod(axis=None, dtype=None, out=None, skipna=True, **kwargs)`

pct_chang()计算方法：
对于一个pandas.Series类型的数据s
|index| col1|
|:--|:--|
|0|$a_0$|
|1|$a_1$|
|2|$a_2$|
|3|$a_3$|
|4|$a_4$|
s调用pct_change()方法后， 变为s_pct_change：
|index| col1|
|:--|:--|
|0|`NAN`|
|1|$\frac{a_1-a_0}{a_0}$|
|2|$\frac{a_2-a_1}{a_1}$|
|3|$\frac{a_3-a_2}{a_2}$|
|4|$\frac{a_4-a_3}{a_3}$|

(1+s_pct_change).cumprod()就变成了比率s_ratio:

|index| col1|
|:--|:--|
|0|`NAN`|
|1|$\frac{a_1}{a_0}$|
|2|$\frac{a_2}{a_0}$|
|3|$\frac{a_3}{a_0}$|
|4|$\frac{a_4}{a_0}$|

 代码示例：
```python
In [179]: df = pd.DataFrame({"col1": range(1, 5), "col2": range(11, 15)}); df
Out[179]: 
   col1  col2
0     1    11
1     2    12
2     3    13
3     4    14

In [180]: s_pct_change = df["col1"].pct_change(); s_pct_change
Out[180]: 
0         NaN
1    1.000000
2    0.500000
3    0.333333
Name: col1, dtype: float64

In [181]: s_ratio = (1+s_pct_change).cumprod(); s_ratio
Out[181]: 
0   NaN
1     2
2     3
3     4
Name: col1, dtype: float64
```
cumprod默认Exclude NA/null values（skipna=True)：
```python
In [183]: s_pct_change[2] = np.nan; s_pct_change 
Out[183]: 
0         NaN
1    1.000000
2         NaN
3    0.333333
Name: col1, dtype: float64

In [184]: s_pct_change.cumprod() #NaN值直接pass掉
Out[184]: 
0         NaN
1    1.000000
2         NaN
3    0.333333
Name: col1, dtype: float64

```



## apply函数会在第一个组里调用两次函数, 如果产生负作用的话, 建议用deepcopy

```
import pandas as pd 
from pandas import DataFrame

df_dict = {"type": ["a", "a", "b", "b", "a"], "num": [1, 1, 1, 1, 1]}

df = DataFrame(df_dict)

def apply_fun(group):
    import copy
    group = copy.deepcopy(group)
    print "begin fun"
    print group
    group.loc[:, "num"] += 1
    print "end fun \n -----"

    return group.head(1)

print df

df_new = df.groupby(["type"], as_index=False).apply(apply_fun)
print df_new
```
结果:
```
     num type
0 0    3    a
1 2    2    b
```

参考链接:

Python pandas groupby object apply method duplicates first group
http://stackoverflow.com/questions/21390035/python-pandas-groupby-object-apply-method-duplicates-first-group

Group By: split-apply-combine
http://pandas.pydata.org/pandas-docs/stable/groupby.html#flexible-apply

pandas.DataFrame.apply
In the current implementation apply calls func twice on the first column/row to decide whether it can take a fast or slow code path. This can lead to unexpected behavior if func has side-effects, as they will take effect twice for the first column/row.
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html


## Pandas ParserError EOF character when reading multiple csv files to HDF5
这是由于字符里有出现不配对的引号
比如下面的文件:
```
sid query   next_change_query
111126  七星彩开奖结果今天   六开彩开奖结果
111126  三星s7    三星s7自动重启
111126  三生三世十里桃花    "friends are angels who lift us to our
```
解决方法:
```python
import csv
df = pd.read_csv(csvfile, delimiter="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')
```
参考链接:
- Pandas ParserError EOF character when reading multiple csv files to HDF5
http://stackoverflow.com/questions/18016037/pandas-parsererror-eof-character-when-reading-multiple-csv-files-to-hdf5



## Excel
- Pandas with XlsxWriter Examples
https://xlsxwriter.readthedocs.io/pandas_examples.html

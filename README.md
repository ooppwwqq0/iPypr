# iPypr
---
title: iPypr
date: 2017-05-11 12:10:29
---

# 摘要

参照 *PHP* 的 *print_r* 函数构造了一个 *Python* 版本的 print_r，起名叫 *iPypr*，方法为 *pypr*。

```
作者 : casstiel
邮箱 : emo_ooppwwqq0@163.com
QQ : 443557165
BLOG : http://c.isme.pub/
GITHUB : https://github.com/ooppwwqq0/iPypr
```

# 安装

```bash
pip install iPypr
```
# 使用方法

```python
from iPypr import pypr

a=[1,"2",3,3.1415,"asda",True,(1,2,4,5,[1,2,{"a":"a","b":True,"c":1,"d":[2,3,4]}]),[2,4,6,7,"123"],{"a":"asdas","b":123}]

pypr(a)

```

输出

``` bash
List(9) [
	[0] => 1
	[1] => "2"
	[2] => 3
	[3] => 3.1415
	[4] => "asda"
	[0] => True
	[6] => Tuple(5) (
		[0] => 1
		[1] => 2
		[2] => 4
		[3] => 5
		[4] => List(3) [
			[0] => 1
			[1] => 2
			[2] => Dict(4) {
				[a] => "a"
				[b] => True
				[c] => 1
				[d] => List(3) [
					[0] => 2
					[1] => 3
					[2] => 4
				]
			}
		]
	)
	[7] => List(5) [
		[0] => 2
		[1] => 4
		[2] => 6
		[3] => 7
		[4] => "123"
	]
	[8] => Dict(2) {
		[a] => "asdas"
		[b] => 123
	}
]
```


### Download the data

[yahoo_fin_examples](https://github.com/stormasm/yahoo_fin_examples/tree/main/v00)

```
python getfun.py test
python getquote.py test
```

Check out the code in these files for the location of the symbol files...

### Process the data

[python-examples](https://github.com/stormasm/python-examples/tree/master/pandas)

```
python selectbuild.py test
```

### Installation Instructions Prior to Running above Steps

This code requires that you have
[redis](http://redis.io)
installed on your system and that the redis server is up and running...

Set an environment variable **BMTOP**

```
cd into BMTOP
git clone this repository
```

### Code Notes of Interest

One change has to be made to the file after you get future new versions
of the file
[stock_info.py](https://github.com/stormasm/yahoo_fin/blob/master/yahoo_fin/stock_info.py#L338)
The attribute and value, which is the first line of the file that gets created
by getfun.py and getquote.py
have to match up in both created files otherwise this line
makes duplicates columns of the code because one attribute is lowercase
and one Attribute is upper case...

```python
  df = concat(symbol, dictfileary)
```

[when the method create_intermediate_dict gets called](https://github.com/stormasm/python-examples/blob/main/pandas/selectbuild.py#L23)

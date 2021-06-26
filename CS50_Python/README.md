## CS50’S WEB PROGRAMMING内のPython項目

### 文字列フォーマットの使用
```py
print(f"Hello, {name}")
```

### 集合（set）
```py
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(1)
s.remove(2)
print(s)
```
```bash
{1, 3}
```

### 辞書型
キーと値のペアのセット。  
**JSのオブジェクトとの違い**: Pythonの辞書はハッシュ可能なものでなければいけない。  
https://www.it-swarm-ja.com/ja/javascript/python%E8%BE%9E%E6%9B%B8%E3%81%A8javascript%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E9%81%95%E3%81%84%E3%81%AF%E4%BD%95%E3%81%A7%E3%81%99%E3%81%8B%EF%BC%9F/1044180049/
> Python辞書はハッシュ可能なものでなければなりません（たとえば、文字列、数値、浮動小数点数など）。
> 以下は、JavaScriptの有効なオブジェクトです。

>```js
>const javascriptObject = { name: 'Alexander Pushkin', year: 1799 }
>```
>Python辞書：
>```py
>python_dictionary = {name: 'Alexander Pushkin', year: 1799}
>```

>```bash
># Traceback (most recent call last):
># NameError: name 'name' is not defined

>簡単な修正方法は、Python辞書のキーを文字列に変換することです。
>```py
>my_dictionary = {'name': 'Alexander Pushkin', 'year': 1799}
>```

**ハッシュ可能とは**  
https://docs.python.org/ja/3/glossary.html
> hashable
>(ハッシュ可能) ハッシュ可能 なオブジェクトとは、生存期間中変わらないハッシュ値を持ち (__hash__() メソッドが必要)、他のオブジェクトと比較ができる (__eq__() メソッドが必要) オブジェクトです。同値なハッシュ可能オブジェクトは必ず同じハッシュ値を持つ必要があります。


### 関数型プログラミング
#### デコレータ
デコレータ ... 別の関数を変更できる高次関数  
https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368  
```py
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

""" Output:
About to run the function
Hello, world!
Done with the function
"""
```

### ラムダ関数
```py
square = lambda x: x * x
```
: の左側が入力。右側が出力。

#### 下2つのコードは同じ挙動(下はラムダ関数)
```py
people = [
    {"name": "kona", "Like": "Nogi"},
    {"name": "shota", "Like": "Nogi"},
    {"name": "ai", "Like": "Sakura"},
]


def f(person):
    return person["name"]


people.sort(key=f)
print(people)
""" Output:
[{'name': 'ai', 'Like': 'Sakura'}, {'name': 'kona', 'Like': 'Nogi'}, {'name': 'shota', 'Like': 'Nogi'}]
"""
```

```py
people = [
    {"name": "kona", "Like": "Nogi"},
    {"name": "shota", "Like": "Nogi"},
    {"name": "ai", "Like": "Sakura"},
]

people.sort(key=lambda person: person["name"])
print(people)
""" Output:
[{'name': 'ai', 'Like': 'Sakura'}, {'name': 'kona', 'Like': 'Nogi'}, {'name': 'shota', 'Like': 'Nogi'}]
"""
```
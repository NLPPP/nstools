# 繁体简体字转换python包

## 1. 功能

（1）繁体转换成简体

（2）简体转换成繁体

## 2. 快速开始

（1）繁体转简体

```
from pylangtools.langconv import Converter

if __name__=="__main__":
    traditional_sentence = '陳奕迅'
    simplified_sentence = Converter('zh-hans').convert(traditional_sentence)
    print(simplified_sentence)#陈奕迅
```

（2）简体转繁体

```

from pylangtools.langconv import Converter

if __name__=="__main__":
    simplified_sentence = '陈奕迅'
    traditional_sentence = Converter('zh-hant').convert(simplified_sentence)
    print(traditional_sentence)#陳奕迅
```


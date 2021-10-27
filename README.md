# dutch-digital-parser

Just a prototype playing around with lark and context-free grammars in order to post-process written out (dutch) numbers in ASR output. 

## Install:

```
$ poetry update
$ poetry install
```

### Use

``` 
$ poetry shell
(.venv) $ echo acht honderd drie en twintig | ddp --tree
getal
  meertal
    vuldeging
      acht
      honderd
    samenvoeging
      drie
      twintig

823
```








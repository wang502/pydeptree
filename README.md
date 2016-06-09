## Pydeptree

##### About
Command line interface to look up project skeleton. It is also for looking the dependency between different .py files.

##### Example output when looking up project skeleton
```
  $ python Dir.py
```
output:
```
Toptal-API
    |
    +-- Toptal_API.egg-info/
    +-- toptal/
        +-- utils.py
           |-- get_response(url)
           |-- Soup(url)
        +-- Toptal.py
           |-- class Toptal
              __init__(self)
              search(self, keyword, start=1, count=10)
              trending(self)
              newest(self)
              topic(self, topic)
           |-- class Item
              __init__(self, url, title)
              get_content(self)
              set_type(self, t)
              __str__(self)
        +-- main.py
           |-- main(newest, search, topic, trending)
        +-- constants.py
        +-- __init__.py
           |-- main(newest, topic, trending, search)
    +-- setup.py
    +-- dist/
    +-- build/
        +-- lib/
            +-- toptal/
                +-- utils.py
                     |-- get_response(url)
                     |-- Soup(url)
                +-- Toptal.py
                     |-- class Toptal
                            __init__(self)
                            search(self, keyword, start=1, count=10)
                            trending(self)
                            newest(self)
                            topic(self, topic)
                     |-- class Item
                            __init__(self, url, title)
                            get_content(self)
                            set_type(self, t)
                            __str__(self)
                +-- main.py
                     |-- main(newest, search, topic, trending)
                +-- constants.py
                +-- __init__.py
                     |-- main(newest, topic, trending, search)
        +-- bdist.macosx-10.11-intel/
```

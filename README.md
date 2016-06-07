## Pydeptree

##### About
Command line interface to look up project skeleton. It is also for looking the dependency between different .py files.

##### Example output when looking up project skeleton
```
  $ python Dir.py
```
output:
```
/Users/Xiaohui/Desktop/contribution/Toptal-API
  |
  +-- /toptal/__init__.py
    main(newest, topic, trending, search)
  |
  +-- /toptal/Toptal.py
    class Toptal
        __init__(self)
        search(self, keyword, start=1, count=10)
        trending(self)
        newest(self)
        topic(self, topic)
    class Item
        __init__(self, url, title)
        get_content(self)
        set_type(self, t)
        __str__(self)
    |
    +-- /build/lib/toptal/Toptal.py
      class Toptal
          __init__(self)
          search(self, keyword, start=1, count=10)
          trending(self)
          newest(self)
          topic(self, topic)
      class Item
          __init__(self, url, title)
          get_content(self)
          set_type(self, t)
          __str__(self)
  |
  +-- /toptal/utils.py
    get_response(url)
    Soup(url)
    |
    +-- /build/lib/toptal/__init__.py
      main(newest, topic, trending, search)
    |
    +-- /build/lib/toptal/utils.py
      get_response(url)
      Soup(url)
    |
    +-- /build/lib/toptal/main.py
      main(newest, search, topic, trending)
  |
  +-- /toptal/main.py
    main(newest, search, topic, trending)
```

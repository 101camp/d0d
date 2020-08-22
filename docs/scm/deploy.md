# 部署

## env.
开发环境:

``` 

༄  screenfetch

                 -/+:.          zoomq@ZQ160626rMBP
                :++++.          OS: 64bit Mac OS X 10.12.6 16G2136
               /+++/.           Kernel: x86_64 Darwin 16.7.0
       .:-::- .+/:-``.::-       Uptime: 14d 2h 33m
    .:/++++++/::::/++++++/:`    Packages: 238
  .:///////////////////////:`   Shell: bash
  ////////////////////////`     Resolution: 2560x1600 2560x1440
 -+++++++++++++++++++++++`      DE: Aqua
 /++++++++++++++++++++++/       WM: Quartz Compositor
 /sssssssssssssssssssssss.      WM Theme: Blue
 :ssssssssssssssssssssssss-     CPU: Intel Core i7-5557U @ 3.10GHz
  osssssssssssssssssssssssso/`  GPU: Intel Iris Graphics 6100
  `syyyyyyyyyyyyyyyyyyyyyyyy+`  RAM: 8760MiB / 16384MiB
   `ossssssssssssssssssssss/
     :ooooooooooooooooooo+.
      `:+oo+/:-..-:/+o+/-

```

## depend

Install with `pip`:

``` sh
$   pip install -r requirements.txt
```

Append to `mkdocs.yml`:

``` yaml
theme:
  name: 'material'
```

并使用定制自动运营脚本来完成编译和发布:


``` sh

༄  echo '' > _trigger/deploy.md

༄  inv pub 101

/opt/data/Sites/101.camp/_running

     crt. PATH ===
/Users/zoomq/Sites/101.camp/_running/gl_101.camp
Already up-to-date.

     crt. PATH ===
/opt/data/Sites/101.camp/_running/zq_gh101camp
Already up-to-date.

     crt. PATH ===
/Users/zoomq/Sites/101.camp/_running/gl_101.camp
./_trigger
TRIGGERed by deploy.md exist
auto deplo NOW:

...


 3 files changed, 76 insertions(+)
To github.com:ZoomQuiet/gh101camp.git
   9b88f3c..9ec3eab  master -> master

     powded by pub101CAMP v.191011.2042
```

## logging

- 200822 ZQ re-init. for d0d
- 191018 DAMA upgrade theme+cfg
- 190321 DAMA upgrade theme +ico
- 190320 DAMA deploy as 101.camp
- 190202 DAMA base gh-pages
- 190201 DAMA init.




```

     _  ___      _   _  ___  _
  __| |/ _ \  __| | / |/ _ \/ |  ___ __ _ _ __ ___  _ __
 / _` | | | |/ _` | | | | | | | / __/ _` | '_ ` _ \| '_ \
| (_| | |_| | (_| |_| | |_| | || (_| (_| | | | | | | |_) |
 \__,_|\___/ \__,_(_)_|\___/|_(_)___\__,_|_| |_| |_| .__/
                                                   |_|

```




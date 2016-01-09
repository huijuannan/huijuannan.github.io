---
title: Mac 装机记录
updated: 2016-1-9
---
> 1月7日拿到新的mac pro，折腾了2天。记录一下装机过程。
> 本文主要参考[阳老的装机日志](http://www.yangzhiping.com/tech/mac3.html)，感谢[沈浪同学](https://github.com/xpgeng)的耐心帮助。

## Xcode
- App Store免费应用,足足4G多，下载时失败了两次，花了大半天才下载完。

## Homebrew & cask

装完Xcode就可以开始各种折腾了
### 安装
- 首先安装homebrew，一下代码copy到Terminal里面，运行就可以了

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

- 之后安装brew cask

```bash
brew tap phinze/homebrew-cask
brew install brew-cask
```

### 大规模装机
安装了上述两个利器之后，装机就变得so easy。按照阳老博客里面的内容，并根据自己的需要在命令行里输入一下代码

```bash
brew cask install sublime-text

brew install wget && brew install curl && brew install openssl && brew install imagemagick && brew install node && brew install zsh && brew install git-flow && brew install python

brew cask install iterm2 && brew cask install jumpcut

brew cask install the-unarchiver && brew cask install mou && brew cask install alfred && brew cask install vlc 
```

- chrome本来也是想用cask安装的，但是失败了，就从官网上下载安装了。
- 经沈浪同学建议，把mou换成了[macdown](http://macdown.uranusjr.com)。因为Mou的作者已经不更新了。
- 安装Dash，把官方文档下载到本地的神器。

## 词典
用了两天发现，mac自带的词典非常强大，取词也十分方便。

- 取词
  - 在系统偏好设置-触控板-光标与点按-查找与数据检测器，选择为`用三个手指轻点`,这样不论在什么页面，只要三指轻点就可以取词了，so easy。
- 下载词典
  - 下载[DictUnifier](https://github.com/jjgod/mac-dictionary-kit)，可以把tar.bz2格式下载的词典拖进去，自动转化成系统可用的词典，并且添加。
  - 到[词库](http://abloz.com/huzheng/stardict-dic/zh_CN/)下载需要的词典，下载完成后拖到DictUnifier里就可以啦。

## 杂七杂八
### 通讯工具
- QQ和微信就不多说了，微信mac版比win版好看很多。

### System Integrity Protection
- 下载macdown以后，想要从命令行直接访问，比如像这样

```
macdown myfile.md
```

- 按照[官方的说明](http://macdown.uranusjr.com/blog/post/6/macdown-04/)，发现没有link的权限，提示`Operation not permitted`
- 于是google以后发现，是由于System Integrity Protection这个玩意导致的，参照[这里](http://stackoverflow.com/questions/32659348/operation-not-permitted-when-on-root-el-capitan-rootless-disabled)设置以后，问题解决。

### CLI
- `tmux`和`oh-my-zsh`安装和配置参照沈浪同学的教程([tmux](https://xpgeng.gitbooks.io/omooc2py/content/guide/Tmux-Guide.html)，[oh-my-zsh](https://xpgeng.gitbooks.io/omooc2py/content/guide/Oh-my-zsh-guide.html))。

## Reference
- [阳老的装机日志](http://www.yangzhiping.com/tech/mac3.html)
- [Homebrew](http://brew.sh)
- [macdown](http://macdown.uranusjr.com)
- [DictUnifier](https://github.com/jjgod/mac-dictionary-kit)
- [词典库](http://abloz.com/huzheng/stardict-dic/zh_CN/)
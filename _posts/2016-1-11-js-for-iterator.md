---
title: JS里for循环的各种姿势
updated: 2016-1-11
---

>以前用Matlab，对for循环的理解只停留在`for i=1:100`这种计数器模式。这几天初学JS，发现原来for的用法还有这么多的姿势。

## 计数器模式

最传统的姿势，相当于一个计数器。

```javascript
for (var i = 0; i < 10; i++)
	//do something
```

## String

> 如果想得到如下的三角形，问怎么写这个循环？

```
#
##
###
####
#####
```

可以还是沿用计数器的模式，计数器每多计一个数，就增加一个`#`

```javascript
var line = ''
for (var i = 0; i < 5; i++)
	line += '#'
	console.log(line)
```

但是更简洁的方法是，直接在for循环体里面把这些都完成了

```javascript
for (var line = '#'; line.length<=5; line += '#')
	console.log(line)
```

所以说，如果for循环的意思以某种固定的规则（在这里，是每一次都要增加一个`#`），重复n次相同的动作（打印到屏幕上），那么可以写成:

```
for (规则)
	重复动作
```

## Object

> JS里的Object相当于Python里面的dict，是一种键（key）和值（value）的一一对应关系。比如建立一个关于我自己的对象`var me = {name: "Nan Huijuan", sex: "female"}`，这样`me.name`就是`Nan Huijuan`。

Object和Array不同，Object里面的key是没有顺序的，这时候如果想要把所有的key都过一遍，就要借助`in`

```javascript
for (var prop in me)
	console.log(me[prop])
```

而如果我们有一个嵌套的Object，像这样

```
var list = {
  value: 1,
  rest: {
    value: 2,
    rest: {
      value: 3,
      rest: null
    }
  }
};
```

如果我们想转换成正常的Array，我们需要做的就是从最外一层，将`value`的值push到一个Array里面，然后list更新为rest，转化成代码则是：

```
array = [];
for (node = list; node; node = node.rest)
	array.push(list.value)
```

## 总结

循环的姿势不只计数器一种。如果想写出简洁优雅的for循环，应该在写之前先想明白，循环的每一周期里，变化的部分是什么，怎么变的。把这部分放在for之后的括号里面。然后再把剩下不变的部分放在body里。

## PS

阳老的[博客](http://www.yangzhiping.com/tech/learn-program-psychology.html)里面说，学习一门编程语言，刻意练习的量是每天500行代码。看了看昨天刷的习题，撑死了100行。真是任重而道远呐……

## Reference
- 例子都来自于[Eloquent Javascript](http://eloquentjavascript.net)

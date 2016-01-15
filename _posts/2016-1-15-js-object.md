---
title: JS里Object初试
updated: 2016-1-15
---

> Object和与之相关连的基于对象的编程，学python的时候一直一知半解，最近刷JS的教程才有了一些初步的了解。

## 简单来说……

如果简单来说，Object就是一种可以快速检索的数据结构。它把key和value一一对应起来。这样，如果我们想知道某一个key对应的值，就直接object.key就可以了，返回的就是这一个key对应的value。

> Python中，这个结构叫做dictionary。是说这个结构就像是字典一样，每一个字，对会有对应的意思，可以查找，非常方便。

所以，构造一个最简单的Object，引用上一篇[博客]()里关于猫咪的例子：

```javascript
var myCat = {name:'Marnie', color:'white and yellow', sex:'f', weightInKg:3};
```

在这里，我创建了一个叫做myCat的Object，我的猫咪myCat这个对象，我让它有4个属性或者说key，分别是名字、颜色、性别和体重。这样，当我想知道其中某一个的值(value）的时候，就只要`myCat.name`来得到就可以了。到这里还非常的直觉和简单。

另外，查找key的方法，不仅可以object.key还可以object[key]，但这种互换只有在key是一个可以做变量名字的字符串的时候才可以，比如myCat里面的几个。但是以下几种情形下，这种互换是不行的，只能用object[key]。

1. 如果key是一个带空格的或者数字等等不能做变量名字的情形，比如`var me = {'my name':'huijuannan'};`，就只能用`me['my name']`。
2. 如果key是一个变量的话(比如，namekey = 'name')，那也只能用object[key]这种形式。原因是object.key与之相对应的是object['key']，因此它会直接把变量名转化成字符串，而不是会读入变量的值在检索。

>所以，`myCat.namekey`只会得到`undefined`。`myCat[namekey]`就会得到`'Marnie'`。

## 当Object遇上Function……

事情变得复杂，是从加入了Function开始。首先，Object里的value可以是function，并且，Object可以通过function创建。

### Function and method

第一种情形，当value不是字符串或者数组，而是一个方程，比如:

```
myCat['mew'] = function(){console.log('Mew~ Mew~')}
myCat.mew() //Mew~ Mew~
```

这时候mew被称作myCat的一种方法（即，Method）。

### Constructor

当我们需要创建许多有共同key的Object的时候，我们就希望会有一个方程来生成他们。比如说，如果我家的猫咪生了许多小猫，那么如果我们每一次都把下面的代码重复一遍的话显然不够明智。

```javascript
var myCat = {name:'Marnie', color:'white and yellow', sex:'f', weightInKg:3};
```

于是，此时，我们用一个方程来创建这些类似的属性，而这个方程被称作constructor。

```
function Cat(name, color, sex){
this.name = name;
this.color = color;
this.sex = sex;
}
```

而此时，如果我们想创建一只叫做Gollum的猫咪，我们要做的就是`gollum = new Cat('Gollum', 'black', 'm');`，这样，就生成了一只名字叫咕噜、黑色的小公猫了。

再回来解释一下constructor这个方程。首先，它是一个方程，输入的值是`name， color, sex`。而方程的作用是，新建一个Object，有name、color、sex这三个key，并且对应的value是我们输入的三个值。所以，我们怎么在方程里面调用这样一个我们还没有创建的object呢？就是`this`。`this`指向的就是有着name、color、sex这三个key的Object。而当我们需要创建新的猫咪对象的时候，我们要做的就是用`new`这个关键词，表明我们要创建一个新的对象了，这样`new Cat('Gollum', 'black', 'm');`返回的就是一个新的Object了。

### Prototype








---
title: JS里Object初试
updated: 2016-1-15
---

> Object和与之相关连的基于对象的编程，学python的时候一直一知半解，最近刷JS的教程才有了一些初步的了解。

## 简单来说……

如果简单来说，Object就是一种可以快速检索的数据结构。它把key和value一一对应起来。这样，如果我们想知道某一个key对应的值，object.key返回的就是这一个key对应的value。

> Python中，这个结构叫做dictionary。就像是字典一样，每一个字，对会有对应的意思，可以查找，非常方便。

所以，构造一个最简单的Object，引用上一篇[博客](http://huijuannan.github.io/notes/js-map-foreach-reduce/)里关于猫咪的例子：

```javascript
var myCat = {name:'Marnie', color:'white and yellow', sex:'f', weightInKg:3};
```

在这里，我创建了一个叫做myCat的Object，我的猫咪myCat这个对象，我让它有4个属性或者说key，分别是名字、颜色、性别和体重。这样，当我想知道其中某一个的值(value）的时候，就只要`myCat.name`就可以得到。到这里还非常的直觉和简单。

另外，查找key的方法，不仅可以object.key还可以object[key]，但这种互换只有在key是一个可以做变量名字的字符串的时候才可以，比如myCat里面的几个。但是以下几种情形下，这种互换是不行的，只能用object[key]。

1. 如果key是一个带空格的或者数字等等不能做变量名字的情形，比如`var me = {'my name':'huijuannan'};`，就只能用`me['my name']`。
2. 如果key是一个变量的话(比如，namekey = 'name')，那也只能用object[key]这种形式。原因是object.key与之相对应的是object['key']，因此它会直接把变量名转化成字符串，而不是会读入变量的值在检索。

>所以，`myCat.namekey`只会得到`undefined`。`myCat[namekey]`就会得到`'Marnie'`。

## 当Object遇上Function……

事情变得复杂，是从加入了Function开始。首先，Object里的value可以是function，并且，Object可以通过function创建。

### Function and method

第一种情形，当value不是字符串或者数组，而是一个方程，比如:

```
myCat['mew'] = function(){console.log('Mew~ Mew~')};
myCat.mew() //Mew~ Mew~
```

这时候mew被称作myCat的一种方法（即，Method）。

### Constructor

当我们需要创建许多有相同key的Object的时候，我们就希望会有一个方程来生成他们。比如说，如果我家的猫咪生了许多小猫，那么如果我们每一次都把下面的代码重复一遍的话显然不够明智。

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

这样，如果我们想创建一只叫做Gollum的猫咪，我们要做的就是`gollum = new Cat('Gollum', 'black', 'm');`，这样，就生成了一只名字叫咕噜、黑色的小公猫了。

再回来解释一下constructor。首先，它是一个方程，输入的值是`name， color, sex`。而方程的作用是，新建一个Object，有name、color、sex这三个key，并且对应的value是我们输入的三个值。所以，我们怎么在方程里面调用这样一个我们还没有创建的object呢？就是`this`。`this`指向的就是有着name、color、sex这三个key的Object。而当我们需要创建新的猫咪对象的时候，我们要做的就是用`new`这个关键词，表明我们要创建一个新的对象了，这样`new Cat('Gollum', 'black', 'm');`返回的就是一个新的Object了。

### Prototype

> Function, array, regular expression 都是Object的一种特殊形式。比如，array可以看做key是0、1、2、3的object。Function的情况比较复杂，当我们创建一个Function的时候，JS会自动给我们创建两个Object。一个是这个Function本身，另外一个是Function.prototype。可以试试下面的代码：

```
function tryMe(){console.log("I'm a test function!")}
tryMe() // I'm a test function!
tryMe.name // 'tryMe'
tryMe.prototype.constructor() //I'm a test function!
```

我们发现，`tryMe()`和`tryMe.prototype.constructor()`的结果是一样的。这就是因为，当我们创建function的时候，同时创建了另外一个Object，即Function.prototype，这个object有一个key是constructor，是指向tryMe()本身的。所以说，在上面一节，我们用`gollum = new Cat('Gollum', 'black', 'm');`创建一个新的Object的时候，其实是创建的Cat.prototype的一个实例。

所以接下来，如果我们想要给所有Cat的实例都加上mew这个动作，我们要做的就是：

```
Cat.prototype.mew = function(){console.log('Mew~ Mew~');};
gollum.mew() // Mew~ Mew~
```

换句话说，我们通过`new Cat(name, color, sex)`创建的Object，会继承所有Cat.prototype的属性，就好比，如果我们让猫咪这一个类会喵喵的话，那么用它来创建的每一只猫咪都会喵喵。

### 多说一点this

```
Cat.prototype.sayHi = function(){console.log("Hi, I'm " + this.name + "!")};
gollum.sayHi() //Hi, I'm Gollum!
```

现在我们让猫咪可以打招呼了。现在我又养了几只狗狗，我希望再创建一个狗狗的constructor，当然因为狗狗和猫猫的属性差不多，所以我希望能借助之前创建好的Cat来帮助我创建Dog。

```
function Dog(name, color, sex){
Cat.call(this,name,color,sex);
}
```

这里面出现了*call*和*this*的组合。为什么不能直接用Cat(name,color,sex)是因为，如果我们直接调用Cat这个方程，那么它对应的this是用`new Cat`创建的那一个Object，而此时，我们并没有这样一个Object，也就是说，当我们把name, color, sex传递给Cat的时候，Cat发现找不到一个合适的this。所以，在这里，如果我们需要明确告诉它，this指代的是我们要新创建的狗狗，不再是猫猫了，此时我们用了call这个方法，它把第一个参数作为this的具体指代，在这里就是Dog创建的Object。

```
var pipi = new Dog('Pipi','white','f');
console.log(pipi); // Dog { name: 'Pi', color: 'white', sex: 'f' }
```

这样我们就创建了一只叫做皮皮的狗。

如果我们想要把Cat的其他方程也移植到Dog这里。

```
Dog.prototype = Object.create(Cat.prototype);
var panda = new Dog('Panda', 'black and white', 'm');
panda.sayHi() // Hi, I'm Panda!
```


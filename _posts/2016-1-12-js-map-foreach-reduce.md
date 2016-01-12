---
title: JS里的Array方法之forEach map reduce
updated: 2016-1-12
---

>刚开始看JS的时候，每次看到把function当做一个变量来用，就很迷糊。看了两天之后，好歹习惯了一些。
>
>这篇文章里的几个方法都是针对数组（Array）的，输入的变量都是函数。

## 简单的例子

用一个数组来记录我的两只喵——玛尼和咕噜，并且记录下他们各自的属性，如性别、毛色等等。

```javascript
var myCat = [
	{name:'Marnie', color:'white and yellow', sex:'f', weightInKg:3},
	{name:'Gollum', color:'black', sex:'m', weightInKg: 4.2}
];
```

在这个数组里面，每一个元素都是一个Object，其中包含了猫咪的名字、颜色和性别。

## forEach

为了检索这方便，我们想要把这个数组转化成以猫咪的名字为key的Object。我们希望数据变成这样：

```javascript
var cat = {Marnie:{name:'Marnie', color:'white and yellow', sex:'f', weightInKg:3},
	Gollum:{name:'Gollum', color:'black', sex:'m', weightInKg: 4.2}};
```

为了达成这个目标，我们要做的就是，对于`myCat`数组里的每一个元素，我们把其中的`name`作为我们新的Object——`cat`的key，而把这个元素整体作为对应的value。可以看到，这里面包含了一个这样的过程，就是对数组里面的每一个元素执行一系列操作，这时候，我们就可以用到`forEach`这个方法。

```javascript
var cat = {};
myCat.forEach(function(a){
	cat[a.name] = a;
})
```

换句话说，array.forEach(fun1)的意思是说，对array里面的每一个元素，都进行fun1这个操作。fun1函数的输入变量，就是array里的一个元素。相当于一个for循环，每次向fun1里输入array的一个元素。

## map

这次我们想要把这个复杂的数组转换成一个简单的，只包含猫咪名字的列表。

```
var catName = myCat.map(function(a){
	return a.name;});
```

抽象出来，map做的事情就是：

1. 建立一个和原来的数组一样大小的空数组
2. 一次对数组的一个元素执行某些操作，比如在我们的例子里面就是,返回猫咪的名字。
3. 把返回的这个值填到新建的数组对应的位置上。


## reduce

最后我们想要做的事情是，算一下两只猫咪的平均体重

```
var meanWeight = myCat.reduce(function(a,b){
	return a.weightInKg +b.weightInKg;})/myCat.length;
```

`reduce`的意思是，把这个数组通过一定的操作汇总成一个值，比如在上面的操作里面，就是把猫咪的体重都加起来，求一个sum。但这个操作不是一次性完成的，而是用循环的方法俩俩进行的。具体说来就是（假设我们有很多只猫咪）：

1. 把第一只猫咪的体重和第二只猫咪的体重相加。
2. 把这两只猫咪的体重之和第三只猫咪的体重相加。
3. 把上面的和再和第四只猫咪的体重相加。

这样我们就可以算出很多只猫咪的体重之和。抽象出来就是，我们有两个变量a和b，a用来储存上一次计算的结果，b储存这一次要用来计算的值，所以把上面的过程再转化一下就是：

1. a = 第一只猫咪的重量，b = 第二只猫咪的重量，计算a+b
2. a = a+b, b = 第三只猫咪的重量，计算a+b
3. a = a+b, b = 第四只猫咪的重量，计算a+b

这里面，如果a没有给定一个初始值，即`reduce`的输入变量只有一个function，那么开始的a的值就默认为array里的第一个元素，b是array里的第二个元素，就像我们的例子一样。而如果我们给定了一个a的初始值，比如`array.reduce(fun1,a0)`那么，初始的a的值就是a0，而此时b是array里第一个元素。

## 总结

JS里的这三个方法之所以让人迷糊，是因为本来这个三个方法本身就是一个函数，可是它还要再接受一个函数作为输入值，所以就涉及到两个函数各自的输入和输出问题。而反过来，如果把各自的输入和输出搞明白了，那么想明白这三个方法怎么用，就没那么难了。

## Reference

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
- http://eloquentjavascript.net/05_higher_order.html

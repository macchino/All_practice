'use strict';
console.log('Hello World');
console.log('Hello World');
console.log('Hello World');
console.log('Hello World');

console.log(12345);
console.log(12345.6789);
console.log('12345');
console.log("hello! I'm juda");
console.log("hello! I\'m juda");
console.log("hel\ \tlo! I\'m \njuda");

let color = 'Red';
console.log(color);

let myColor = 'Blue';
console.log(myColor);

var myName = 'Taro';
console.log(myName);

// 定数
const PI = 3.14;
console.log(PI);
// PI = 3.1; NG

const TAX_RATE = 10;
console.log(TAX_RATE);

let MyName = 'Taro';
let num = 123;
let dec = 123.456;

console.log(MyName);
console.log(num);
console.log(dec);

console.log(typeof MyName);
console.log(typeof num);
console.log(typeof dec);
// 変数に型違いが編入出来てしまう
MyName = 456;
console.log(MyName);
console.log(typeof MyName);

// JavaScript=動的型付け言語

// 演算子
let ans = 1 + 2;
console.log(ans);
let i = 20;
let j = 10;
let ans1 = i + j;
console.log(ans1);
let ans2 = i - j;
console.log(ans2);
let ans3 = i * j;
console.log(ans3);
let x = 3;
let y = 2;
let ans5 = x / y;
console.log(ans5);
let ans6 = Math.pow(x, y);
console.log(ans5);
let ans7 = x ** y;
console.log(ans7);


let lastName = 'あああ';
let firstName = 'いいいい';
let massage1 = 'こんにちは' + lastName + ' ' + firstName;
console.log(massage1);

let message2 = `こんにちは ${lastName} ${firstName}
Javascriptの学習`;
console.log(message2);

let num20 = 20;
num = num20 + 10;
console.log(num);

let num30 = 20;
num30 += 10;
console.log(num30);

let num31 = 20;
num31 -= 10;
console.log(num31);

let weghit = 60;
let tall = 1.7;
let BMI = weghit / (tall * tall);
console.log(BMI);

let num40 = 10;
num40++;
console.log(num40);

let num41 = 11;
let num42 = 11;
let ans41 = ++num41;
let ans42 = num42++;
console.log(ans41);
console.log(ans42);


let temp = 29;
if (temp > 28) {
    console.log('冷房稼働');
    }

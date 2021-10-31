'use strict';
let birthYear = '2000';
let age = 18;

console.log(birthYear + age)
console.log(age + birthYear)

console.log(Number(birthYear) + age)
console.log(String(age)+ '歳')

let b1 = true;
if (!b1) {
    console.log('はい');
} else {
    console.log('いいえ')
}

let num = 100;
let str = '100';

if (num == str) {
    console.log('同じ');
} else {
    console.log('同じではない')
}

if (num === str) {
    console.log('同じ');
} else {
    console.log('同じではない')
}

let weight = 60;
let height = 1.70;
let bmi = weight / (height * height);
console.log(bmi);

if (bmi >= 25) {
    console.log('肥満');
} else if (b >= 18.5) {
    console.log('普通');
} else {
    console.log('痩せ')
}

console.log(true && true)
console.log(true === true)
console.log(false && false)
console.log(false === false)

console.log(true || true)
console.log(true || false)
console.log(false || false)

console.log(!true)
console.log(!false)



console.log(false && true || true);
console.log(false && (true || true));
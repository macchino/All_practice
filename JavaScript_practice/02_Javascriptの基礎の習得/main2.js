'use strict';
console.log(29 > 28);
console.log(20 > 28);

let a = 100;
if (a >= 100) {
    console.log('100以上')
}

let b = 101;
if (b > 100) {
    console.log('100より大きい')
}
let d = 99;
if (d < 100) {
    console.log('100未満')
}
let e = 100;
if (e == 100) {
    console.log('100と等しい')
}

// if else

let g = 99;
if (g >= 100) {
    console.log('100以上')
} else {
    console.log('100以上ではない')
}

// else if
let x = 6;
if (x >= 90) {
    console.log('A');
} else if (x >= 80) {
    console.log('B');
} else if (x >= 60) {
    console.log('C');
} else {
    console.log('D')
}
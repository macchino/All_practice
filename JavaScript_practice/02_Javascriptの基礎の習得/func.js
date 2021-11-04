'use strict';
function rectangle(height, width) {
    return height * width;
}
console.log(rectangle(3, 5));

const getRectangl = function(height, width) {
    return height * width;
}

console.log(getRectangl(3, 5));

// const getRectangle
// = new Function('height', 'width', 'return height * width');

// console.log(getRectangl(3, 5));

const getRectangle = (height, width) => {
    return height * width;
};
console.log(getRectangle(3, 5));

function getPrice(unitPrice, n) {
    return unitPrice * n;
};
console.log(getPrice(100, 20));


// const displayMessage = function () {
//     console.log('Timeout!');
// }
// setTimeout(displayMessage, 3000);

// function greeting(name) {
//     console.log('Hello' + name + '-san.');
// }

// function inputUserName(callback) {
//     let name = prompt('あなたのお名前を入力してください');
//     callback(name);
// }

// inputUserName(greeting);

let colors = ['Red', 'Green', 'Blue'];
console.log(colors);
console.log(colors[0]);
console.log(colors[1]);
console.log(colors[2]);
console.log(colors[3]);

let arr = [1, '2', 3, ['a', 'b', 'c']]
console.log(arr);

console.log(colors.length);
console.log(colors[colors.length -1]);

let emptyArr = []
console.log(emptyArr);

colors.push('black');
console.log(colors);

colors.unshift('white')
console.log(colors);

colors[1] = 'Aka';
console.log(colors);

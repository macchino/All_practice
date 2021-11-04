'use strict';
// class属性を追加・更新（赤）
let setRedClassButton = document.getElementById('setRedClassButton');
console.log(setRedClassButton)
setRedClassButton.addEventListener('click', function (e) {
    let showText = document.getElementById('showText');
    showText.setAttribute('class', 'red');
}, false
);

// class属性を追加・更新（青）

let setBlueClassButton = document.getElementById('setBlueClassButton');
console.log(setBlueClassButton)
setBlueClassButton.addEventListener('click', function (e) {
    let showText = document.getElementById('showText');
    showText.setAttribute('class', 'blue');
}, false
);

// 属性の削除
let removeClassButton = document.getElementById('removeClassButton');
console.log(removeClassButton)
removeClassButton.addEventListener('click', function (e) {
    let showText = document.getElementById('showText');
    showText.removeAttribute('class');
}, false
);
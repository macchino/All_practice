'use strict';

// let btn = document.getElementById('triggerButton');
// btn.addEventListener('click', function (e) {
    // alert('clicked!');
    // IDによるノードの取得
    // let headerTitle = document.getElementById('headerTitle');
    // console.log(headerTitle);
    // コンテンツの取得
//     console.log(headerTitle.textContent);
// }, false);

// let btn = document.getElementById('triggerButton');
// btn.addEventListener('click', function (e) {
//     // IDによるノードの取得
//     let headerTitle = document.getElementById('headerTitle');
//     // テキストの置換
//     headerTitle.textContent = 'タイトルが変更されました';

// }, false);


let btn = document.getElementById('triggerButton');
btn.addEventListener('click', function (e) {
     // IDによるノードの取得
    let inputColorName = document.getElementById('inputColorName');
    // 取得したinput要素の入力値を取得
    let colorNameText = inputColorName.value;
    // 取得したinput要素のname属性値を取得
    let inputName = inputColorName.getAttribute('name');
    // idがshowTextのp要素を取得
    let showText = document.getElementById('showText');
    // 出力
    showText.textContent = `name属性: ${inputName}, 入力されたテキスト: ${colorNameText}`;
}, false);
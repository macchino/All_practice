'use scrict';
window.console.log('Hello');

// 警告表示
// window.alert('Are You OK?');

// 確認ダイアログ
// window.confirm('Are You OK?');

// 別のwindowを開く
// window.open('https://google.com');

// windowを閉じる
// window.close();

// scroll
let btn = document.getElementById('triggerButton');
btn.addEventListener('click', function (e) {
    window.scroll(0, 300);
}, false);


'use scrict';

let btn = document.getElementById('triggerButton');
btn.addEventListener('click', function (e) {
    let elements = document.getElementsByClassName(' foo ');
    console.log(elements);
    for(let i = 0; i < elements.length; i++) {
        console.log(elements[i].textContent);
    };

    let elements1 = document.querySelector('.foo');
    console.log(elements1);

    let elements2 = document.querySelectorAll('.foo');
    console.log(elements2);
    for (let e = 0; e < elements2.length; e++) {
        console.log(elements2[e].textContent);
    }
}, false);


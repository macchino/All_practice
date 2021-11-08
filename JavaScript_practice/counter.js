'use strict';

let num = 0;
function updateCounter(n) {
    const counter = document.getElementById('counter');
    counter.textContent = n;
}
function countUp() {
    num++;
    // const counter = document.getElementById('counter');
    // counter.textContent = num;
    updateCounter(num);
}

function reset() {
    num = 10;
    // const counter = document.getElementById('counter');
    // counter.textContent = num;
    updateCounter(num);
}


countUpButton.addEventListener('click', countUp, false);
ResetButton.addEventListener('click', reset, false);
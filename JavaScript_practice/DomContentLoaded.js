'user strict';

// DOMContentLoaded
document.addEventListener('DOMContentLoaded', function () {
    alert('DOMContentLoaded');
}, false);

// Load
window.onload = function () {
    const nowLoading = document.getElementById('nowLoading');
    nowLoading.style.display = 'none';
}
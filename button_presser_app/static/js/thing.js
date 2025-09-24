const colors = ["#FFB6C1", "#87CEFA", "#90EE90", "#FFD700", "#FFA07A", "#DDA0DD", "#20B2AA"];
let current = 0;

document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("press-btn");
    const bg = document.getElementById("background-container");
    if (btn && bg) {
        btn.addEventListener("click", function () {
            current = (current + 1) % colors.length;
            bg.style.backgroundColor = colors[current];
        });
    }
});

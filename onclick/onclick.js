const increase = document.getElementById("increase");
const reset = document.getElementById("reset");
const decrease = document.getElementById("decrease");
const random = document.getElementById("random");
const number = document.getElementById("head");
let count = 0;

increase.onclick = function() {
    count++;
    number.textContent = count;
}
decrease.onclick = function() {
    count--;
    number.textContent = count;
}
reset.onclick = function() {
    count = 0;
    number.textContent = count;
}
random.onclick = function() {
    count = Math.floor(Math.random() * 100) + 1;
    number.textContent = count;
}
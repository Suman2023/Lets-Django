let Count = 0;

document.querySelector("#counter").style.color = "grey";
function countUp() {
  Count++;
  const counter = document.getElementById("counter");
  counter.innerHTML = Count;
  countColor(Count);
}

function countDown() {
  Count--;
  const counter = document.getElementById("counter");
  counter.innerHTML = Count;
  countColor(Count);
}

function countColor(count) {
  const counter = document.querySelector("#counter");
  if (count == 0) {
    counter.style.color = "grey";
  } else if (count < 0) {
    counter.style.color = "red";
  } else {
    counter.style.color = "green";
  }
}

function formSubmit() {
  const name = document.querySelector("#name").value;
  alert(`Hello, ${name}`);
}

document.querySelector("form").onsubmit = formSubmit;

document.querySelectorAll("button").forEach((button) => {
  button.onclick = () => {
    const colorChange = document.querySelector("#changeColor");
    colorChange.innerHTML = button.dataset.value;
    colorChange.style.color = button.dataset.color;
  };
});
document.querySelector("select").onchange = function () {
  document.querySelector("#changeColor").style.color = this.value;
  document.querySelector("#changeColor").innerHTML = this.value;
};

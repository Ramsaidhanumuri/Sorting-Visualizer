var slider = document.getElementById("a_size");
var output = document.getElementById("a_size_value");
output.innerHTML = slider.value;

slider.oninput = function array_size() {
  output.innerHTML = this.value;
}

var slider1 = document.getElementById("a_speed");
var output1 = document.getElementById("a_speed_value");
output1.innerHTML = slider1.value;

slider1.oninput = function array_speed() {
  output1.innerHTML = this.value;
}
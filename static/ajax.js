// alert("ajax.js в деле!");

var databox;
function initiate() {
  databox = document.getElementById("databox");

  var button = document.getElementById("button");
  button.addEventListener("click", read);
}
function read() {
  // var url = "textfile.txt"; // bad path
  // var url = "/static/textfile.txt"; // good path <<<<<<<< =====================
  // var url = "{{ login }}"; // not path
  // var url = "{% static '.\textfile.txt' %}";
  var url = document.getElementById("myVar").value;

  var request = new XMLHttpRequest();
  request.addEventListener("load", show);
  request.open("GET", url, true);
  request.send(null);
}
function show(event) {
  var data = event.target;
  if (data.status == 200) {
    databox.innerHTML = data.responseText;
  }
}
window.addEventListener("load", initiate);
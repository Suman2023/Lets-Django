// for index.html

document.querySelector("#room-name-input").focus();
document.querySelector("#room-name-input").onkeyup = (e) => {
  if (e.keyCode == 13) {
    //it represents enter key
    document.querySelector("#room-name-submit").click();
  }
};

document.querySelector("#room-name-submit").onclick = (e) => {
  var roomName = document.querySelector("#room-name-input").value;
  window.location.pathname = "/chat/" + roomName + "/";
};

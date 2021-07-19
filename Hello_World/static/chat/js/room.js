//room.html
const roomName = JSON.parse(document.getElementById("room-name").textContent);

// if we use this websocket everything gets erased on reload
// const chatSocket = new WebSocket(
//   "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
// );

//Instead use this
const chatSocket = new ReconnectingWebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

chatSocket.onmessage = (e) => {
  const data = JSON.parse(e.data);
  console.log(data);
  document.querySelector("#chat-log").value += data.message + "\n";
};

chatSocket.onclose = (e) => {
  console.error("Something went wrong in our side :(");
};

document.querySelector("#chat-message-input").focus();
document.querySelector("#chat-message-input").onkeyup = (e) => {
  if (e.keyCode == 13) {
    //it represents enter key
    document.querySelector("#chat-message-submit").click();
  }
};

document.querySelector("#chat-message-submit").onclick = (e) => {
  const messageInputDom = document.querySelector("#chat-message-input");
  const message = messageInputDom.value;
  chatSocket.send(
    JSON.stringify({
      message: message,
      command: "new_message",
    })
  );
  messageInputDom.value = "";
};

let ws = new WebSocket("ws://localhost:3000");

// for(let i = 0; i < 1000; i++) {
//     if (ws.readyState === WebSocket.OPEN) {
//         ws.send("hello");
//     } else {
//         console.warn("websocket is not connected");
//     }
// }



ws.addEventListener(
    "open", event => {
        console.log("Websocket opened!");
        while(1) {
            let i = (prompt("Enter a number: ")??"0");
            ws.send(i.toString());
        }
      }
)

ws.addEventListener(
    "message", event => {
        // let param = await Bun.stdin("Enter a message: ");
        
        console.log(event.data);
    }
)
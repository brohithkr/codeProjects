console.log("Hello via Bun!");

let app = Bun.serve<string>({
    async fetch(req, server) {
        server.upgrade(req)
        return new Response("Hello via Bun!");
    },
    websocket: {
        open: (ws) => {
            console.log("Websocket opened!");
            // ws.send("Hello via Bun!");
        },
        message: (ws, message) => {
            console.log("Websocket message!");
            ws.send(`Heard you: ${message}`);
        },
        close: (ws) => {
            console.log("Websocket closed!");
        }
    }
})

console.log(`Listening on http://${app.hostname}:${app.port}`);
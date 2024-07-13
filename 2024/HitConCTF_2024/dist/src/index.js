import { $ } from "bun";

const server = Bun.serve({
    host: "0.0.0.0",
    port: 1337,
    async fetch(req) {
        const url = new URL(req.url);
        if (url.pathname === "/") {
            return new Response(`
                <p>Welcome to echo-as-a-service! Try it out:</p>
                <form action="/echo" method="POST">
                    <input type="text" name="msg" />
                    <input type="submit" value="Submit" />
                </form>
            `.trim(), { headers: { "Content-Type": "text/html" } });
        }
        else if (url.pathname === "/echo") {
            const msg = (await req.formData()).get("msg");
            if (typeof msg !== "string") {
                return new Response("Something's wrong, I can feel it", { status: 400 });
            }

            const output = await $`echo ${msg}`.text();
            return new Response(output, { headers: { "Content-Type": "text/plain" } });
        }
    }
});

console.log(`listening on http://localhost:${server.port}`);

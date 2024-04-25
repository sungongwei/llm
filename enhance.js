const OpenAI = require("openai").default;
const { HttpsProxyAgent } = require("https-proxy-agent");

const openai = new OpenAI({
  httpAgent: new HttpsProxyAgent('http://127.0.0.1:7890')
});

async function main() {
  console.log("Starting...");
  const completion = await openai.chat.completions.create({
    messages: [{ role: "user", content: "You are a helpful assistant." }],
    model: "gpt-3.5-turbo",
  });

  console.log(completion.choices[0]);
}

main();

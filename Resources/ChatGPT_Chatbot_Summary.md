# OpenAI ChatGPT Chatbot — Quick Summary

This guide summarizes the official OpenAI docs for building a simple ChatGPT-style chatbot using the Chat Completions API, with quick-start steps for Node.js and Python.

## Official Docs (Links)
- Chat Completions Guide: https://platform.openai.com/docs/guides/chat-completions
- Chat API Reference: https://platform.openai.com/docs/api-reference/chat
- Quickstart: https://platform.openai.com/docs/quickstart
- OpenAI Node SDK: https://github.com/openai/openai-node
- OpenAI Python SDK: https://github.com/openai/openai-python

Note: Direct download of some platform docs was blocked in this environment, so the SDK READMEs are saved locally instead.

## Prerequisites
- OpenAI account and API key from https://platform.openai.com/api-keys
- Set the environment variable before running code:
  - Windows (PowerShell): `setx OPENAI_API_KEY "<your-key>"`
  - macOS/Linux (bash): `export OPENAI_API_KEY="<your-key>"`
- Recommended: Node.js 18+ or Python 3.9+

## Install SDKs
- Node.js: `npm install openai`
- Python: `pip install openai`

## Minimal Chatbot Example

### Node.js
```js
import OpenAI from "openai";
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await openai.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Say hello in one short sentence." }
  ],
});

console.log(response.choices[0].message.content);
```

### Python
```python
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello in one short sentence."},
    ],
)

print(resp.choices[0].message.content)
```

## Prompt Structure (messages)
- `system`: sets behavior and tone (e.g., role, style)
- `user`: end-user input
- `assistant`: model replies (you usually don’t include this on the first request)

Keep prompts concise and include clear instructions. For multi-turn chat, append prior messages to maintain context.

## Model Selection
- Start with `gpt-4o-mini` for cost-effective, fast chat.
- For higher quality reasoning, consider `gpt-4o`.

## Streaming (Optional)
- Both SDKs support streaming tokens for responsive UIs.
- See the SDK READMEs for streaming examples.

## Safety and Error Handling
- Never hardcode API keys; use environment vars or a secret manager.
- Add retries (e.g., 429 rate limits), timeouts, and logging.
- Validate/limit user input to avoid prompt injection issues.

## Basic CLI or Web Server Pattern
- CLI: read from stdin in a loop, push `user` messages, print assistant replies.
- Web: create an endpoint that accepts a message, calls Chat Completions, and returns the assistant’s reply; maintain session context per user.

## Costs and Limits
- Monitor usage at https://platform.openai.com/usage
- Set budgets/limits; choose models to balance cost, speed, and quality.

```
This summary is based on the official OpenAI documentation and SDK READMEs. For the most accurate, up-to-date details, consult the official docs links above.
```

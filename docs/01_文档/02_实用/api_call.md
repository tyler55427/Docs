# API 调用格式对比：OpenAI Completions / Responses / Anthropic Messages

三种格式的核心区别：**OpenAI Completions 是"古董"，OpenAI Responses 是"未来"，Anthropic Messages 是"另一套体系"**。

## 一、端点命名由来

### `/v1` 是什么

`/v1` 是 **API 版本号**，放在 URL 路径里。当接口有破坏性变更时，不用换域名，只换路径版本。老用户继续请求 `/v1` 不受影响，新用户用 `/v2`，两套并存。

> 也有公司把版本放在请求头里——Anthropic 就是 `anthropic-version: 2023-06-01`，它的 `/v1` 只是约定，真正的版本在 header。

### 为什么多一层 `/chat`

```
/v1                  ← 版本
   /completions          ← 旧"文本补全"（输入 prompt）
   /chat/completions     ← 对话补全（输入 messages）
   /responses            ← 新一代智能体接口
   /embeddings /images   ← 其他资源
```

1. 最早只有 `/v1/completions`——你传一个 `prompt` 字符串，模型接着写。**不分角色**，不支持多轮对话。
2. ChatGPT 出现后，需要区分 `user` / `assistant` / `system` 角色，输入格式完全不同。OpenAI 没有去改老接口（那会弄坏所有老代码），而是**新增了一个端点**：`/v1/chat/completions`。
3. 现在 `/v1/responses` 是最新一代，目标是**取代上面两个**。

> 一句话：`/v1` 是版本号，`chat` 是"对话"这个分支。多出这一层完全是为了向后兼容——老的"裸补全"不能删，对话接口只能另起一个路径。

## 二、核心差异

| | OpenAI Completions | OpenAI Responses | Anthropic Messages |
| :--- | :--- | :--- | :--- |
| **端点** | `POST /v1/completions` | `POST /v1/responses` | `POST /v1/messages` |
| **理念** | 文本补全，模型接着写 | 智能体工作流，能自主用工具 | 对话交互，Claude 原生接口 |
| **输入格式** | `prompt` 字符串 | `input` 项目列表 | `messages` 数组，`system` 在顶层 |
| **状态管理** | 无状态 | 有状态（`previous_response_id`） | 无状态，需自行传完整历史 |
| **内建工具** | 不支持 | 平台自动执行（搜索/文件/代码解释器） | 支持工具调用，但执行需自己托管 |
| **独有功能** | — | 服务端状态管理 | 扩展思考(thinking)、提示词缓存(cache_control) |

## 三、代码示例

### 1. OpenAI Completions（旧版文本补全）

```bash
curl https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo-instruct",
    "prompt": "什么是机器学习？",
    "max_tokens": 100
  }'
```

```python
import openai

response = openai.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="什么是机器学习？",
    max_tokens=100,
)
print(response.choices[0].text)
```

```json
// 响应格式
{
  "id": "cmpl-xxx",
  "object": "text_completion",
  "choices": [
    {
      "text": "机器学习是人工智能的一个分支...",
      "index": 0
    }
  ],
  "usage": { "prompt_tokens": 5, "completion_tokens": 30, "total_tokens": 35 }
}
```

### 2. OpenAI Chat Completions（对话——最通用）

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "你是一个助手。"},
      {"role": "user", "content": "什么是机器学习？"}
    ]
  }'
```

```python
import openai

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是一个助手。"},
        {"role": "user", "content": "什么是机器学习？"},
    ],
)
print(response.choices[0].message.content)
```

```json
// 响应格式
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "机器学习是人工智能的一个分支..."
      }
    }
  ],
  "usage": { "prompt_tokens": 20, "completion_tokens": 50, "total_tokens": 70 }
}
```

### 3. OpenAI Responses（新一代智能体）

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "input": "搜索一下量子计算的最新进展",
    "tools": [{"type": "web_search"}]
  }'
```

```python
import openai

response = openai.responses.create(
    model="gpt-4o",
    input="搜索一下量子计算的最新进展",
    tools=[{"type": "web_search"}],
)
print(response.output)
```

### 4. Anthropic Messages（Claude 原生）

```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-5",
    "max_tokens": 1024,
    "system": "你是一个助手。",
    "messages": [
      {"role": "user", "content": "什么是机器学习？"}
    ]
  }'
```

```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    system="你是一个助手。",
    messages=[
        {"role": "user", "content": "什么是机器学习？"},
    ],
)
print(response.content[0].text)
```

```json
// 响应格式
{
  "id": "msg_xxx",
  "type": "message",
  "role": "assistant",
  "content": [
    {"type": "text", "text": "机器学习是人工智能的一个分支..."}
  ],
  "model": "claude-sonnet-5",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 20,
    "output_tokens": 50
  }
}
```

## 补充：各端点关键差异

| 对比项 | OpenAI Chat Completions | Anthropic Messages |
| :--- | :--- | :--- |
| `system` 位置 | 在 `messages` 数组内，`role: "system"` | 顶层 `system` 字段，独立于 `messages` |
| 认证方式 | `Authorization: Bearer` | `x-api-key`（或 `Authorization: Bearer` + OAuth header） |
| 响应内容 | `choices[0].message.content` | `content[0].text`（content 是数组） |
| 版本管理 | 路径版本 `/v1/` | 路径版本 + 请求头 `anthropic-version` |
# API 调用方式对比

## 一、接口格式对比

三种格式的核心区别：**OpenAI Completions 是“古董”，OpenAI Responses 是“未来”，Anthropic Messages 是“另一套体系”**。

#### 1.1 端点命名由来

| 层级              | 端点                           | 说明                                                                                                                   |
| :---------------- | :----------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **版本**    | `/v1`                        | API 版本号，放在 URL 路径中。<br />破坏性变更时新旧版本并存，老用户继续用`/v1`，新用户用 `/v2`。                   |
| ├─ 旧版补全     | `/completions`               | 最早期的接口，传`prompt` 字符串，模型接着写。<br />**不分角色**，不支持多轮对话。现已过时。                    |
| ├─ 对话补全     | `/chat/completions`          | ChatGPT 时代新增。<br />输入`messages` 数组，支持 `user` / `assistant` / `system` 角色区分。<br />目前最通用。 |
| ├─ 新一代智能体 | `/responses`                 | 最新接口，支持有状态管理、内建工具自动执行。<br />目标是在未来**取代上面两个**。                                 |
| └─ 其他资源     | `/embeddings` `/images` 等 | 文本向量化、图像生成等其他能力分支。                                                                                   |

#### 1.2 核心差异总览

|                    | OpenAI Completions       | OpenAI Chat Completions       | OpenAI Responses                             | Anthropic Messages                            |
| :----------------- | :----------------------- | :---------------------------- | :------------------------------------------- | :-------------------------------------------- |
| **端点**     | `POST /v1/completions` | `POST /v1/chat/completions` | `POST /v1/responses`                       | `POST /v1/messages`                         |
| **定位**     | 文本补全（已过时）       | 对话交互（当前最通用）        | 智能体工作流（未来方向）                     | Claude 原生接口                               |
| **输入格式** | `prompt` 字符串        | `messages` 数组             | `input`（字符串或项目列表）                | `messages` 数组 + 顶层 `system`           |
| **状态管理** | 无状态                   | 无状态，需自行传完整历史      | **有状态**（`previous_response_id`） | 无状态，需自行传完整历史                      |
| **内建工具** | 不支持                   | 需自行编排工具调用循环        | **平台自动执行**（搜索/文件/代码）     | 支持工具调用，但执行需自己托管                |
| **独有功能** | —                       | —                            | 服务端状态管理                               | 扩展思考(thinking)、提示词缓存(cache_control) |

#### 1.3 文本输入参数对比

| 对比项                    | OpenAI Completions    | OpenAI Chat Completions            | OpenAI Responses                | Anthropic Messages                      |
| :------------------------ | :-------------------- | :--------------------------------- | :------------------------------ | :-------------------------------------- |
| **顶层必填参数**    | `model`, `prompt` | `model`, `messages`            | `model`, `input`            | `model`, `messages`, `max_tokens` |
| **System 指令位置** | 无（不支持）          | `messages` 内 `role: "system"` | `instructions` 顶层字段       | 顶层`system` 字段                     |
| **对话历史传递**    | 不支持多轮            | 全部放在`messages` 数组          | 用`previous_response_id` 继承 | 全部放在`messages` 数组               |
| **最大输出控制**    | `max_tokens`        | `max_tokens`                     | `max_output_tokens`           | `max_tokens`（必填）                  |
| **温度参数**        | `temperature`       | `temperature`                    | `temperature`                 | `temperature`                         |
| **响应内容路径**    | `choices[0].text`   | `choices[0].message.content`     | `output` 数组                 | `content[0].text`（数组）             |

---

#### 1.4 图像输入（多模态）参数对比

目前 **OpenAI Completions 不支持图像输入**（那是上古接口），以下对比其余三种：

| 对比项                 | OpenAI Chat Completions (GPT-4o)                       | OpenAI Responses (GPT-4o)                       | Anthropic Messages (Claude 3/4)                                                                |
| :--------------------- | :----------------------------------------------------- | :---------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| **图像传递方式** | 放在`messages` 的 `content` 数组中                 | 放在`input` 的 `content` 数组中             | 放在`messages` 的 `content` 数组中                                                         |
| **图像来源**     | URL 或 Base64                                          | URL 或 Base64                                   | URL 或 Base64                                                                                 |
| **参数格式**     | `{"type": "image_url", "image_url": {"url": "..."}}` | `{"type": "input_image", "image_url": "..."}` | `{"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": "..."}}` |
| **多图支持**     | 支持，放多个对象即可                                   | 支持                                            | 支持，放多个对象即可                                                                           |
| **图像尺寸限制** | 每张图 ≤ 20MB，边长 ≤ 20000px                        | 同左                                            | 每张图 ≤ 10MB，建议 ≤ 1.5MP                                                                  |

- URL 与 Base64 的区别
  - URL 只传地址，API 服务器**自己回源下载**图片
  - Base64 把图片二进制**编码成字符串，直接塞进请求体**

## 二、调用方式示例

同一个接口可以用不同“工具”去调用。

以下以 **OpenAI Chat Completions（当前最通用）** 为例，展示三种调用方式。

三种调用方式的核心区别：**Python SDK 是“写代码”，cURL 是“敲命令”，HTTP Client 是“发请求”**。

| 特性                 | **Python SDK**          | **cURL（命令行）**       | **HTTP Client（如 requests）** |
| :------------------- | :---------------------------- | :----------------------------- | :----------------------------------- |
| **一句话定位** | 编程库，封装了底层 HTTP 细节  | 命令行工具，直接发送 HTTP 请求 | 编程库，手动构造 HTTP 请求           |
| **优点**       | 代码最简洁，自动处理重试/认证 | 调试最快，无需编程环境         | 灵活性最高，可精细控制 HTTP 层       |
| **缺点**       | 需要 Python 环境              | 命令冗长，不适合复杂逻辑       | 需自己处理 HTTP 细节（错误码、重试） |
| **适用场景**   | 生产代码、项目集成            | 快速测试、接口连通性检查       | 非 Python 语言、需要精细控制请求     |

###### 2.1 Python SDK

```python
from openai import OpenAI

client = OpenAI(
  api_key="sk-xxx", 
  base_url="https://api.openai.com/v1"
)

# client = base_url，点号即路径：client.chat.completions.create = base_url + /chat/completions
# 通过SDK补全api路径
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是一个助手。"},
        {"role": "user", "content": "什么是机器学习？"}
    ],
    temperature=0.7,
    max_tokens=100,
)

print(response.choices[0].message.content)
```

###### 2.2 cURL 命令

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "你是一个助手。"},
      {"role": "user", "content": "什么是机器学习？"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
  }'
```

返回结构（`choices[0].message.content` 即正文）：

```json
{
  "id": "chatcmpl-xxx",
  "model": "gpt-4o",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "机器学习是..."
      },
      "finish_reason": "stop"
    }
  ]
}
```

###### 2.3 Python + requests（手动 HTTP）

```python
import requests

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-xxx",
}
data = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "你是一个助手。"},
        {"role": "user", "content": "什么是机器学习？"}
    ],
    "temperature": 0.7,
    "max_tokens": 100,
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result["choices"][0]["message"]["content"])
```

###### 2.4 CLI（如 Claude Code）

CLI 类工具把"发请求"这件事彻底藏起来，甚至连 `base_url` 都不用写——**路径由 SDK/框架自动补全**。

- OpenAI SDK 是 `base_url` + `.chat.completions.create`
- Anthropic SDK 则是固定发 `POST /v1/messages`，写代码时看不到这个路径，只有抓包才知道。

```bash
claude --print "什么是机器学习？"
# 等价于请求 https://api.anthropic.com/v1/messages
```

---

## 三、特殊调用

基础文本调用之外，还有两类常用能力：**图像输入**和**工具调用**。

这里都只给 cURL，因为请求体和语言无关。

### 3.1 图像输入：URL 与 Base64

**URL 传图**（OpenAI Chat Completions）

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": [
        {"type": "text", "text": "这张图里有什么？"},
        {"type": "image_url", "image_url": {"url": "https://example.com/photo.jpg"}}
      ]}
    ]
  }'
```

**Base64 传图**（OpenAI Chat Completions，`data:` 前缀必须带）

```bash
IMG_B64=$(base64 -w 0 photo.jpg)

curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d "{
    \"model\": \"gpt-4o\",
    \"messages\": [
      {\"role\": \"user\", \"content\": [
        {\"type\": \"text\", \"text\": \"这张图里有什么？\"},
        {\"type\": \"image_url\", \"image_url\": {\"url\": \"data:image/jpeg;base64,$IMG_B64\"}}
      ]}
    ]
  }"
```

本地图片文件转 Base64：

```python
import base64

with open("photo.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")
# img_b64 里不带 data: 前缀；OpenAI 拼进 url 时自己加，Anthropic 直接放 data 字段
```

### 3.2 工具调用

模型不会自己执行工具，它只**输出"我想调哪个工具、参数是什么"**；执行完你要把结果作为一条 `role: "tool"` 的消息回传，模型才能接着往下写。

所以这是一个**循环**：请求 → 返回 → 本地执行 → 结果回传 → 请求。

`tool_choice` 控制行为：`auto`（模型自己判断，默认）、`none`（禁用）、`required`（强制至少调一个）、`{"type": "function", "function": {"name": "..."}}`（强制指定某个）。

**第一步 请求：声明工具**

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "北京现在几点了？"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_current_time",
          "description": "获取指定城市的当前时间",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {"type": "string", "description": "城市名，如 北京"}
            },
            "required": ["city"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

**第二步 返回：模型要求调用**

`finish_reason` 是 `"tool_calls"` 而不是 `"stop"`，这就是循环的信号——不要当最终答案用。

```json
{
  "id": "chatcmpl-xxx",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        {
          "id": "call_abc123",
          "type": "function",
          "function": {
            "name": "get_current_time",
            "arguments": "{\"city\": \"北京\"}"
          }
        }
      ]
    },
    "finish_reason": "tool_calls"
  }]
}
```

**第三步 本地执行**

解析 `arguments`，调用自己的函数：`get_current_time("北京")` → `"14:30"`。

**第四步 结果回传：补上工具结果再问一次**

把第二步里的 `assistant` 消息**原样带回**，再追加一条 `role: "tool"` 的消息，`tool_call_id` 对应第二步的 `call_abc123`。

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "北京现在几点了？"},
      {"role": "assistant", "content": null, "tool_calls": [
        {
          "id": "call_abc123",
          "type": "function",
          "function": {"name": "get_current_time", "arguments": "{\"city\": \"北京\"}"}
        }
      ]},
      {"role": "tool", "tool_call_id": "call_abc123", "content": "14:30"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_current_time",
          "description": "获取指定城市的当前时间",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {"type": "string", "description": "城市名，如 北京"}
            },
            "required": ["city"]
          }
        }
      }
    ]
  }'
```

这次返回的 `finish_reason` 是 `"stop"`，`content` 里就是最终答案——循环结束。

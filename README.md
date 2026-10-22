# 微信私人伴侣 · WeChat Private Companion

一个只监听私聊的微信陪伴型 AI。默认人设是中性的「私人陪伴者」，**不预设角色、不预设性别、不假设用户是男性或女性**，适合朋友式陪聊、情绪倾听和日常聊天。人设、称呼、语气都可以自己改。

> 仓库不包含任何角色设定、聊天记录、账号配置、API Key 或表情包图片，只保留代码和接口。

## 特点

- **只走私聊**：不监听群，不抢群聊的话；需要时也可以自己加群。
- **用户不限性别**：提示词不假设对方性别、年龄、关系状态，不使用“男朋友 / 女朋友 / 老公 / 老婆”定义关系。
- **通用陪伴**：默认朋友式陪伴；对方明确想要更亲密的关系时，先确认边界。
- **人设可定制**：`persona.txt` 是空模板，默认人设写在 `config.py` 的 `SYSTEM_PROMPT`。
- **OpenAI 兼容模型**：DeepSeek、GLM、Qwen、Kimi、Ollama 等兼容接口都能接。
- **图片识别**：对方发图片时先看懂图，再结合内容回应。
- **表情包接口**：代码支持标签表情，但仓库不带任何图片素材。
- **隐私优先**：配置、日志、聊天缓存都在本地，且默认不提交。

## 快速开始

```bash
git clone https://github.com/XXXzhouhan/wechat-private-companion.git
cd wechat-private-companion

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

1. 复制 `.env.example` 为 `.env`，填模型地址、Key、模型名。
2. 微信小号登录 PC 微信（微信 4.1.12+，4.1.15.53 已验证）。
3. 双击 `启动助手.bat`，打开桌面 APP。
4. 在「基础设置」填私聊联系人（微信备注 / 昵称 / wxid），保存。
5. 点「重启接管」，在私聊里发：`小伴 在吗`。

APP 和 `run.bat` 不要同时开。关掉 APP 窗口会退出接管并恢复微信窗口。

## 配置说明

首次运行没有 `config_local.py`，APP 保存后会生成；它已被 `.gitignore` 忽略。

| 项目 | 默认 | 说明 |
|---|---|---|
| `GROUPS` | `[]` | 群名列表；只私聊就留空 |
| `PRIVATE_CHATS` | `[]` | 私聊联系人，填备注 / 昵称 / wxid |
| `PRIVATE_TRIGGER_MODE` | `all` | `all` 每条都回；`smart` 回过后追问；`keyword` 叫名字才回 |
| `BOT_NAMES` | `["小伴"]` | 机器人昵称，可改成你喜欢的名字 |
| `KEYWORDS` | `["小伴", "伴侣"]` | 群聊触发关键词；私聊 `all` 模式不需要 |
| `MAX_REPLY_CHARS` | `200` | 单条回复上限 |
| `PRIVATE_CONTEXT_SIZE` | `300` | 私聊上下文条数 |
| `STICKER_CHANCE` | `0.25` | 闲聊后补表情的概率（需要有素材） |
| `MEME_ENABLE` | `False` | 默认关闭联网热梗，保持人设稳定 |
| `SEARCH_ENABLE` | `False` | 默认关闭联网搜索，避免回复变成搜索总结 |

## 自定义人设

打开 `persona.txt`，把注释行前面的 `#` 去掉再改；以 `#` 开头的行不会生效。也可以直接在 APP 的「人设」页编辑。

建议写清楚：

- 角色叫什么、是什么身份
- 说话长度、语气、口头禅
- 关系定位（朋友 / 陪伴者 / 对方希望的其他关系）
- 边界与禁忌
- 2-4 组简短示例

不要把性别、年龄、职业等假设强加给用户；如果角色需要性别，也请让用户自己选。

## 表情包接口

`stickers/` 只保留接口，默认没有图片。放自己的素材：

```
标签_名字.png
```

支持的标签由文件名决定，例如：害羞、卖萌、傲娇、比心、可爱、开心、日常、摸鱼。`categories.json` 可以把细标签归到大类，默认 `{}`。

详见 [`stickers/README.md`](stickers/README.md)。

## 安全与边界

- 不写露骨性内容，不引导色情角色扮演。
- 不情感操控、不制造愧疚、不用离开或自伤威胁挽留。
- 不索取金钱、礼物、账号密码、照片、住址等隐私。
- 对方明显未成年：切换成朋友模式。
- 出现自伤、自杀或严重危机信号：退出陪伴角色，优先安全，建议联系可信任的人或当地急救 / 心理援助热线。
- 不宣称能替代现实关系或专业心理咨询。

## 隐私

- 仓库不包含 `.env`、`config_local.py`、日志、聊天缓存、表情图片或任何个人数据。
- 聊天内容会发送给你配置的模型 API，不是纯本地推理。
- 不要用主力微信号；桌面自动化存在限流、封号风险，请使用小号并控制频率。
- 若你 fork 本项目，提交前请检查 `git status`，不要把 `.env` 或聊天记录推上去。

## 关键词 / Keywords

**中文**：微信私人伴侣、微信 AI 陪伴、微信聊天机器人、微信自动回复、私聊机器人、私有部署、自定义人设、不限性别、情感陪伴、陪聊、树洞、微信小号、后台回复、图片识别、OpenAI 兼容、DeepSeek、隐私优先、开源。

**English**: WeChat companion bot, AI companion, private chatbot, self-hosted chatbot, customizable persona, gender-neutral companion, emotional support bot, OpenAI-compatible, DeepSeek, Windows automation, privacy-first, open source.

> GitHub Topics 建议：`wechat-bot` `ai-companion` `private-companion` `self-hosted` `chatbot` `llm` `openai-compatible` `deepseek` `windows` `privacy` `chinese`

## 目录

| 文件 | 作用 |
|---|---|
| `app.py` | 桌面启动助手 / 配置界面 |
| `bot.py` | 微信监听与回复主程序 |
| `config.py` | 默认配置与通用系统提示词 |
| `persona.txt` | 人设模板（默认空） |
| `.env.example` | 模型配置示例 |
| `stickers/` | 表情包接口（不含图片） |
| `memes.py` / `search.py` | 可选的热梗 / 联网搜索模块 |

## 免责声明

本项目与腾讯、DeepSeek 及其关联公司没有隶属、合作或背书关系。“微信”“DeepSeek”等名称仅用于说明程序读取或调用的对象，商标归其权利人所有。

微信个人号自动化可能违反平台规则，存在限流或封号风险；请自行评估并遵守当地法律与平台条款。本项目按 MIT 许可提供，不提供任何担保。

## License

MIT。第三方依赖与声明见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。

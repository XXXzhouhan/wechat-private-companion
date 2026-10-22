import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

BASE = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE, ".env")
LOCAL_PATH = os.path.join(BASE, "config_local.py")

PROVIDERS = {
    "1": ("智谱 GLM-4.7-Flash（免费）", "https://open.bigmodel.cn/api/paas/v4", "glm-4.7-flash"),
    "2": ("DeepSeek Chat（中间档，快）", "https://api.deepseek.com/v1", "deepseek-chat"),
    "3": ("通义千问", "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    "4": ("Kimi", "https://api.moonshot.cn/v1", "moonshot-v1-8k"),
    "5": ("本地 Ollama（完全免费，需装本地模型）", "http://localhost:11434/v1", "qwen2.5:7b"),
    "6": ("自定义", "", ""),
}


def ask(prompt, default=""):
    tip = f"{prompt}" + (f" [{default}]" if default else "")
    value = input(tip + "：").strip()
    return value or default


def split_names(text):
    for sep in ("，", ";", "；", "|"):
        text = text.replace(sep, ",")
    return [x.strip() for x in text.split(",") if x.strip()]


def main():
    print("=" * 56)
    print("微信私人伴侣 配置向导")
    print("=" * 56)
    print("提示：私聊联系人填微信备注/昵称/wxid，名字要和微信里一字不差。\n")

    private_chats = split_names(ask("1) 私聊联系人（备注/昵称/wxid，多个用逗号分隔）"))
    if not private_chats:
        print("私聊联系人不能为空。")
        return 1

    names = split_names(ask("2) 机器人昵称", "小伴"))
    if not names:
        print("机器人昵称不能为空。")
        return 1

    print("\n3) 选择模型服务：")
    for key, (label, _, model) in PROVIDERS.items():
        print(f"   {key}. {label}" + (f"（{model}）" if model else ""))
    choice = ask("   序号", "1")
    label, base_url, model = PROVIDERS.get(choice, PROVIDERS["1"])

    if choice == "6":
        base_url = ask("   接口地址（到 /v1 为止）", "https://api.deepseek.com/v1")
        model = ask("   模型名", "deepseek-chat")

    api_key = "ollama"
    if choice != "5":
        api_key = ask(f"   {label} 的 API Key").strip()
        if not api_key:
            print("API Key 不能为空（本地 Ollama 请选 5）。")
            return 1

    trigger = ask(
        "\n4) 私聊触发：all=每条都回（推荐） / smart=回过后继续追问 / keyword=叫名字才回",
        "all",
    )
    if trigger not in ("all", "smart", "keyword"):
        trigger = "all"

    print(f"\n接口：{base_url}")
    print(f"模型：{model}")
    print(f"Key ：{api_key[:6]}...{api_key[-4:]}" if len(api_key) > 12 else "Key ：已填写")
    print(f"私聊：{'、'.join(private_chats)}")
    print(f"昵称：{'、'.join(names)}")
    if ask("\n确认写入配置？(y/n)", "y").lower() not in ("y", "yes", ""):
        print("已取消。")
        return 1

    env_lines = [
        "# 由 configure.py 生成，请勿提交到 git",
        f"LLM_BASE_URL={base_url}",
        f"LLM_API_KEY={api_key}",
        f"LLM_MODEL={model}",
        "",
    ]
    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(env_lines))

    local_lines = [
        "# 由 configure.py 生成",
        "GROUPS = []",
        f"PRIVATE_CHATS = {private_chats!r}",
        f"PRIVATE_TRIGGER_MODE = {trigger!r}",
        f"BOT_NAMES = {names!r}",
        "TRIGGER_MODE = 'smart'",
        "",
    ]
    with open(LOCAL_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(local_lines))

    print("\n已写入 .env 和 config_local.py")
    print("下一步：")
    print("  双击 启动助手.bat           # 桌面 APP，打开自动接管")
    print("  python bot.py --test-llm    # 测模型")
    print("  python bot.py --doctor      # 测微信/私聊联系人")
    print("  python bot.py --dry-run     # 干跑")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n已取消。")
        sys.exit(1)


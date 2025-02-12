

# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI, APIError, AuthenticationError, Timeout, APIConnectionError

content_question = "在DRG2.0政策背景下，血液内科如何扭亏为盈，以及作为一名主治医生在日常工作中的操作建议"

try:

    client = OpenAI(api_key="sk-b487b362bdbc4c3ba4caf57ebbd61fa1", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": content_question},
        ],
        stream=False
    )

    print(response.choices[0].message.content)

except AuthenticationError as e:
    print(f"认证失败，请检查 API 密钥。错误信息：{e}")
except Timeout as e:
    print(f"请求超时，请检查网络连接或稍后重试。错误信息：{e}")
except APIConnectionError as e:
    print(f"无法连接到 API 服务器，请检查网络设置或 API 地址。错误信息：{e}")
except APIError as e:
    print(f"API 返回错误响应。错误信息：{e}")
except Exception as e:
    print(f"发生未知错误：{e}")

# 从 response 中提取要写入的内容
content_answer = response.choices[0].message.content

try:
    # 以写入模式打开文件，如果文件不存在则创建它
    with open('问答_chat.txt', 'a', encoding='utf-8') as file:
        # 将内容写入文件
        file.write(f"问题：{content_question}\n")
        file.write(f"回答：{content_answer}\n")
    print("内容已成功写入到问答.txt 文件。")
except Exception as e:
    print(f"写入文件时出现错误: {e}")
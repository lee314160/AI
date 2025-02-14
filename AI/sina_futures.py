import webbrowser
import os

# 定义要打开的网址列表
urls = [
    "https://www.doubao.com/chat/114020116519170",
    "https://rewards.bing.com/",
    "https://finance.sina.com.cn/",
    "https://finance.sina.com.cn/futuremarket/",
    "https://finance.sina.com.cn/futures/quotes/I0.shtml",
    "https://finance.sina.com.cn/futures/quotes/JM0.shtml",
    "https://finance.sina.com.cn/futures/quotes/Y0.shtml",
    "https://finance.sina.com.cn/futures/quotes/P0.shtml",
    "https://finance.sina.com.cn/futures/quotes/CF0.shtml",
]

# 尝试查找 Edge 浏览器的可执行文件路径
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]
edge_path = None
for path in edge_paths:
    if os.path.exists(path):
        edge_path = path
        break

if edge_path is None:
    print("未找到 Edge 浏览器可执行文件，请检查路径。")
else:
    # 注册 Edge 浏览器
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    # 打开每个网址
    for url in urls:
        webbrowser.get('edge').open(url)
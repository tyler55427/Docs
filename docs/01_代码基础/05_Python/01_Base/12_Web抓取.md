# Web 抓取

## 打开网页

```python
import webbrowser as w
w.open('http://www.baidu.com')
```

> `webbrowser` 只能"打开链接"，不能下载文件或解析页面内容；下载请用 `requests`、解析请用 `BeautifulSoup` / `lxml`。

## 下载文件

```python
import requests     # 需 pip install requests

url = 'https://example.com/file.zip'
with open('file.zip', 'wb') as f:
    f.write(requests.get(url).content)
```

## 简单爬虫骨架

```python
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://example.com')
resp.raise_for_status()                  # 状态码非 2xx 时抛异常
soup = BeautifulSoup(resp.text, 'html.parser')

for link in soup.select('a'):
    print(link.get('href'))
```
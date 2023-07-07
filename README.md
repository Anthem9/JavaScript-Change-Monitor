
# JavaScript Change Monitor
这个项目是一个简单但强大的 JavaScript 代码监控工具，可以监控指定网页上 JavaScript 的变化。当 JavaScript 发生变化时，会发送通知到指定的 url 。

## 安装
1. 首先，确保你已经安装了 Python 3.6 或更高版本。
2. 克隆这个仓库到你的本地机器上，然后进入该目录。
3. 使用以下命令安装所需的依赖：
```bash
pip install -r requirements.txt
```
## 配置
配置文件位于项目根目录下的 `config.json` 文件。这个文件应包含以下字段：
- xizhi_key: 接收通知的 URL 。
- url: 需要监控的网页的 URL 。
- check_interval: 检查 JavaScript 变化的间隔时间，以秒为单位。
例如：

```json
{
    "xizhi_key": "https://xizhi.qqoq.net/xxxxxxxxxxxxxxxxxxxxxxxxxx.send",
    "url": "https://to_be_monitored.com",
    "check_interval": 3600
}
```
## 运行
使用 Python 运行`monitor.py`文件：

```bash
python monitor.py
```
当检测到 JavaScript 代码变化时，控制台将输出变化的内容，并且向 xizhi_key 指定的 URL 发送通知。

## 注意
本项目旨在研究和学习目的，请确保你的使用符合所有适用的法律和政策。
请确保你有足够的权限访问和监控你设定的 URL ，避免违反任何隐私政策或使用协议。
## 贡献
欢迎提交 Pull 请求和 Issue 来改进本项目。在提交 Pull 请求之前，请确保你的代码已经过充分测试，并且和现有代码风格一致。

## 许可
本项目使用 MIT 许可证，详见 LICENSE 文件。
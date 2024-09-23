# 下载速度测试

### 描述
这个Python脚本允许用户测试从指定URL的下载速度。它测量以块下载数据所花费的时间，并计算平均下载速度（以KB/s为单位）。该脚本处理无法访问的URL的异常，并提供下载过程的反馈。

### 使用指南
#### 先决条件
- 系统上安装了Python 3.x
- `requests`库（使用`pip install requests`安装）

#### 使用步骤
1. **克隆仓库:**
   ```sh
   git clone https://github.com/mzpiyo/download-speed-test.git
   cd download-speed-test
   ```

2. **运行脚本:**
   ```sh
   python download_speed_test.py
   ```

3. **输入URL:**
   当提示时，输入你想测试下载速度的URL。

4. **查看结果:**
   脚本将显示耗时和平均下载速度（以KB/s为单位）。

#### 示例
```sh
请输入测速地址: https://example.com/file.zip
下载在 5.23 秒内完成。
平均下载速度: 195.34 KB/s
```

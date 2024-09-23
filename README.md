# download-speed-test

Englist | [简体中文](./README.zh-CN.md)

### Description
This Python script allows users to test the download speed from a specified URL. It measures the time taken to download data in chunks and calculates the average download speed in KB/s. The script handles exceptions for inaccessible URLs and provides feedback on the download process.

### Usage Guide
#### Prerequisites
- Python 3.x installed on your system
- `requests` library (install using `pip install requests`)

#### Steps to Use
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/mzpiyo/download-speed-test.git
   cd download-speed-test
   ```

2. **Run the Script:**
   ```sh
   python download_speed_test.py
   ```

3. **Input the URL:**
   When prompted, enter the URL you want to test the download speed for.

4. **View Results:**
   The script will display the elapsed time and the average download speed in KB/s.

#### Example
```sh
请输入测速地址: https://example.com/file.zip
下载在 5.23 秒内完成。
平均下载速度: 195.34 KB/s
```

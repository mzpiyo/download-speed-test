import requests
import time

# 测试下载速度的函数
def test_download_speed(url):
    start_time = time.time()
    try:
        response = requests.get(url, stream=True, timeout=10)
    except requests.exceptions.RequestException:
        print("无法访问地址。")
        return

    total_bytes = 0

    for chunk in response.iter_content(chunk_size=1024):
        total_bytes += len(chunk)
        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            print("测速完成。")
            break

    if elapsed_time <= 10:
        print(f"下载在 {elapsed_time:.2f} 秒内完成。")
        download_speed = total_bytes / elapsed_time / 1024  # KB/s
    else:
        download_speed = total_bytes / 10 / 1024  # KB/s

    print(f"平均下载速度: {download_speed:.2f} KB/s")

# 输入测速地址
url = input("请输入测速地址: ")

# 测试下载速度
test_download_speed(url)

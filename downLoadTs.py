import requests
from multiprocessing import Pool
import datetime


def mission(url, num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "origin": "https://www.22tu.tv",
        "referer": "https://www.22tu.tv/",
        "sec-ch-ua": 'hrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    }
    print("开始下载 %s" % num + ".ts")
    start = datetime.datetime.now().replace(microsecond=0)
    try:
        response = requests.get(url, headers=headers)
        # 获取文件的二进制代码
        data = response.content
        # 保存数据
        save_data(data, str(num))
        end = datetime.datetime.now().replace(microsecond=0)
        print("耗时：%s" % (end - start))
    except Exception as e:
        print("异常请求: %s" % e.args)


# 传入数据和名字
def save_data(data, num):
    num = num.zfill(4)
    with open(num + ".ts", "wb") as f:
        f.write(data)
        f.close()


if __name__ == "__main__":
    pool = Pool(15)
    for n in range(1, 1227):
        url = "https://www.hyxrzs.com/20210404/oZR8GUAa/oZR8GUAa{}.ts".format(n)
        #print(url)
        pool.apply_async(mission, (url, n))
    pool.close()
    pool.join()

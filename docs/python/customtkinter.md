
## customtkinter

```python title="main.py"
import json
import math
import os
import pathlib
import re
import socket
import sys
import threading
import time
import tkinter.messagebox
import urllib
import urllib.request
import urllib.parse
import urllib.error

import customtkinter

timeout = 5
socket.setdefaulttimeout(timeout)

class Crawler:
    # 睡眠时长
    __time_sleep = 0.1
    __amount = 0
    __start_amount = 0
    __counter = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0', 'Cookie': ''}
    __per_page = 30
    __out = "./"
    __ui = None

    # 获取图片url内容等
    # t 下载图片时间间隔
    def __init__(self, t=0.1):
        self.time_sleep = t

    # 获取后缀名
    @staticmethod
    def get_suffix(name):
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    @staticmethod
    def handle_baidu_cookie(original_cookie, cookies):
        """
        :param string original_cookie:
        :param list cookies:
        :return string:
        """
        if not cookies:
            return original_cookie
        result = original_cookie
        for cookie in cookies:
            result += cookie.split(';')[0] + ';'
        result.rstrip(';')
        return result

    # 保存图片
    def save_image(self, rsp_data, word):
        out_folder = os.path.join(self.__out, word)
        if not os.path.exists(out_folder):
            os.mkdir(out_folder)
        # 判断名字是否重复，获取图片长度
        self.__counter = len(os.listdir(out_folder)) + 1
        for image_info in rsp_data['data']:
            try:
                if 'replaceUrl' not in image_info or len(image_info['replaceUrl']) < 1:
                    continue
                obj_url = image_info['replaceUrl'][0]['ObjUrl']
                thumb_url = image_info['thumbURL']
                url = 'https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=%s&thumburl=%s' % (
                    urllib.parse.quote(obj_url), urllib.parse.quote(thumb_url))
                time.sleep(self.time_sleep)
                suffix = self.get_suffix(obj_url)
                # 指定UA和referrer，减少403
                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-agent',
                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'),
                ]
                urllib.request.install_opener(opener)
                # 保存图片
                filepath = os.path.join(self.__out, './%s/%s' % (word, str(self.__counter) + str(suffix)))
                urllib.request.urlretrieve(url, filepath)
                if os.path.getsize(filepath) < 5:
                    self.__ui.update_log("下载到了空文件，跳过!")
                    os.unlink(filepath)
                    continue
            except urllib.error.HTTPError as urllib_err:
                self.__ui.update_log(urllib_err)
                continue
            except Exception as err:
                time.sleep(1)
                self.__ui.update_log(err)
                self.__ui.update_log("产生未知错误，放弃保存")
                continue
            else:
                self.__ui.update_log("图片+1,已有" + str(self.__counter) + "张图片")
                self.__counter += 1
        return

    # 开始获取
    def get_images(self, word):
        search = urllib.parse.quote(word)
        # pn int 图片数
        pn = self.__start_amount
        while pn < self.__amount:
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=%s&rn=%d&gsm=1e&1594447993172=' % (
                search, search, str(pn), self.__per_page)
            # 设置header防403
            try:
                time.sleep(self.time_sleep)
                req = urllib.request.Request(url=url, headers=self.headers)
                page = urllib.request.urlopen(req)
                self.headers['Cookie'] = self.handle_baidu_cookie(self.headers['Cookie'],
                                                                  page.info().get_all('Set-Cookie'))
                rsp = page.read()
                page.close()
            except UnicodeDecodeError as e:
                self.__ui.update_log(e)
                self.__ui.update_log('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e:
                self.__ui.update_log(e)
                self.__ui.update_log("-----urlErrorurl:", url)
            except socket.timeout as e:
                self.__ui.update_log(e)
                self.__ui.update_log("-----socket timout:", url)
            else:
                # 解析json
                rsp_data = json.loads(rsp, strict=False)
                if 'data' not in rsp_data:
                    self.__ui.update_log("触发了反爬机制，自动重试！")
                else:
                    self.save_image(rsp_data, word)
                    # 读取下一页
                    self.__ui.update_log("下载下一页")
                    pn += self.__per_page
        self.__ui.update_log("下载任务结束")
        out_folder = os.path.join(self.__out, word)
        os.startfile(out_folder)

        return

    def start(self, word, out, ui, total_page=1, start_page=1, per_page=30, ):
        """
        爬虫入口
        :param word: 抓取的关键词
        :param total_page: 需要抓取数据页数 总抓取图片数量为 页数 x per_page
        :param start_page:起始页码
        :param per_page: 每页数量
        :return:
        """
        self.__per_page = per_page
        self.__start_amount = (start_page - 1) * self.__per_page
        self.__amount = total_page * self.__per_page + self.__start_amount
        self.__out = out
        self.__ui = ui
        self.get_images(word)


class ConfigFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(height=200)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # 关键字
        self.wordLabel = customtkinter.CTkLabel(self, text="关键字")
        self.wordLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.wordEntry = customtkinter.CTkEntry(self, placeholder_text="输入关键字，如：头像")
        self.wordEntry.grid(row=0, column=1, columnspan=4, padx=20, pady=20, sticky="ew")

        # 总页数
        self.pageLabel = customtkinter.CTkLabel(self, text="总页数")
        self.pageLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.pageSlider = customtkinter.CTkSlider(self, from_=1, to=100, command=self.page_slider_change)
        self.pageSlider.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        self.pageRLabel = customtkinter.CTkLabel(self, text="", width=25, )
        self.pageRLabel.grid(row=1, column=4, padx=20, pady=20, sticky="ew")

        # 每页数量
        self.sizeLabel = customtkinter.CTkLabel(self, text="总页数")
        self.sizeLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.sizeSlider = customtkinter.CTkSlider(self, from_=1, to=100, command=self.size_slider_change)
        self.sizeSlider.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        self.sizeRLabel = customtkinter.CTkLabel(self, text="", width=25, )
        self.sizeRLabel.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

        self.folderLabel = customtkinter.CTkLabel(self, text="输出目录")
        self.folderLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.folderEntry = customtkinter.CTkEntry(self, state="readonly")
        self.folderEntry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        self.folderButton = customtkinter.CTkButton(self, text="选择", command=self.choose_folder)
        self.folderButton.grid(row=3, column=4, padx=20, pady=20, sticky="ew")
        self.folderEntry.bind('<Button-1>', lambda _: os.startfile(self.folderEntry.get()))

        self.set_default()

    def set_default(self):
        self.wordEntry.insert(0, "二次元")
        self.page_slider_change(1)
        self.size_slider_change(10)
        self.folderEntry.configure(state="normal")
        self.folderEntry.insert(0, pathlib.Path.home())
        self.folderEntry.configure(state="disabled")

    def choose_folder(self):
        output_folder = customtkinter.filedialog.askdirectory()
        if output_folder:
            self.folderEntry.delete(0, len(self.folderEntry.get()))
            self.folderEntry.configure(state="normal")
            self.folderEntry.insert(0, output_folder)
            self.folderEntry.configure(state="disabled")

    def page_slider_change(self, val):
        int_v = int(val)
        self.pageRLabel.configure(text=int_v)
        self.pageSlider.set(int_v)

    def size_slider_change(self, val):
        int_v = math.ceil(val / 10) * 10
        self.sizeRLabel.configure(text=int_v)
        self.sizeSlider.set(int_v)

    def get(self):
        return {
            "word": self.wordEntry.get(),
            "page": self.pageSlider.get(),
            "size": self.sizeSlider.get(),
            "output_folder": self.folderEntry.get()
        }


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("图片下载")
        self.set_position("center")

        self.T = None
        self.is_doing = False

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.checkbox_frame = ConfigFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="下载", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.log = customtkinter.CTkTextbox(self, state="disabled")
        self.log.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.minsize(self.winfo_width(), self.winfo_height())

    def on_closing(self):
        sys.exit()
        self.destroy()


    def doing(self):
        config = self.checkbox_frame.get()
        crawler = Crawler(0.05)
        crawler.start(word=config["word"], total_page=config["page"], per_page=config["size"],
                      out=config["output_folder"], ui=self)

    def button_callback(self):
        if self.is_doing is True:
            tkinter.messagebox.showwarning(title="警告", message="请等待当前任务结束！")
            return
        config = self.checkbox_frame.get()
        if len(config["word"]) < 1:
            tkinter.messagebox.showerror(title="参数错误", message="请输入关键字")
            return
        if len(config["output_folder"]) < 1:
            tkinter.messagebox.showerror(title="参数错误", message="请选择输入目录")
            return

        self.T = threading.Thread(target=self.doing)
        self.update_log("下载期间请不要关闭窗口!!!")
        self.T.start()
        self.is_doing = True

    def update_log(self, msg):
        self.log.configure(state=tkinter.NORMAL)
        self.log.insert(tkinter.END, "\n" + str(msg))
        self.log.configure(state=tkinter.DISABLED)
        self.log.see(tkinter.END)

    def set_position(self, position=""):
        window_width = 600
        window_height = 600

        if position == "center":
            self.geometry(
                "{}x{}+{}+{}".format(window_width, window_height,
                                     int((self.winfo_screenwidth() / 2) - window_width / 2),
                                     int((self.winfo_screenheight() / 2) - window_height / 2)))

        else:
            self.geometry("{}x{}".format(window_width, window_height))

    def close(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

```

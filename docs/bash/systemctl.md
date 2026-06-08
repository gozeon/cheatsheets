

## 常用

### systemctl 管理进程

```bash
# 1. 启动服务（让程序在后台飞一会儿）
sudo systemctl start my-app

# 2. 停止服务（更新服务器文件前必做，防止文件被占用锁死）
sudo systemctl stop my-app

# 3. 重启服务（更新完 publish 文件后，一键让新代码生效）
sudo systemctl restart my-app

# 4. 查看简要状态（看它现在是活的还是死的）
sudo systemctl status my-app

# 5. 让程序开机自动运行（服务器重启了也不怕，会自动拉起）
sudo systemctl enable my-app

# 6. 取消开机自启
sudo systemctl disable my-app

# 7. 刷新系统配置（神级命令：只要你修改了 .service 配置文件，必须执行这个系统才会认新配置）
sudo systemctl daemon-reload
```

### journalctl 管理进程日志

```bash
# 🌟 黄金组合：实时追踪最新日志
sudo journalctl -u my-app.service -n 50 -f

# 1. 只看错误（Error）日志（自动隐藏普通的 Info 提示，排查崩溃神技）
sudo journalctl -u my-app.service -p err

# 2. 按时间清洗日志（查看过去 10 分钟内发生了什么）
sudo journalctl -u my-app.service --since "10 minutes ago"

# 3. 查看自今天凌晨以来的所有日志
sudo journalctl -u my-app.service --since today

# 4. 清除所有历史日志缓存（如果硬盘空间紧缺）
sudo journalctl --vacuum-size=100M  # 限制总日志体积不超过 100M
```

### 配置文件示例

```txt title="/etc/systemd/system/my-app.service"
[Unit]
Description=My .NET Razor Web Application
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/var/www/my-app
ExecStart=/var/www/my-app/YourExecutableName --urls "http://0.0.0"
Restart=always
RestartSec=5
Environment=ASPNETCORE_ENVIRONMENT=Production
Environment=PORT=5000

[Install]
WantedBy=multi-user.target
```

#### [Unit] —— 基本信息与启动顺序  

这个板块主要定义服务的元数据以及它与其他服务的依赖关系。

- Description=：服务的简短描述。当你执行 systemctl status 时，这个名字会显示在最顶端。
- After=network.target：至关重要！ 意思是“在网络驱动和系统网络建立完成之后再启动本程序”。对于 Web 项目、API 服务，必须加这行，否则开机自启时由于网络还没通，程序直接报错闪退。

#### [Service] —— 核心运行逻辑（最重要）  

这里决定了程序怎么跑、以谁的身份跑。  

- Type=simple：最常用的类型。表明 ExecStart 启动的进程就是该服务的主进程。
- User= 和 Group=：安全核心！ 规定程序由哪个 Linux 用户运行。
	- 千万不要写 root。如果代码有漏洞，黑客就能拿到整台服务器的最高控制权。
	- 建议写 www-data（Nginx 默认用户）或创建一个专门的普通用户。
- WorkingDirectory=：文件定位的核心！ 指定程序运行时的“当前目录”。
	- 对于 .NET Razor 项目，必须指向包含 wwwroot 的那个文件夹，否则程序启动后找不到静态资源。
- ExecStart=：启动命令的绝对路径。
	- 注意：Systemd 规定这里的可执行文件路径必须是绝对路径（如 /var/www/my-app/YourApp），不能写相对路径。 后面可以正常跟程序自带的参数。
- Restart=always：高可用核心！ 只要进程退出了（不管是正常退出、异常崩溃、还是被系统 OOM 杀掉），Systemd 都会立刻尝试重新拉起它。
- RestartSec=5：崩溃后等待 5 秒再重启，防止程序代码有致命致命错误时，陷入每毫秒重启一次的“死循环”，把 CPU 飙到 100%。
- Environment=：注入环境变量。比如 .NET 识别的 ASPNETCORE_ENVIRONMENT=Production（生产环境模式）。

#### [Install] —— 开机自启行为  
这里决定了服务在什么情况下会被触发开机自启。  

- WantedBy=multi-user.target：这是 Linux 最标准的“多用户、有网络的非图形界面状态”（即标准的服务器状态）。当你执行 systemctl enable 时，系统会把这个服务挂载到开机启动链条中。

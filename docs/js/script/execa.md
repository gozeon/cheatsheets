
使用 `execa` 模拟bash环境，针对windiw

```js
(async function () {
    const { execa } = require('execa')
    const { execSync } = require('child_process')

    const testCommand = [
        "date",
        "type -p dir",
        "echo $PATH",
        "ffprobe C:/Users/admin/Documents/IPTVBuddy/audio.mp3",
        "rg bash",
        "jq '.name, .version' package.json",
        "locale",
        "npm config list",
        "npm install -g cowsay",
        "python --version",
        "pip install cowsay",
        "python -c \"import cowsay; cowsay.cow('Your message here')\"",
        "soffice.com --version",
        "which cowsay"
    ].join(" && ")

    const paths = [
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\rg\\ripgrep-15.2.0-x86_64-pc-windows-msvc",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\jq",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\node\\global",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\node\\node-v26.13.0-win-x64",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\python",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\python\\Scripts",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\ffmpeg\\ffmpeg-9.0.2-full_build\\bin",
        "C:\\Users\\admin\\Documents\\IPTVBuddy\\tools\\LibreOffice\\program",
    ].join(";")
    const { failed, stderr, stdout, stdio, escapedCommand } = await execa(testCommand, [], {
        shell: 'C:/Users/admin/Documents/IPTVBuddy/tools/PortableGit/bin/sh.exe',
        encoding: 'utf8',
        stdio: ['ignore', 'pipe', 'pipe'],
        extendEnv: false,
        env: {
            HOME: 'C:/Users/admin/Documents/IPTVBuddy/',
            TERM: 'xterm-256color',
            LANG: 'zh_CN.UTF-8',
            LC_ALL: 'zh_CN.UTF-8',
            OUTPUT_CHARSET: 'UTF-8',

            PATH: paths,
            TMP: 'C:/Users/admin/Documents/IPTVBuddy/TEMP',
            TEMP: 'C:/Users/admin/Documents/IPTVBuddy/TEMP',

            NPM_CONFIG_PREFIX: "C:/Users/admin/Documents/IPTVBuddy/tools/node/global",
            NPM_CONFIG_CACHE: "C:/Users/admin/Documents/IPTVBuddy/tools/node/cache",
            NPM_CONFIG_REGISTRY: "https://registry.npmmirror.com",

            // python embed 需要删除python312._pth , 安装 pip 使用 https://bootstrap.pypa.io/get-pip.py
            PYTHONNOUSERSITE: '1',
            PYTHONUNBUFFERED: '1',
            PIP_INDEX_URL: 'https://pypi.tuna.tsinghua.edu.cn/simple/',
            PIP_CACHE_DIR: "C:/Users/admin/Documents/IPTVBuddy/tools/python/pip_cache"
        },
    })
    console.log(stderr)
    console.log(stdout)
    console.log(failed)
    console.log(escapedCommand)
})()
```

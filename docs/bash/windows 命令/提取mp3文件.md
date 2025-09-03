```bat
@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set path=C:\Users\admin\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin;%path%

REM %%~nf → 取文件名（不带扩展名）
REM %%~dpnxf = 文件的 完整路径（drive + path + name + extension）

REM 创建输出目录
if not exist audios mkdir audios

REM 提取所有 mp4 的音频到 audios 目录
for %%f in (*.mp4) do (
    echo 提取音频: %%f
    ffmpeg -i "%%f" -q:a 0 -map a "audios\%%~nf.mp3" -y
)

REM 生成文件列表供 ffmpeg 合并使用
REM 生成文件列表（带引号，防止空格出错）
echo 正在生成文件列表...
(
    for %%f in (audios\*.mp3) do (
        echo file '%%~dpnxf'
    )
) > audios\file_list.txt

REM 合并 mp3 文件
echo 正在合并音频...
ffmpeg -f concat -safe 0 -i audios\file_list.txt -c copy audios\merged.mp3 -y

echo 处理完成！合并后的文件在 audios\merged.mp3
pause

```

# ENLEARN

ENLEARN 本地背诵系统的 TCF Canada Oral B2 题库安装包。

## 当前内容

- `TCF_Oral_B2_CEO_176.csv`：37个主题、176张法中背诵卡
- `INSTALL_B2_TO_ENLEARN.ps1`：自动备份并修改本地 `app.js`，安装B2题库
- `START_ENLEARN_B2.ps1`：在本地端口8091启动ENLEARN网页
- `使用说明.txt`：中文安装与训练说明

## 默认安装位置

```text
C:\Users\evolx\Desktop\DIY Program\ENLEARN背诵软件
```

## 快速安装

下载本仓库后，在仓库文件夹打开PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File ".\INSTALL_B2_TO_ENLEARN.ps1"
powershell -ExecutionPolicy Bypass -File ".\START_ENLEARN_B2.ps1"
```

浏览器打开：

```text
http://127.0.0.1:8091/
```

题库选择：`🔥 TCF Oral B2 CEO (176句)`。

> 如果页面正常但没有声音，请另外启动原ENLEARN的本地TTS服务。历史版本的TTS端口可能是5050或5051，应以当前`app.js`中的`TTS_PROXY_PORT`为准。

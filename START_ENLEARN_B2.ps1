param(
  [string]$Target = "C:\\Users\\evolx\\Desktop\\DIY Program\\ENLEARN背诵软件",
  [int]$WebPort = 8091
)

$ErrorActionPreference = "Stop"
if (-not (Test-Path -LiteralPath (Join-Path $Target "index.html"))) {
  throw "目标文件夹没有 index.html：$Target"
}

$Existing = Get-NetTCPConnection -LocalPort $WebPort -State Listen -ErrorAction SilentlyContinue
if (-not $Existing) {
  $Py = Get-Command py -ErrorAction SilentlyContinue
  if (-not $Py) { $Py = Get-Command python -ErrorAction SilentlyContinue }
  if (-not $Py) { throw "找不到 Python。请先安装 Python，或运行原来的 ENLEARN 启动脚本。" }
  Start-Process -FilePath $Py.Source -ArgumentList @("-m","http.server",$WebPort,"--directory",$Target) -WindowStyle Minimized
  Start-Sleep -Seconds 2
}

Start-Process "http://127.0.0.1:$WebPort/"
Write-Host "ENLEARN 已打开：http://127.0.0.1:$WebPort/" -ForegroundColor Green
Write-Host "若法语不能发音，请再运行原来文件夹中的 TTS 启动脚本。" -ForegroundColor Yellow


param(
  [string]$Target = "C:\\Users\\evolx\\Desktop\\DIY Program\\ENLEARN背诵软件"
)

$ErrorActionPreference = "Stop"
$CsvName = "TCF_Oral_B2_CEO_176.csv"
$SourceCsv = Join-Path $PSScriptRoot $CsvName
$AppJs = Join-Path $Target "app.js"
$TargetCsv = Join-Path $Target $CsvName

if (-not (Test-Path -LiteralPath $Target)) {
  throw "找不到 ENLEARN 文件夹：$Target"
}
if (-not (Test-Path -LiteralPath $AppJs)) {
  throw "找不到 app.js：$AppJs。请确认脚本指向真正包含 app.js 的文件夹。"
}
if (-not (Test-Path -LiteralPath $SourceCsv)) {
  throw "安装包中缺少 $CsvName"
}

$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$Backup = "$AppJs.before_B2_$Stamp"
Copy-Item -LiteralPath $AppJs -Destination $Backup -Force
Copy-Item -LiteralPath $SourceCsv -Destination $TargetCsv -Force

$Text = Get-Content -LiteralPath $AppJs -Raw -Encoding UTF8
$Entry = '    { id: "tcf_oral_b2", name: "🔥 TCF Oral B2 CEO (176句)", file: "TCF_Oral_B2_CEO_176.csv" },'

if ($Text -notmatch 'id:\s*"tcf_oral_b2"') {
  $Pattern = '(const\s+CSV_FILES\s*=\s*\[\s*)'
  if ($Text -notmatch $Pattern) {
    throw "没有在 app.js 中找到 const CSV_FILES = [。已保留备份：$Backup"
  }
  $Text = [regex]::Replace($Text, $Pattern, ('$1' + [Environment]::NewLine + $Entry + [Environment]::NewLine), 1)
  [System.IO.File]::WriteAllText($AppJs, $Text, [System.Text.UTF8Encoding]::new($false))
  Write-Host "已登记新题库到 app.js" -ForegroundColor Green
} else {
  Write-Host "app.js 已经登记过 B2 题库，跳过重复修改。" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "安装完成！" -ForegroundColor Green
Write-Host "题库：$TargetCsv"
Write-Host "app.js 备份：$Backup"
Write-Host ""
Write-Host "下一步：重启 ENLEARN，然后在题库下拉框选择："
Write-Host "🔥 TCF Oral B2 CEO (176句)" -ForegroundColor Cyan
Read-Host "按 Enter 关闭"


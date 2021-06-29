# Genshin_Impact_Wishes_Analyzer
## by HansenH 20210629
原神抽卡数据读取，保存，与分析。  
Genshin Impact Wishes Analyzer.  
Read wishes log from URL and save them to Excel. Analyze wishes' history data with Python.  
</br>
### 需要安装的Python非标准库:  
openpyxl  
pandas  
requests  
</br>
### 使用方法：  
打开原神客户端，查看祈愿历史，断网，点击右上角刷新按钮，复制页面上出现的URL。  
运行export_log.py，粘贴该URL，回车，导出数据到xlsx文件。  
复制想要分析的xlsx文件到目录下提示的文件夹内，运行analyzer.py后生成的txt文件即为分析报告。

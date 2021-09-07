# Genshin_Impact_Wishes_Analyzer

## by HansenH 20210629, EYH 20210828

原神抽卡数据读取, 保存, 与分析.
Genshin Impact Wishes Analyzer.
Read wishes log from URL and save them to csv and mysql db (local or remote). Analyze wishes' history data with Python.

### 为什么写这个程序

很多现有的原神抽卡分析工具只能从URL而非文件分析历史记录, 而官方只可查看过去6个月的历史记录。
通过这个工具可以持久化保存之前的记录, 可以自己将记录拼接 csv 文件(可用 Excel 读取), 或存于 mysql 数据库,分析更长期的记录。

### 需要安装的Python非标准库

```bash
pip install openpyxl
pip install pandas
pip install requests
pip install thrift2pyi
pip install sqlalchemy
```

### How to Find the API call URL

打开原神客户端, 查看祈愿历史, 断网, 点击右上角刷新按钮, 复制页面上出现的 URL。

Start the game, go the the history section in Wishes.
Then disconnect your internet, refresh the page, then you should find the URL.

## Usage

### All-in-one Bootstrap

```bash
python3 bootstrap.py all
```

For more detail, see `.common/idl/const.thrift`.

### Python CLI

```python
> from genshin_wishes import *
> job = CharacterWishes(url)
> job.run()
> job.analyze()
```

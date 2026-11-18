# bulletin trial · 社区公告轮换试验的计划与回访底表

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m bulletin_trial rounds data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`schedule` 以 `site/round` 为键，`assigned` 是原随机分派，`actual` 表示实投，空值是未投。`message` 是公告版本，`messages` 指向实际题目知识点 `topic`。轮次为顺序周。联合接触 `crossings` 指另一站居民参加的活动及公告版本。
`returns` 中 `correct=null` 是未作答，每条代表该站轮次的一份预期回访；`policy` 包含排期预设的洗脱周数 `washout`、可补的轮次数或回访预算。底表保留计划、实际和响应，不作推断。

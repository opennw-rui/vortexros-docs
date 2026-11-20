# Debug 5 文档与验证追踪

用户操作内容位于 operator/qinq-flexible.md 和 operator/link-aggregation.md，新增同一次提交的跨服务/聚合成员迁移、影响、查询和撤销；没有将开发拓扑说明写进用户步骤。

V030R-B02：命令参考原有849条规范路径，历史 cli-coverage.tsv 只有846个当前路径。补齐 display logbuffer、port vlan-stacking vlan、undo port vlan-stacking vlan 三项的证据映射；命令参考标题数量由846修正为849。没有新增命令或重复运行原全量验收。check-commands.py 已确认849个规范路径及语法/视图匹配。原台账含旧名称的历史行继续保留，不把历史行数当当前命令数。

日志复用 Debug2/logbuffer/live-terminal.txt，QinQ 复用 Debug2/flexible-qinq 原始配置、流量和撤销记录，同时补入 Debug5 的迁移真实 CLI/流量证据。原记录存放于开发服务器 /root/vros-open-items-20261119/，当前包对应的升级和设备验证另见产品仓库 Debug5 记录。

补充L2子接口固定外层多内层迁移案例见 operator/subinterfaces-l2.md；最终run42在QEMU和真机的安装、CLI及配置/后端保留证据，见产品仓库 docs/validation/v0.30-dev-debug5-review.md。没有再次执行全量CLI或实际反向回退事务。

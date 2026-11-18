# 邻居组与认证


具有相同属性的邻居可以加入同一个邻居组。内部组继承本地AS；外部组必须先指定对端AS，再加入成员：

```text
bgp 64512
 group IBGP-RR internal
 peer IBGP-RR password simple Lab-Password-01
 peer IBGP-RR connect-interface LoopBack 0
 peer 10.0.0.2 group IBGP-RR
 peer 10.0.0.3 group IBGP-RR
 group TRANSIT external
 peer TRANSIT as-number 64513
 peer TRANSIT password simple Transit-Password-01
 peer 192.0.2.2 group TRANSIT
 ipv4-family unicast
  peer IBGP-RR reflect-client
  peer TRANSIT route-policy RP-IN import
```

命令关键字不区分大小写，邻居组名称按输入原样保存并区分大小写；`TRANSIT`与`transit`是两个不同对象。成员继承组的AS、认证、源接口及地址族策略。邻居可以用`peer ADDRESS password simple PASSWORD`设置自己的认证密码，以覆盖组密码。已经加入邻居组的成员不能再单独配置AS；需要改变归属时，应先执行`undo peer ADDRESS`，再重新创建。

BFD按字段继承。组上启用BFD并配置计时器后，成员默认继承；成员只配置一个计时字段时，仅该字段覆盖组值，其余字段继续继承。`peer ADDRESS bfd disable`用于明确关闭该成员从组继承的BFD，`undo peer ADDRESS bfd disable`恢复继承；`undo peer ADDRESS bfd enable`同样删除成员级开关。存在显式关闭的成员时，系统会把组的有效BFD配置逐一投影到其余成员，避免后端重新继承组BFD而使关闭失效。运行态、BFD会话归属和FRR profile使用同一套有效值。

密码认证使用BGP TCP MD5。当前只提供`simple`形式，密码以明文进入配置并按明文下发到FRR，`display current-configuration`也会显示原值；应限制配置文件、命令输出和运维会话的访问权限。密码长度为1至80个不含空格的可打印字符，不支持`cipher`输入形式。

邻居组不能在仍有成员引用时删除。可按以下顺序撤销：

```text
bgp 64512
 undo peer 192.0.2.2
 undo peer TRANSIT password
 undo group TRANSIT
```

CLI 操作：

```text
commit
```

`display bgp group`用于查看后端邻居组状态；`display current-configuration configuration bgp`用于核对设备配置。密码只应通过配置查看，不会作为普通BGP会话状态字段输出。


[会话与路由查询、精确撤销](queries.md) · [完整双端案例](../../examples/bgp.md) · [策略实际结果](../../examples/bgp-policy.md)

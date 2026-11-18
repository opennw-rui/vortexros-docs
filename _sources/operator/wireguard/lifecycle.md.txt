# 修改与删除

## 修改和删除

- 新增或删除peer只影响该peer；
- 修改密钥、目的地址或监听参数时，相关Tunnel可能短暂重新建立；
- profile仍被Tunnel引用时不能删除；
- 修改peer underlay、source或destination后，应重新检查对应VPN中到公网地址的路由。

```text
undo interface Tunnel 10
undo wireguard profile WG-PROFILE
```

CLI 操作：

```text
commit
```


[功能目录](../wireguard.md) · [命令参数](../reference/wireguard.md)


完整撤销的实测对照：删除 peer 后接口仍存在但对端探测不再成功；直接删除仍被接口引用的 profile 会被拒绝。解除引用、删除隧道和 profile 并提交后，接口与 peer 均不再出现在查询结果中，服务健康保持 ready。若已经保存过配置，撤销后需要再次 save，避免下次启动恢复示例对象。


如果只是更换 profile，可在同一个 Candidate 中解除旧绑定并绑定完整的新 profile，再提交。单独撤销绑定、私钥或其他必填字段后，Tunnel 不完整，commit 会拒绝；删除 profile 时仍保留这样的 Tunnel 也不能完成提交。完整停用应删除不再使用的 Tunnel。

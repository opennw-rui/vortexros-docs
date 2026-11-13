# 首次启动与验收

## 启动前检查

```bash
sudo vortexros-bootstrap check --verbose
```

必须消除所有 `FAIL`。对每个 `WARN` 记录接受理由或完成修复。

## 显式启动

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now vortexros.target
```

这是首次部署中唯一启用控制面目标的步骤。执行后systemd启动`vortexrosd`和`vortexros-route-zapi`；VPP、FRR保持独立生命周期，后端是否ready仍以CLI回读为准。

## CLI 验收

```text
sudo vortexros
<VortexROS> system-view
[~VortexROS] display service verbose
[~VortexROS] display health verbose
[~VortexROS] display alarm active
[~VortexROS] display vpp api compatibility verbose
[~VortexROS] display vpp interface-ownership verbose
```

检查 configured、running、ready、converged 不应混为一个状态。可选功能未配置且 API 缺失可以显示 unavailable；已配置功能依赖缺失必须是错误。

## 配置与重启恢复

```text
[~VortexROS] commit
[~VortexROS] save
```

随后由维护窗口执行设备重启，并重复上述 display。未 `save` 的 Running 在 daemon 重启后丢失是既定语义。

## 不要做的事

- 不要把后端进程“正在运行”当成配置已收敛；
- 不要绕过 CLI 直接修改 VPP、FRR pathspace 或受管 LCP/VRF 接口；
- 不要在接管事务处于 transition 时重复绑定驱动；
- 不要删除接口恢复台账来掩盖 critical 告警。

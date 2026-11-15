# 数据面激活与恢复

修改设备模式、CPU、队列、描述符或大页等参数后，先提交、保存，再按提示激活：

~~~text
commit
save
reset dataplane
~~~

`reset dataplane`需要交互确认，可能中断由数据面承载的业务。影响管理链路时，应使用可恢复的管理连接。

## 激活后检查

~~~text
display dataplane
display dataplane interfaces
display interface brief
display ip interface brief
display health
~~~

核对设备的期望模式与活动模式、接口名称、IP和路由，再从实际业务源地址执行ping。需要CPU或驱动初始化才能生效的参数，不能只根据配置显示判断已经应用。

## 恢复默认参数

在对应视图撤销显式的worker、队列或描述符设置，提交、保存后再次激活。撤销后采用设备或驱动默认值；不同网卡的默认队列及描述符数可能不同，不应统一认定为256或1024。

切回kernel模式时保留接口的产品名称，已提交的地址和路由按新的接口归属恢复。若激活失败，先查看数据面阶段和告警，再按[管理连接恢复](../../troubleshooting/dpdk-management.md)处理。

[设备配置](devices.md) · [资源查询](resources.md)

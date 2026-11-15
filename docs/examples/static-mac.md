# 静态 MAC

## 拓扑和作用

本例把远端MAC固定到指定桥域出口，并关闭学习和未知单播泛洪，以便用流量区分“表项实际转发”和“只是泛洪可达”。实验复用开发服务器的隔离PE3与Linux端点，不涉及真机：

~~~text
PE3 Vbdif777 192.0.2.1/24
  BD777 / VLAN777
  host-p3docce ───── remote0 192.0.2.3/24
                       MAC 92:28:40:07:45:9d
~~~

静态MAC只决定二层目的MAC的出口，不创建IP路由或ARP。实际设备必须替换端口名和对端真实MAC；不能把示例MAC用于其他主机。

## Linux端点

~~~sh
ip link set remote0 up
ip address add 192.0.2.3/24 dev remote0
~~~

实验端口已在独立网络命名空间中连通，若地址已存在不重复添加。VPP基础口和LCP应已建立；PE3开启switch。

## PE3完整配置

~~~text
system-view
enable switch
vlan 777
quit
bridge-domain 777 no-learn no-uu-flood
 l2 binding vlan 777
quit
interface host-p3docce
 portswitch
 port link-type access
 port default vlan 777
quit
interface Vbdif 777
 ip address 192.0.2.1 255.255.255.0
quit
mac-address static 9228-4007-459d host-p3docce bridge-domain 777
commit
display bridge-domain 777
display mac-address bridge-domain 777
ping -a 192.0.2.1 -c 3 192.0.2.3
~~~

业务桥域777由模型映射为内部VPP桥域，不应手动依赖内部编号。出口必须属于本业务，跨VLAN端口会在配置校验时拒绝。关闭学习和未知单播泛洪会影响该域所有未知目的流量；本例是独占实验域，不应直接用在承载其他客户的桥域。

## 真实结果

~~~text
bridge-domain 777
  flood: on  uu-flood: off  forward: on  learn: off
  bvi: Vbdif777
  ports:
    Vbdif777         shg 0
    host-p3docce     shg 0

MAC Address       VLAN/VSI/BD                    Learned-From        Type
02fe-ade9-8be5    -/-/777                        host-p3docce        static
9228-4007-459d    -/-/777                        host-p3docce        static
Total items displayed = 2

3 packets transmitted, 3 received, 0% packet loss
~~~

运行时自动产生的本地项不应冒充用户静态配置。上面第二条为本例目标MAC。

## 撤销对照

~~~text
undo mac-address static 9228-4007-459d host-p3docce bridge-domain 777
commit
display mac-address bridge-domain 777
ping -a 192.0.2.1 -c 3 192.0.2.3
~~~

真实查询只剩本地项，目标MAC不再存在；探测3发0收。由于学习和未知单播泛洪仍关闭，这次失败证明原可达性依赖该静态出口，不能将删除后的失败当作产品故障。

最后撤销本例独占对象：

~~~text
undo interface Vbdif 777
interface host-p3docce
 undo portswitch
quit
undo bridge-domain 777
undo vlan 777
commit
display bridge-domain 777
display health
save
~~~

真实撤销后display bridge-domain 777显示(no bridge-domain)，健康ready、Running/Actual=6/6、零告警；save应答Y并保存成功。已有其他业务时，只撤本例新增项，保留共享接口和交换全局设置。

[MAC功能](../operator/mac-table.md) · [桥域参数](../operator/reference/bridge-domains.md)

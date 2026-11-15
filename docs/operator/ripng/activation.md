# 进程与发布

## 配置


```text
ripng 2 vpn-instance BLUE
 network 2001:db8:100::/64
 import-route static
 default-route originate
```

RIPng视图中的`import-route ospf`表示导入OSPFv3路由，系统会映射到后端的IPv6协议名称。


[完整双端案例与实测](../../examples/ripng.md) · [参数参考](../reference/ripng.md)

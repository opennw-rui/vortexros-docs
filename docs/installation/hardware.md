# 支持的硬件

本页对应 **VortexROS 0.28 开发版 Debug 9**、配套 **VPP 26.10.4** 和 **DPDK 26.07**。选型时先看本版安装范围，再按 PCI ID、驱动和实际用途确认网卡。内核驱动、PCI 绑定驱动和 DPDK PMD 是三项独立信息。

## VortexROS 验证记录

| 平台或设备 | 路径 | 验证范围 |
| --- | --- | --- |
| Intel Celeron N5105（x86‑64），Intel I225‑V rev 03（`8086:15f3`） | Linux 模块 `igc`。DPDK 接管时，Linux 显示 `vfio-pci`，VPP 使用 IGC PMD | Ubuntu amd64 真机运行 Debug 5 和 VPP 26.10.3。库存确认四个 I225‑V，VPP 识别四口，核对时两口有链路。该条为 Debug 5 的历史硬件验证，Debug 9 没有重新执行性能验收。当前[发布验证](../release/vortexros.md)另列。 |
| Intel I226 系列 | Linux `igc` 与 DPDK IGC PMD，按 PCI ID 确认具体型号 | 上游支持。DPDK 26.07 还列有 I226‑LM 的平台验证。目前无 VortexROS I226 真机验收记录。 |
| QEMU/KVM amd64 | Linux 数据面首装，VPP 隔离案例使用 AF_PACKET／veth 或 memif | 隔离环境已验证首装和相关协议及转发案例。memif 和 veth 属于虚拟测试路径。 |
| Proxmox VE（PVE）VirtIO 网卡 | 虚拟机网卡模型选 **VirtIO (paravirtualized)**，虚拟机中的 Linux 驱动为 `virtio_net`。虚拟机若使用 DPDK，对应独立的 Virtio PMD | 上游有驱动。PVE 宿主桥接、虚拟机中的 Linux 转发和虚拟机中的 DPDK 是不同路径。目前无 PVE 专项验收记录。 |

[N5105 产品规格](https://www.intel.com/content/www/us/en/products/sku/212328/intel-celeron-processor-n5105-4m-cache-up-to-2-90-ghz/specifications.html) · [DPDK 26.07 IGC](https://doc.dpdk.org/guides-26.07/nics/igc.html) · [DPDK 26.07 平台验证](https://doc.dpdk.org/guides-26.07/rel_notes/release_26_07.html) · [Proxmox VE 虚拟机手册](https://pve.proxmox.com/pve-docs/qm.1.html) · [DPDK 26.07 Virtio](https://doc.dpdk.org/guides-26.07/nics/virtio.html)

## 在 Proxmox VE 中选择 VirtIO

在虚拟机的 **硬件 → 网络设备** 中选择 VirtIO，并将设备接到所需的 PVE bridge。按 Linux 模式首装后，在虚拟机内运行 `ethtool -i`，确认驱动为 `virtio_net`，再通过 `display interface brief` 核对接口。虚拟机中的 DPDK 仍须独立验证 PCI 设备识别、IOMMU／VFIO 条件及管理路径。

## FD.io VPP 支持范围

FD.io VPP 列出 x86‑64 和 Arm AArch64 两种架构，软件包支持近期 Debian 和 Ubuntu 版本。DPDK 的 x86 平台包括 Intel 和 AMD，另有 Arm 平台。VortexROS 本版单文件安装器面向 **Ubuntu 26.04 amd64**。VPP 的架构支持范围可用于评估底层能力，产品安装包和各功能的验收范围以[支持矩阵](support.md)为准。

VPP 的硬件驱动由 FD.io CSIT 性能用例覆盖。走 VPP 原生驱动时查 VPP 功能清单；走 DPDK 时查配套版本的 PMD 指南和设备 PCI ID。下表是常见选型入口，完整厂商列表见 DPDK 驱动目录。

| 网卡家族 | 常见驱动或数据路径 |
| --- | --- |
| Intel I210／I350 | DPDK IGB |
| Intel I225／I226 | DPDK IGC，26.07 构建库为 `librte_net_e1000` |
| Intel X520／X540／X550 | DPDK IXGBE |
| Intel X710／XXV710／XL710 | DPDK I40E，VF 另查对应驱动 |
| Intel E810 | DPDK ICE，或在满足条件时使用 AVF/VF 路径 |
| NVIDIA ConnectX‑5／6／7 | DPDK MLX5，具体型号、固件和依赖见驱动指南 |
| Broadcom NetXtreme‑E、AWS ENA | 分别查 DPDK BNXT、ENA |
| QEMU/KVM／Proxmox VE VirtIO、VMware VMXNET3 | 分别查 DPDK Virtio、VMXNET3 |

[FD.io VPP 26.10 支持策略](https://s3-docs.fd.io/vpp/26.10/aboutvpp/supported.html) · [VPP 原生驱动和功能](https://s3-docs.fd.io/vpp/26.10/aboutvpp/featurelist.html) · [DPDK CPU 平台](https://core.dpdk.org/supported/cpus/) · [DPDK 26.07 网卡驱动](https://doc.dpdk.org/guides-26.07/nics/index.html) · [DPDK 网卡及设备清单](https://core.dpdk.org/supported/nics/)

## 公开性能数据

FD.io CSIT 的数值对应 CPU、网卡、驱动、帧长、核心数和功能的组合。下列条目可在 CSIT 26.10 报告中打开对应图表，读取 NDR、PDR、MRR 或延迟。NDR 是无丢包速率，PDR 使用测试设定的允许丢包率，MRR 是最大接收速率类测试。

| 测试平台 | 网卡与驱动 | 26.10 已公开的用例 |
| --- | --- | --- |
| Xeon 6767P / Granite Rapids（[2n-gnr][gnr-ipv4]） | Intel E810，AVF | IPv4／IPv6 随机 2 万前缀、Geneve |
| Xeon Platinum 8580 / Emerald Rapids（[2n-emr][emr-ipv4]） | Intel E810，AVF | IPv4／IPv6 随机 2 万前缀、NAT44；单 worker IPv4 2 万条的 PDR 从 28.09 到 27.80 Mpps（26.06 → 26.10，64 字节帧） |
| Xeon 6780E / Sierra Forest（[3n-srf][srf-wireguard]） | Intel E810，DPDK 或 AVF | IPsec、VXLAN、WireGuard 软件与硬件加密 |
| Xeon Platinum 8462Y+ / Sapphire Rapids（[2n-spr][spr-nat44]） | NVIDIA ConnectX‑7，MLX5 | NAT44 TCP 吞吐 |
| NVIDIA Grace（[2n-grc][grc-ipv4]） | NVIDIA ConnectX‑7，MLX5 | IPv4／IPv6 随机 2 万前缀、NAT44 连接速率、Geneve |
| AWS C6in（[2n-c6in][c6in-ipv4]） | ENA，DPDK | IPv4／IPv6 随机 2 万前缀 |
| AMD EPYC 7532（`2n-zn2`） | 平台含 Intel X710／XXV710 和 ConnectX‑5 | 在 26.10 的 Search Tests 中以 `2n-zn2` 搜索，按网卡和测试名称确认结果 |

N5105／I225 的记录用于说明 VortexROS 的硬件功能验证范围。本手册目前没有该组合、I226 或 PVE VirtIO 的受控吞吐基准。现有产品隔离测试和上游对比见[性能测试](../release/performance.md)。

[CSIT 26.10 用例和数据入口](https://csit.fd.io/cdocs/release_notes/current/#csit-2610-selected-performance-tests) · [CSIT 测试台规格](https://csit.fd.io/cdocs/infrastructure/fdio_dc_testbed_specifications/)

## 核对自己的设备

在 Ubuntu 终端查看 CPU、网卡 PCI ID 和当前驱动。若为 PVE VirtIO，以下命令在虚拟机内执行，并用实际接口名替换 `ens18`。

~~~bash
lscpu
lspci -nnk
ethtool -i ens18
~~~

在 VortexROS CLI 用 `display dataplane interfaces` 核对期望模式和活动模式，再用 `display interface hardware offload` 查看具体网口的硬件能力。DPDK 接管前按[数据面配置](../operator/dataplane.md)核对 PCI、IOMMU、大页和管理连接。接管后按[硬件验收](08-hardware-acceptance.md)检查实际链路、业务和恢复。

[gnr-ipv4]: https://csit.fd.io/report/#eNrtmMtugzAQRb-GbqpBtgOkmy6a8h-VC5MEFYw7diOlX18TVRpQH4vQqCLygpevR_M48l3gfE_45LC9T_JNst4kat3U4ZasHm7Dg1qnCingYC2oIg1vhC1qh7AjbRqPpG1TO1AGdoZACrFDZSXeSVG9gj5sobEZFNkzyArQ74evcLlKt6jEC5CpoSMaEqrHz4RfsrNav3lWQ00T5YDE4i_FcpDdH0cRP7XA-zWh5oDQB0se3ai07zvl3VvSHbrmHTkkzIj1KkBhSVbTPP5oR-pkfPuey8gHmFKkK5HmMi1GxfJiMSzmZbIuT9K_8Dd15D-D_2R8S-RvI_85_O0y-Kvo_-fyV9fg_yr6_2X4m6Wf_-j_s_gvxP-z6P_n8s-uwf-z6P-X4W-Wfv6j_8_i_1f-n5c3pqfu9B8oLz8A0RXamA
[emr-ipv4]: https://csit.fd.io/report/#eNrtlUtPhDAQgH9NvZghbZeCFw-u_A9T21khFqhTJFl_vWVjMhAfh030YPbAa75O5vEdSNNI-JAw3AqzF_Ve6Lrz-SZ2d9f5QSHpSkmYYwRdFfmNMKBNCNgj2eDJxs4n0EMOECgpn1BHhTdKuhew8wG6WEJVPoJygFO7fOUrORtQy2egwUP0tBTU9x8FP1Vn6l8nprmnDZmRGP7QLCfF9rjK-G4EPm8JLSfkORhNmFatfT0pnz6Q7TF1b8gpeUfMXZbCSLltnekYV3SzvnbkNswiU8liJwujinK1Rg7qJWgaUTcn9Iv-9cX_uf71f_BfXvyf67_8E_-muRpG6k__AdO8Ay4zosM
[srf-wireguard]: https://csit.fd.io/report/#eNrtl11rgzAUhn-NuxmRJJraXexinf-jWHOsYX5kJ7Fd9-sXXSHKKAw2Bw5vjOQ9L-fDBw4a2yLsDVSPgdgFyS7giZLuEURP9-7AyvANo-SkNeGb0L0hVJAZIEYBYlY4t7EkaojBgjBKj8A1gy2j-SuRWr4QpeO97ZoGKkOYYNsDYTkBW7r7TuqzQjh2GUpnpbapzLk3HPoEWmJfB3--1vGlKK_KznrVlTpRToBevN2D9-jy4g23O_OGDCHzjlHDPsReM3yGfKN9by0wq8God_D-YY4-IncNjMR8mtZe9EidTLVsfVWi__SMhhENBQvjh_5epEGSDrF_AgZfwZgTDL5YMOIVjDnBiBcIhqrV27pJfsxFP8b_tEgGLNY9MicWfKlYrFtkTix-fYmI9K5psR7-S0T6Af-xmVE
[spr-nat44]: https://csit.fd.io/report/#eNrtVU1PhDAQ_TV4MUNoaQsXDyL_w1SYFRIWxrZLsv56CzEZiNF4wYPZSz_mzUzfa19SHyaHzx6Hh0RXSVElsujbOCT5432c3OClERnMRCBNGlcOB7QewVuirnfoLPWtBzmCJwciy15RksBSZM0b2PkEPakl_AKiAQxd3IaGYLRBKWyhM1rnBsjk4JWQZWFKCHQJQK1baMinTxpfODHaXgKjkekOmdEx-JMErqLuuin5ThjnW4eWC6JAhgL6Dbffy-cOJ2fP6Pt35DbLbXJCEx9wgzX7w8OVNujuUruJuelq7ZvmWapFqg1ncbBcgrpOinqFDvWKvHnleK_I_-EVdfPK8V5Rf-IVXd-Nkzuvf5GuPwB-b8Xl
[grc-ipv4]: https://csit.fd.io/report/#eNrtlMtOwzAQRb_GbNBE9iROViwo-Y_KOEMTkYdlm6jt1-NUSJMIuqlggdSFn3dGc8dHcoiTp32g_knonah2AquuSZPInx_T4vuApZIwOwdYZmnnqScTCEaaZvJpMyPgCAdvAaU8EDplj9VMJsLQHzV0roCyeAVlgWK7nNII1vSE8h382IBr_FIQX74KfqvOavMRWU2eNkqyw-JVs5zi2tMq_noLnGE8GU5JfbAUKays_dwpR795M1DozsQp6Y1YtwkKS8pu68STW6mb52sntqEXmEpmucy0yvJyude1qOpL7B-ixjvqW1HjP0Nd3FHfirr4bdS6fhgnP1w-cl1_Aq4gl0c
[c6in-ipv4]: https://csit.fd.io/report/#eNrtlU1vgzAMhn8Nu0yJYpMPethhHf9jYuCtqJSiwCp1v34OmhQC2w6TduuBr-dN7NeOLMbp7Ol5pO4hM_vM7TN0bcO3LH-854fvRrSgxGUYBFrJb546qkYSbU1ddSQxkr-QF9iL2ra9QKXeCAagvhLN0BxFO2hh9YuAWtB0CF98jXXVEaqj8H0jhsaHhPj0lXCTParN-xRV9pQobCOKv5mNu4bDdbHlhxLi8spTFddzHVGaaFxY-77SuPrVVyca2w-KW7hHUa_5UKIEdZpnug4LNWnf4RxtmHCYUEjYcS8KJXFhd8aOW6Qk2C1HxVqBG57njHcrXEgD0roV3UlgjIBbbkEC7jYcc8seIXJOhuzPsBfM1zgcsHYpBanVNgRItsjBU4oSQwi3WqzZspaFXlLHJvLQEJNQw9SmleTMTIjKHdQrzIWnZ_BFi1DIAnPXQKEs2CDMCU2ZuXIW_3E88Taefx1PvI3nbTxNedef_Wn-i5ryEwOzusc

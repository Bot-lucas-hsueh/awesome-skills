# Standards & Reference

## 7.1 Official Documentation

- [阿里云产品文档](https://help.aliyun.com/zh/ecs)
- [API OpenAPI](https://next.api.aliyun.com/)
- [阿里云架构中心](https://architecture.aliyun.com/)
- [成本优化指南](https://help.aliyun.com/zh/ecs/user-guide/cost-optimization)

## 7.2 Core Services Reference

### 7.2.1 ECS实例规格

| 系列 | 适用场景 | CPU/内存 | 特点 |
|------|---------|---------|------|
| 突发性能t系列 | 轻量负载 | 1-2核/1-2G | 性价比高，有积分机制 |
| 通用g系列 | 中等负载 | 2-8核/4-32G | 平衡计算和内存 |
| 计算型c系列 | 高计算 | 2-8核/4-16G | 高CPU性能 |
| 内存型r系列 | 内存密集 | 2-8核/16-64G | 大内存需求 |

### 7.2.2 常用区域

| 区域 | 地域ID | 说明 |
|------|--------|------|
| 华北2(北京) | cn-beijing | 北方首选 |
| 华东1(杭州) | cn-hangzhou | 电商/互联网 |
| 华东2(上海) | cn-shanghai | 金融/游戏 |
| 华南1(深圳) | cn-shenzhen | 华南首选 |

### 7.2.3 VPC网络规划

```
VPC CIDR: 192.168.0.0/16
子网:
  - 交换机1(可用区A): 192.168.1.0/24 (ECS/SLB)
  - 交换机2(可用区B): 192.168.2.0/24 (RDS)
  - 交换机3(私网): 192.168.3.0/24 (内网服务)
```

## 7.3 成本优化标准

### 7.3.1 计费方式对比

| 方式 | 适用场景 | 折扣 |
|------|---------|------|
| 按量付费 | 测试/临时/波动负载 | 1.0x |
| 包年包月 | 稳定长期使用 | 0.3-0.5x |
| 预留实例券 | 稳定长期，容量确定 | 0.2-0.4x |
| 抢占式实例 | 无状态/容错任务 | 0.1-0.2x |

## 7.4 SDK Compatibility

| SDK | 状态 | 备注 |
|-----|------|------|
| Alibaba Cloud SDK for Python | 推荐 | ECS/RDS/OSS全覆盖 |
| Terraform Provider | 推荐 | 基础设施即代码 |
| ROS | 推荐 | 资源编排服务 |

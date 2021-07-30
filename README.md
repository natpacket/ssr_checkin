# 简介

适用于特定ssr网站签到领流量,开启你的流量白嫖之旅吧   
在开始之前你需要确定你有这个[网站](https://wangzi.uk/)的账号

# 目录

- [简介](#简介)
- [目录](#目录)
- [功能](#功能)
- [使用方式](#使用方式)
  - [使用腾讯云函数(免费)](#使用腾讯云函数免费)
    - [1.Fork本项目](#1.Fork本项目)
    - [2.获取相关参数](#2.获取相关参数)
    - [3.填写secret](#3.填写secret)
    - [4.部署](#4.部署)
  - [使用Actions(不建议使用)](#使用Actions不建议使用)
    - [解释及声明](#解释及声明)
    - [Actions运行方式](#Actions运行方式)
      - [1.填写secret](#1.填写secret)
      - [2.运行任务](#2.运行任务)
- [同步上游代码](#同步上游代码)
- [申明](#申明)

# 功能

- [x] 每天自动签到领流量

# 使用方式

## 使用腾讯云函数(免费)

### 1.Fork本项目

项目地址:[natpacket/ssr_checkin](https://github.com/natpacket/ssr_checkin)

### 2.获取相关参数

- 为了确保权限足够, 获取以下这两个参数时不要使用子账户! 而且, 腾讯云账户需要 [实名认证](https://console.cloud.tencent.com/developer/auth) !
- 开通云函数 `SCF` 的腾讯云账号，在 [访问秘钥页面](https://console.cloud.tencent.com/cam/capi) 获取账号的 `SecretID`，`SecretKey`
- 依次登录 [SCF 云函数控制台](https://console.cloud.tencent.com/scf) 和 [SLS 控制台](https://console.cloud.tencent.com/sls) 开通相关服务，确保您已开通服务并创建相应 [服务角色](https://console.cloud.tencent.com/cam/role) **SCF_QcsRole、SLS_QcsRole**

### 3.填写secret

`Name`和`Value`格式如下：
  
| Name | Value |
|:---:|:---:|
|TENCENT_SECRET_ID | 腾讯云用户 SecretID|
|TENCENT_SECRET_KEY | 腾讯云账户 SecretKey|
|USER_JSON | config.json 中内容|

### 4.部署

- 首次 `Fork` 需要去 `Actions` 里面同意使用 `Actions` 条款.
- 添加完上面 `3` 个 `Secrets` 后, 进入 `Actions` --> `Serverless`, 点击右边的 `Run workflow` 即可部署至腾讯云函数

## 使用Actions(不建议使用)

### 解释及声明

使用 GitHub Actions 执行此类任务属于 **滥用谷歌资源** , 因此 **不建议** 这种使用方法!

### Actions运行方式

#### 1.填写secret

`Name`和`Value`格式如下：

| Name | Value |
|:---:|:---:|
|USER | 该网站账号|
|PASSWD | 密码|

**当有多个账号时，账号与账号、密码与密码之间应该空格**

#### 2.运行任务

- 点击star,即可运行任务
- 进入 `Actions` --> `wangzi.uk网站签到 `, 点击右边的 `Run workflow` 即可运行签到
- 进入`ssr_checkin/.github/workflows/run.yml`自行配置定时任务

# 同步上游代码

### 安装pull应用

安装 [pull](https://github.com/apps/pull) 应用, 实现自动同步上游代码.

# 申明

1. 此脚本仅用于学习研究, 不保证其合法性, 准确性, 有效性, 请根据情况自行判断, 本人对此不承担任何保证责任.
2. 您必须在下载后 **24** 小时内将所有内容从您的计算机或手机或任何存储设备中完全删除, 若违反规定引起任何事件本人对此均不负责.
3. 请勿将此脚本用于任何商业或非法目的, 若违反规定请自行对此负责.
4. 此脚本涉及应用与本人无关, 本人对因此引起的任何隐私泄漏或其他后果不承担任何责任.
5. 本人对任何脚本引发的问题概不负责, 包括但不限于由脚本错误引起的任何损失和损害.
6. 如果任何单位或个人认为此脚本可能涉嫌侵犯其权利, 应及时通知并提供身份证明，所有权证明, 我将在收到认证文件确认后删除此脚本.
7. 所有直接或间接使用, 查看此脚本的人均应该仔细阅读此声明.
8. 本人保留随时更改或补充此声明的权利, 一旦您使用或复制了此脚本, 即视为您已接受此免责声明.

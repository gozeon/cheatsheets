.NET 工程配置详解：环境变量与 User Secrets

在 .NET 开发中，配置系统采用统一的 `IConfiguration` 抽象，支持多种配置源。理解配置的加载机制和优先级是保障项目开发安全与部署灵活性的关键。

---

## 1. 配置加载机制与优先级

.NET 遵循“后加载覆盖先加载”的原则，默认（Minimal Hosting）加载顺序大致如下（后者优先级高于前者）：

1. `appsettings.json`
2. `appsettings.{Environment}.json`
3. User Secrets（通常仅在 Development 环境加载）
4. 环境变量
5. 命令行参数

环境切换：通过设置 ASPNETCORE_ENVIRONMENT (Web) 或 DOTNET_ENVIRONMENT (通用 Host) 来决定加载哪个环境的配置文件。

---

## 2. 环境变量 (Environment Variables)

### 使用场景
适用于生产环境、容器化部署（Docker / Kubernetes）、CI/CD 流水线以及服务器基础配置。

### 使用方法与注意事项
* 嵌套结构映射：环境变量不支持 JSON 的原生层级，需使用双下划线 `__` 表示层级。例如：`TmdbSettings:ApiKey` 对应环境变量 `TmdbSettings__ApiKey`。
* 切换环境示例 (PowerShell):
  `$env:ASPNETCORE_ENVIRONMENT = "Production"`
  `dotnet run`
* 优点与特点：跨平台，完美契合 DevOps 流程，能够有效实现应用与运行环境的解耦。

---

## 3. User Secrets (本地用户机密)

### 使用场景
仅限本地开发环境。用于存储绝对不能提交到 Git 仓库的敏感信息（如 API Key、第三方服务密码、数据库连接串）。

### 初始化与使用命令
1. 初始化（在项目目录下执行）：`dotnet user-secrets init`，这会在 `.csproj` 文件中写入一个 `UserSecretsId`。
2. 设置机密：`dotnet user-secrets set "TmdbSettings:ApiKey" "your-secret-key"`
3. 查看已设置的机密：`dotnet user-secrets list`

### 存储路径
密钥物理文件存储在用户的全局配置目录下，与项目代码彻底隔离：
* Windows: `%APPDATA%\Microsoft\UserSecrets\<UserSecretsId>\secrets.json`
* Linux/macOS: `~/.microsoft/usersecrets/<UserSecretsId>/secrets.json`

---

## 4. 环境变量 vs User Secrets 对比

| 特性 | User Secrets | 环境变量 |
| :--- | :--- | :--- |
| 主要用途 | 本地开发防止敏感信息泄露 | 生产环境、CI/CD 部署注入配置 |
| 存储位置 | 用户目录下的 secrets.json | 操作系统 / 容器进程环境变量 |
| 生效环境 | 默认仅限 Development 环境 | 任何环境均可生效 |
| Git 安全性 | 安全（物理路径在项目外） | 安全（通过外部环境注入） |
| 配置覆盖级 | 低于环境变量与命令行 | 高于配置文件和 User Secrets |

---

## 5. 最佳实践与避坑指南

* 绝对防泄露：切勿将包含真实密钥的 `secrets.json` 或生产环境的 `appsettings.Production.json` 提交到 Git。
* EF Core 迁移注意：执行 `dotnet ef database update` 时，工具会启动 Host 并读取当前的 `ASPNETCORE_ENVIRONMENT`。请务必确认当前环境，避免误将开发环境的配置用于操作生产数据库。
* 生产隔离：生产环境中严禁依赖 User Secrets。应使用云平台的密钥管理服务或通过容器环境变量注入。

## 参考

https://learn.microsoft.com/en-us/dotnet/core/extensions/configuration  

# 💀 worst-practices-demo
此為「故意不安全」的示範型儲存庫，用來觸發 GitHub Advanced Security（含 secret scanning、code scanning、dependency scanning、IaC scanning）之各項掃描。請勿部署至正式環境。

## 目的 (Purpose)
本專案刻意放入多種常見弱點與錯誤實務（anti-patterns），方便 GitHub Advanced Security 與其他 SAST / secret 掃描工具偵測並示範其功能。

## 包含 8 類常見弱點 (8 Common Vulnerability Types)
- `app.py` (Python)：
	- SQL 注入 (SQL Injection)
	- 弱雜湊/不安全雜湊 (Weak Hashing / MD5)
	- 硬編碼秘密 (Hard-coded Secrets)
- `insecure_server.js` (Node.js)：
	- 指令注入 (Command Injection)
	- 不安全 HTTP 服務設定 (Insecure HTTP Server Configuration)
	- 危險動態執行 `eval` (Unsafe eval / Potential Remote Code Execution)
- `Dockerfile`：
	- 過期基底映像 (Outdated Base Image)
- `requirements.txt` / `package.json`：
	- 脆弱或過時相依套件 (Vulnerable / Outdated Dependencies)
- `.github/workflows/codeql.yml`：
	- （可自行新增）示範 CodeQL 掃描流程 (CodeQL Workflow Example) – 非弱點，供自動化掃描練習。
- 假的帳號憑證與 API Keys (Fake Credentials / API Keys) – 用於 Secret Scanning 測試（非真實資料）。

## 快速執行 (Quick Start)
```bash
python app.py
node insecure_server.js
```

## 掃描練習建議 (Suggested Scans)
1. 啟用 GitHub Advanced Security → 觀察 Secret Scanning / Dependency Alerts。
2. 新增 CodeQL Workflow → 觸發 Code Scanning 報告。
3. 對 `main.tf` 執行 IaC 掃描（例如 terraform/security 工具）。
4. 測試第三方 SAST 工具（例如檢查 `eval`、命令注入、硬編碼密鑰）。

## 術語解釋 (Glossary)
### 弱點類 (Vulnerabilities)
| 中文 (English) | 說明 | GHAS 掃描來源 (GHAS Feature) |
| -------------- | ---- | ----------------------------- |
| SQL 注入 (SQL Injection) | 以惡意輸入拼接 SQL，可能讀取或竄改資料。 | Code Scanning (CodeQL) |
| 弱雜湊 / 不安全雜湊 (Weak Hashing / MD5) | 使用易被暴力破解或碰撞的雜湊演算法 (MD5)。 | Code Scanning (CodeQL) |
| 硬編碼秘密 (Hard-coded Secrets) | 將密鑰 / Token 直接寫在原始碼或設定檔中。 | Secret Scanning |
| 指令注入 (Command Injection) | 未過濾輸入直接組成系統指令，攻擊者可執行任意命令。 | Code Scanning (CodeQL) |
| 不安全 HTTP 服務設定 (Insecure HTTP Server Configuration) | 缺乏必要安全設定（如未限制來源、未使用 TLS 等）。 | Code Scanning (自訂/規則) |
| 危險動態執行 eval (Unsafe eval / Potential RCE) | 將使用者可控字串交給 `eval`，可能執行任意程式碼。 | Code Scanning (CodeQL) |
| 過期基底映像 (Outdated Base Image) | 使用含已知漏洞或未更新的容器基底映像。 | Dependency/Container Alerts (Dependabot) |
| 脆弱 / 過時相依套件 (Vulnerable / Outdated Dependencies) | 引入具已知 CVE 或不再維護之版本。 | Dependency Alerts (Dependabot) |

### 其他類 (Others)
| 中文 (English) | 說明 |
| -------------- | ---- |
| GitHub 進階安全 (GitHub Advanced Security) | GitHub 提供的進階安全功能集合（含多種掃描）。|
| Secret 掃描 (Secret Scanning) | 偵測原始碼中疑似憑證、API Key、Token 等。|
| 程式碼掃描 (Code Scanning) | 以 SAST（靜態分析）方法找出程式弱點。|
| 相依性掃描 (Dependency Scanning) | 檢查依賴套件是否含已知漏洞。|
| IaC 掃描 (Infrastructure as Code Scanning) | 分析 Terraform / Bicep 等基礎架構定義是否存在錯誤設定或風險。|
| CodeQL | GitHub 提供的語意分析與查詢引擎，用於撰寫與執行安全規則。|
| SAST | 靜態應用程式安全測試 (Static Application Security Testing)。|
| API 金鑰 (API Key) | 用於呼叫服務 API 的認證字串。|
| 假憑證 / 測試憑證 (Fake Credentials) | 為測試掃描工具而放入之非真實金鑰。|
| Terraform | 常見的 IaC 工具，用於宣告式建立雲端資源。|
| RCE | 遠端程式碼執行 (Remote Code Execution)；攻擊者可在目標環境執行任意程式碼。|

## 警告 (WARNING)
請勿在任何正式/生產環境使用此程式碼。如不慎放入真實秘密，請立刻移除並進行金鑰/密碼輪替。
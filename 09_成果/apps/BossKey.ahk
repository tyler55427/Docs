; ==============================================
; 窗口 Toggle 脚本
;
; 使用步骤：
;   1. 在下方"应用配置"区域添加应用，格式：
;      apps["应用名称"] := { winTitle: "窗口标题", lnkPath: "启动路径" }
;      - winTitle: 必填，匹配窗口标题（精确匹配）
;      - lnkPath : 必填，未运行时启动的可执行文件或快捷方式路径
;   2. 在文件末尾"快捷键绑定"区域添加热键：
;      !u:: ToggleApp("应用名称")
;      - ! = Alt, ^ = Ctrl, + = Shift, # = Win，可组合如 ^!u
; ==============================================

; 允许检测隐藏窗口
DetectHiddenWindows(true)

global apps := Map()

; ==============================================
; 应用配置
; ==============================================
; 示例（删除并替换为你的应用）:
; apps["记事本"] := { winTitle: "无标题 - 记事本", lnkPath: "notepad.exe" }
; apps["计算器"] := { winTitle: "计算器", lnkPath: "calc.exe" }

; ==============================================
; 通用查找函数
; ==============================================
FindAppWindow(appTitle) {
    ; DetectHiddenWindows 已全局开启
    allWindows := WinGetList()
    for h in allWindows {
        try {
            title := WinGetTitle("ahk_id " h)
            if (title = appTitle) {
                return h
            }
        }
    }
    return 0
}

; ==============================================
; 通用 Toggle 函数
; ==============================================
ToggleApp(appName) {
    config := apps.Get(appName)
    if !config {
        ToolTip("❌ 未找到应用配置: " appName)
        SetTimer(() => ToolTip(), -1500)
        return
    }

    ; 查找窗口（包括隐藏的）
    hWnd := FindAppWindow(config.winTitle)

    if (!hWnd) {
        ; 应用未运行：启动
        try {
            Run(config.lnkPath)
            ToolTip("🚀 " appName " 启动中...")
            SetTimer(() => ToolTip(), -1500)

            ; 等待应用窗口出现
            loop 60 {
                Sleep(200)
                hWnd := FindAppWindow(config.winTitle)
                if (hWnd) {
                    WinActivate("ahk_id " hWnd)
                    ToolTip("✅ " appName " 已启动")
                    SetTimer(() => ToolTip(), -1500)
                    break
                }
            }
        } catch as err {
            ToolTip("无法启动 " appName)
            SetTimer(() => ToolTip(), -2000)
        }
    } else {
        ; 应用已运行：切换隐藏/显示
        if DllCall("IsWindowVisible", "Ptr", hWnd) {
            WinHide("ahk_id " hWnd)
            ToolTip("🔽 " appName " 已隐藏")
            SetTimer(() => ToolTip(), -1000)
        } else {
            WinShow("ahk_id " hWnd)
            WinActivate("ahk_id " hWnd)
            ToolTip("🔼 " appName " 已显示")
            SetTimer(() => ToolTip(), -1000)
        }
    }
}


; ==============================================
; 快捷键绑定
; ==============================================
; 格式: 修饰键+键:: ToggleApp("应用名称")
; 示例（删除并替换为你的绑定）:
; !u:: ToggleApp("记事本")   ; Alt+U
; ^!h:: ToggleApp("计算器")  ; Ctrl+Alt+H
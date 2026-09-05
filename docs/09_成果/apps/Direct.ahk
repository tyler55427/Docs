#Requires AutoHotkey v2.0

CapsLock & i:: {
    Send "{Up}"
}

CapsLock & k:: {
    Send "{Down}"
}

CapsLock & j:: {
    Send "{Left}"
}

CapsLock & l:: {
    Send "{Right}"
}

CapsLock & f:: {
    Send "{Backspace}"
}

CapsLock & e:: {
    Send "{Enter}"
}

CapsLock & d:: {
    Send "{Delete}"
}

CapsLock & m:: {
    Send "{Escape}"
}

; ==============================================
; 游戏窗口 Toggle 统一管理脚本
; 快捷键：
;   Alt+J - 国王指意
;   Alt+K - 正中靶心
; ==============================================

; 允许检测隐藏窗口
DetectHiddenWindows(true)

global games := Map()

; ========== 国王指意 ==========
games["国王指意"] := {
    lnkPath: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\国王指意.lnk",
    winTitle: "国王指意"
}

; ========== 正中靶心 ==========
games["正中靶心"] := {
    lnkPath: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\正中靶心.lnk",
    winTitle: "正中靶心"
}

; ==============================================
; 通用查找函数
; ==============================================
FindGameWindow(gameTitle) {
    ; DetectHiddenWindows 已全局开启
    allWindows := WinGetList()
    for h in allWindows {
        try {
            title := WinGetTitle("ahk_id " h)
            if (title = gameTitle) {
                return h
            }
        }
    }
    return 0
}

; ==============================================
; 通用 Toggle 函数
; ==============================================
ToggleGameWithoutSuspend(gameName) {
    config := games.Get(gameName)
    if !config {
        ToolTip("❌ 未找到游戏配置: " gameName)
        SetTimer(() => ToolTip(), -1500)
        return
    }

    ; 查找窗口（包括隐藏的）
    hWnd := FindGameWindow(config.winTitle)

    if (!hWnd) {
        ; 游戏未运行：启动
        try {
            Run(config.lnkPath)
            ToolTip("🎮 " gameName " 启动中...")
            SetTimer(() => ToolTip(), -1500)

            ; 等待游戏窗口出现
            loop 60 {
                Sleep(200)
                hWnd := FindGameWindow(config.winTitle)
                if (hWnd) {
                    WinActivate("ahk_id " hWnd)
                    ToolTip("✅ " gameName " 已启动")
                    SetTimer(() => ToolTip(), -1500)
                    break
                }
            }
        } catch as err {
            ToolTip("无法启动 " gameName)
            SetTimer(() => ToolTip(), -2000)
        }
    } else {
        ; 游戏已运行：切换隐藏/显示
        if DllCall("IsWindowVisible", "Ptr", hWnd) {
            WinHide("ahk_id " hWnd)
            ToolTip("🔽 " gameName " 已隐藏")
            SetTimer(() => ToolTip(), -1000)
        } else {
            WinShow("ahk_id " hWnd)
            WinActivate("ahk_id " hWnd)
            ToolTip("🔼 " gameName " 已显示")
            SetTimer(() => ToolTip(), -1000)
        }
    }
}


; ==============================================
; 快捷键绑定
; ==============================================
!u:: ToggleGameWithoutSuspend("国王指意")   ; Alt+U
!i:: ToggleGameWithoutSuspend("正中靶心")   ; Alt+I

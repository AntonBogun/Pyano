#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetBatchLines -1
+`::
Send a+b+c
Send {e down}{e up}{w down}{w up}\
Send a
Send b
Send c
Send d
Send e
Send t
Send h
Send y
Send j
Send l
Send o
Send u
Send k
Send m
Send n
Send b
Send z
Send p
Send 1
Sleep 3000
Send b+d+mo
Sleep 3000
Send {space}abcdefg
^b::pause
return

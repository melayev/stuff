section .data
    hi db `hi there!\n`, 0
    stdout equ 1

section .text
    global _main

_main:
    ; Write "hi" to stdout (file descriptor 1) using the write function
    mov rax, 0x2000004    ; syscall number for sys_write (macOS 64-bit)
    mov rdi, stdout       ; file descriptor (stdout)
    mov rsi, hi           ; pointer to the string
    mov rdx, 11           ; length of the string, including the null terminator
    syscall

    ; Exit the program using the exit function
    mov rax, 0x2000001    ; syscall number for sys_exit (macOS 64-bit)
    xor rdi, rdi          ; status: 0
    syscall
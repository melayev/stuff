section .data
    hi db `Hi there, `, 0
    prompt_user db 'Enter your name: ', 0
    input_error_message db "Error reading input.", 0
    input_buffer db 32

    stdout equ 1
    sys_exit equ 0x02000001
    sys_read equ 0x02000003
    sys_write equ 0x02000004

section .text
    global _main

_main:
    ; Ask user to enter their name
    mov rax, sys_write
    mov rdi, stdout
    mov rsi, prompt_user
    mov rdx, 18
    syscall

    ; Read a line of input from stdin into the input buffer.
    mov rax, sys_read
    mov rdi, 0
    mov rsi, input_buffer
    mov rdx, 100
    syscall

    ; Add '!' to the end of the input_buffer before the null terminator
    mov rdi, rsi  ; Copy the address of input_buffer into rdi
    add rdi, rax  ; Move rdi to the end of the string (rax contains the number of bytes read)
    mov byte [rdi - 1], '!'  ; Replace newline with !
    inc rdi  ; Move to the position after '!'
    mov byte [rdi], `\n`  ; New line
    inc rdi
    mov byte [rdi], 0  ; Null-terminate the string

    ; Write `hi` to stdout (file descriptor 1) using the write function
    mov rax, sys_write    ; syscall number for sys_write (macOS 64-bit)
    mov rdi, stdout       ; file descriptor (stdout)
    mov rsi, hi           ; pointer to the string
    mov rdx, 11           ; length of the string, including the null terminator
    syscall

    ; Write `input_buffer` to stdout
    mov rax, sys_write
    mov rdi, stdout
    mov rsi, input_buffer
    mov rdx, 32
    syscall

    ; Exit the program using the exit function
    mov rax, sys_exit    ; syscall number for sys_exit (macOS 64-bit)
    xor rdi, rdi          ; status: 0
    syscall
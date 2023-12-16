# Menu V1.1
- [Load Store](#loadstore)
    + [Find Maximum Value](#find-maximum-value)
- [Subroutines Activation Block](#subroutines-activation-block)
    + [Return address](#return-address)
    + [Activation Stack](#activation-stack)
- [If/Else Branches](#ifelse-branches)
    + [Commands outline](#commands-outline-branches)
        - [Compare](#compare) 
        - [Branches](#branches)
    + [Basic IF/ELSE](#basic-ifelse)
    + [IF/ELSE IF](#ifelse-if)
    + [SWITCH CASE](#switch-case)
- [LOOPS](#loops)
    + [FOR](#for)
    + [WHILE](#while)
## Load/Store
#### Find Maximum Value
```asm
.section .data

.section .text
.global asm_function
asm_function:
ldi r17,8 ; set r1
mov r1,r17 

ldi r17,10 ; set r2
mov r2,r17

ldi r17,5 ; set r3
mov r3,r17

ldi r17,9 ; set r4
mov r4,r17

max_r1_to_r4:
  cp r1, r2 ; set C-flag(1) if r2>r1
  brsh found_r1_bigger_than_r2 ;branch if C is 0(clear)
  mov r1, r2
found_r1_bigger_than_r2: 
  cp r1, r3
  brsh max_r1r2_bigger_than_r3
  mov r1, r3
max_r1r2_bigger_than_r3:
  cp r1, r4
  brsh max_r1r2r3_bigger_than_r4
  mov r1, r4
max_r1r2r3_bigger_than_r4:
  mov r0, r1
  ret
ret

.end
```

## Subroutines Activation Block
#### Return address
```asm
.section .data
    array_1: .byte 1,19,4,17 ;Initialize an Array

.section .text
    .global asm_function

asm_function:
    LDI R27,hi8(array_1) ;Get array_1 address into X(R27:R26)
    LDI R26,lo8(array_1)

;PUSH elements int stack
    LD R1,X+
    PUSH R1 
    LD R1,X+
    PUSH R1
    LD R1,X+
    PUSH R1
    LD R1,X+
    PUSH R1

;Initialize a byte for return value
    PUSH R0

;Call function
    call sum_4 ;sum four numbers(parameters)

;Get the return value from stack to R15
    POP R15;

;Go back to the original stack pointer (SP) position
    POP R0
    POP R0
    POP R0
    POP R0    
    
ret

sum_4:
;SP address stored in 3E3D
;get SP -> Y register(Y: R29:R28)
    IN R29,0X3E
    IN R28,0X3D

;Load elements from stack to registers
    LDD R4,Y+4
    LDD R3,Y+5
    LDD R2,Y+6
    LDD R1,Y+7

;Add
    add R1,R4
    add R1,R3 
    add R1,R2

;Store result in Stack (space was initialized in Line22)
    STD Y+3,R1
ret

.end
```


#### Activation Stack
__Calculate result[i] = a[i] + b[i]__  
__a = [1, 7, 3, 8, 32]__  
__b = [5, 10, 15, 20, 25]__  
__result = [ ]__  
```asm
.section .data
    a: .byte 1, 7, 3, 8, 32  ;0x0100 - 0x0104
    b: .byte 5, 10, 15, 20, 25 ;0x0105 - 0x0109
    result: .space 5 ;0X010a - 0X010f

.section .text
    .global asm_function

asm_function:
    ;push a's location into stack
    ldi r20,lo8(a)
    push r20
    ldi r20,hi8(a)
    push r20

    ;push b's location into stack
    ldi r20,lo8(b)
    push r20
    ldi r20,hi8(b)
    push r20

    ;push c's location into stack
    ldi r20,lo8(result)
    push r20
    ldi r20,hi8(result)
    push r20

;After pushing addresses of a,b,c
;the stack looks like |hi8(c)|lo8(c)|hi8(b)|lo8(b)|hi8(a)|lo8(a)|

    call my_function
ret

my_function:
    POP R1
    POP R2 ; Store return address

    POP R31;
    POP R30; Z Register for result

    POP R29;
    POP R28; Y Register for b

    POP R27;
    POP R26; X Register for a

    CLR R16 ;counter
    jmp loop

loop:
    cpi R16, 5
    BREQ end_loop;

    LD R24,X+ 
    LD R25,Y+
    add R24,R25
    ST Z+,R24

    INC R16 ; i+=1
    JMP loop

end_loop:
    PUSH R2
    PUSH R1
ret


.end
```



## If/Else Branches
#### Commands outline branches
##### Compare
```asm
CP Rd,Rr
; Rd >= Rr -> Flag C = 0 
; Rd < Rr -> Flag C = 1
; Rd = Rr -> Flag Z = 0
```

```asm
CPI Rd,k
; Rd >= k -> Flag C = 0  
; Rd < k -> Flag C = 1  
; Rd = k -> Flag Z = 0  
```
##### Branches

```asm
BREQ k  
; branch if Flag Z = 1
```

```asm
BRSH k
; branch if Flag C = 0  (Rd >= Rr/Rd >= k)
```

```asm
BRLO k
; branch if Flag C = 1 (Rd < Rr/Rd < k)
```



#### Basic IF/ELSE

```python
if a > b:
    a = a + b
else:
    b = b * 2
c = a + b 
```

```asm

.section .data
a: .byte 5
b: .byte 8
c: .space 1

.section .text
    .global asm_function

asm_function:
    lds r16, a  ; r16 = a
    lds r17, b  ; r17 = b
    
    cp r16, r17 ; compute (a - b)
    brsh else   ; if a >= b, go to ELSE
            ; so if a < b, continue to IF
    
if:
    add r16, r17    ; a = a + b
    jmp end
    
else:
    lsl r17 ; b  = b * 2
        ; OR USE add r17, r17
    
end:
    sts a, r16
    sts b, r17
    
    mov r18, r17
    add r18, r16
    sts c, r18  ; c = a + b
    
    ret
    
.end
```



#### IF/ElSE IF
```python
def asm_function(input):
    if input < 10:
        return 50
    elif input < 20:
        return 100
    else:
        return 200

input_value = ...  # 假设这里有某种方式获得输入值
result = asm_function(input_value)
print("Result:", result)

```

```asm 
.section .text
.global asm_function

asm_function:
    ; 假设输入参数在 r16 寄存器中
    cpi r16, 10         ; 比较 r16 是否小于 10
    brsh else_if        ; 如果不小于，跳转到 else_if
    ldi r17, 50         ; 将 r17 设置为 50
    rjmp end_if         ; 跳转到 if 结束

else_if:
    cpi r16, 20         ; 比较 r16 是否小于 20
    brsh else_part      ; 如果不小于，跳转到 else_part
    ldi r17, 100        ; 将 r17 设置为 100
    rjmp end_if         ; 跳转到 if 结束

else_part:
    ldi r17, 200        ; 将 r17 设置为 200

end_if:
    ret                 ; 返回

```
#### SWITCH CASE
```JAVA
public class SwitchExample {
    public static void main(String[] args) {
        int input = ...;  // 假设这里有某种方式获得输入值
        int result = asmFunction(input);
        System.out.println("Result: " + result);
    }

    public static int asmFunction(int input) {
        switch (input) {
            case 1:
                return 5;
            case 2:
                return 10;
            default:
                return 255;
        }
    }
}

```


```asm
.section .text
.global asm_function

asm_function:
    ; 假设输入参数在 r16 寄存器中
    cpi r16, 1          ; 比较 r16 是否等于 1
    breq case1          ; 如果等于，跳转到 case1
    cpi r16, 2          ; 比较 r16 是否等于 2
    breq case2          ; 如果等于，跳转到 case2
    rjmp default_case   ; 如果都不是，跳转到 default_case

case1:
    ldi r17, 5          ; 将 r17 设置为 5
    rjmp end_switch     ; 跳转到 switch 结束

case2:
    ldi r17, 10         ; 将 r17 设置为 10
    rjmp end_switch     ; 跳转到 switch 结束

default_case:
    ldi r17, 255        ; 将 r17 设置为 255

end_switch:
    ret                 ; 返回

```


## LOOPS

#### FOR
```python
def asm_function():
    accumulator = 0
    for i in range(10, 0, -1):
        accumulator += i
    return accumulator

result = asm_function()
print("Result:", result)
```

```asm
.section .text
.global asm_function

asm_function:
    ldi r16, 0          ; 初始化计数器 r16 = 0
    ldi r17, 10         ; 设置循环次数 r17 = 10

for_loop:
    dec r17             ; r17 = r17 - 1
    brmi for_end        ; 如果 r17 < 0，跳出循环
    add r16, r17        ; r16 = r16 + r17
    rjmp for_loop       ; 重复循环

for_end:
    ret                 ; 返回

```

#### WHILE
```python
def asm_function():
    counter = 0
    while counter != 10:
        counter += 1
    return counter

result = asm_function()
print("Result:", result)

```

```
.section .text
.global asm_function

asm_function:
    ldi r16, 0          ; 初始化计数器 r16 = 0
    ldi r17, 10         ; 设置循环结束的条件值 r17 = 10

loop_start:
    cp r16, r17         ; 比较 r16 和 r17
    breq loop_end       ; 如果相等，跳出循环
    inc r16             ; 否则，r16 = r16 + 1
    rjmp loop_start     ; 重复循环

loop_end:
    ret                 ; 返回

```
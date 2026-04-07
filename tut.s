.globl run_turing_machine

error_code:
    .string "0"

run_turing_machine:
    mv    t6, a0              # Save original tape pointer for return
    li    t2, 48              # ASCII '0'
    li    t3, 49              # ASCII '1'
    li    t4, 66              # ASCII 'B'

    add   t0, a0, a1          # Get current head address
    lb    t1, (t0)            # Load current char
    bne   t1, t4, find_end    # If not on 'B', start scanning right
    addi  a1, a1, 1           # If on leading 'B', move to index 1 first

find_end:
    add   t0, a0, a1          
    lb    t1, (t0)           
    beqz  t1, move_left_once  # Stop at Null terminator
    beq   t1, t4, move_left_once # Stop at trailing 'B'
    
    # Character Validation
    beq   t1, t2, is_valid    
    beq   t1, t3, is_valid    
    j     error_exit          # Return 0 for invalid chars

is_valid:
    addi  a1, a1, 1           # Move head right
    j     find_end

move_left_once:
    addi  a1, a1, -1          # Move back onto the binary digits

increment_loop:
    add   t0, a0, a1          
    lb    t1, (t0)           

    beq   t1, t2, write_one   # '0' + 1 = '1' (Halt)
    beq   t1, t3, write_zero  # '1' + 1 = '0' (Carry, Move Left)
    beq   t1, t4, write_one   # Overflow into 'B': write '1' (Halt)
    j     error_exit          # Safety catch

write_one:
    li    t5, 49              
    sb    t5, (t0)            # Store '1'
    j     success_exit

write_zero:
    li    t5, 48              
    sb    t5, (t0)            # Store '0'
    addi  a1, a1, -1          # Move Left
    j     increment_loop

error_exit:
    la    a0, error_code            
    ret

success_exit:
    mv    a0, t6              # Return tape pointer
    ret



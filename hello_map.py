#!/usr/bin/python3
from bcc import BPF
from time import sleep

# BPF program to count syscalls by syscall number
program = r"""
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

// Define a hash map to store syscall counts
BPF_HASH(counter_table, u64, u64);

// Define the raw tracepoint probe for sys_enter
RAW_TRACEPOINT_PROBE(sys_enter) {
    u64 syscall_id = ctx->args[1];  // Extract the syscall ID from the raw tracepoint context
    u64 counter = 0;
    u64 *p;

    // Lookup the current count in the hash map
    p = counter_table.lookup(&syscall_id);
    if (p != 0) {
        counter = *p;  // If found, use the current count
    }

    // Increment the counter
    counter++;

    // Update the hash map with the new count
    counter_table.update(&syscall_id, &counter);
    return 0;
}
"""

# Initialize BPF
b = BPF(text=program)

# Attach BPF program to the raw syscall tracepoint
try:
    b.attach_raw_tracepoint(tp="sys_enter", fn_name="raw_tracepoint__sys_enter")
except Exception as e:
    print(f"Failed to attach to raw tracepoint: {e}")
    exit(1)

# Print syscall counts every 2 seconds
while True:
    sleep(2)
    for k, v in b["counter_table"].items():
        print(f"Syscall {k.value}: {v.value}")

#!/usr/bin/python3  
from bcc import BPF
from time import sleep

program = r"""
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

BPF_HASH(counter_table, u64, u64);

RAW_TRACEPOINT_PROBE(sys_enter) {
    u64 syscall_id = ctx->args[1]; // Get the syscall id
    u64 counter = 0;
    u64 *p;

    p = counter_table.lookup(&syscall_id);
    if (p != 0) {
        counter = *p;
    }
    counter++;
    counter_table.update(&syscall_id, &counter);

    return 0;
}
"""

# Load the eBPF program
b = BPF(text=program)

# Print the header
print("%-18s %-16s" % ("SYSCALL", "COUNT"))

# Print the map contents
def print_event():
    counter_table = b.get_table("counter_table")
    items = [(k.value, v.value) for k, v in counter_table.items()]
    for k, v in sorted(items):
        print("%-18d %-16d" % (k, v))

while True:
    try:
        sleep(1)
        print_event()
    except KeyboardInterrupt:
        exit()

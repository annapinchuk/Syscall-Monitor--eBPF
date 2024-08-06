# Syscall Monitor - eBPF
<img src="https://github.com/annapinchuk/ebpf/blob/main/images/bee.png" width="1000" height="260" />
This project provides a simple eBPF-based syscall monitor that counts the number of times each syscall is invoked on a Linux system. It uses the BPF Compiler Collection (BCC) to attach an eBPF program to the raw tracepoint for `sys_enter`, capturing all syscalls and maintaining a count for each.

This project solves Exercise 5 in Chapter 2 of the book [Learning eBPF](https://github.com/lizrice/learning-ebpf) by Liz Rice.

## Prerequisites

- Python 3
- BPF Compiler Collection (BCC)
- Linux kernel with eBPF support

## Installation

1. **Install BCC**:
    - On Ubuntu, you can install BCC using:
      ```bash
      sudo apt-get update
      sudo apt-get install bpfcc-tools linux-headers-$(uname -r)
      sudo apt-get install python3-bpfcc
      ```

2. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd syscall-monitor
    ```

## Usage

1. **Run the Program**:
    ```bash
    sudo python3 hello_map.py
    ```

This will start the syscall monitor and print the counts of each syscall every second.

#### should look like this screenshot: 

<img src="https://github.com/annapinchuk/ebpf/blob/main/images/ebpf.PNG" />

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

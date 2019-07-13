from bcc import BPF

code = '''

BPF_HASH(last);

int tracer(void *ctx) {
    u64 ts, *tsp, delta, key = 0;

    tsp = last.lookup(&key);
    if (tsp != 0) {
        delta = bpf_ktime_get_ns() - *tsp;
        if (delta < 1000000000) {
            bpf_trace_printk("%d\\n", delta / 1000000);
        }
    }
    ts = bpf_ktime_get_ns();
    last.update(&key, &ts);

    return 0;
}

int counter(void *ctx) {
    u64 c, *count, key = 1;

    count = last.lookup(&key);
    if (count != 0) {
        c = *count + 1;
        bpf_trace_printk("%d\\n", c);
    } else {
        c = 1;
    }
    last.update(&key, &c);

    return 0;
}
'''

b = BPF(text=code)
b.attach_kprobe(event=b.get_syscall_fnname("sync"), fn_name="tracer")

# Looks like we can't have two functions for same syscall
# b.attach_kprobe(event=b.get_syscall_fnname("sync"), fn_name="counter")

print("Tracing for quick sync's... Ctrl-C to end")
start = 0
while 1:
    # (task, pid, cpu, flags, ts, cnt) = b.trace_fields()
    (task, pid, cpu, flags, ts, ms) = b.trace_fields()
    if start == 0:
        start = ts
    ts = ts - start
    # print("Call count: %s" % cnt)
    print("At time %.2f s: multiple syncs detected, last %s ms ago" % (ts, ms))

from bcc import BPF

code = '''
#include <linux/blkdev.h>

BPF_HASH(start, struct request *);

void trace_start(struct pt_regs *ctx, struct request *req) {
    u64 ts = bpf_ktime_get_ns();
    start.update(&req, &ts);
}

void trace_completion(struct pt_regs *ctx, struct request *req) {
    u64 *tsp, delta;

    tsp = start.lookup(&req);
    if (tsp != 0) {
        delta = bpf_ktime_get_ns() - *tsp;
        bpf_trace_printk("%d %x %d\\n", req->__data_len, req->cmd_flags, delta / 1000);
        start.delete(&req);
    }
}

'''

b = BPF(text=code)
b.attach_kprobe(event="blk_start_request", fn_name="trace_start")
b.attach_kprobe(event="blk_account_io_completion", fn_name="trace_completion")

print ("%-18s %-7s %8s" % ("TIME(s)", "BYTES", "LAT(ms)"))
while True:
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
        (bytes, flags, us) = msg.split()
        ms = float(int(us, 10)) / 1000
        print ("%-18.9f %7s %8.2f" % (ts, bytes, ms))
    except KeyboardInterrupt:
        exit()

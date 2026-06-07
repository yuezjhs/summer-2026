import re, os

base = "/mnt/c/Users/yuezj/Desktop/my-first-git-project"
with open(os.path.join(base, "study-plan.md"), "r", encoding="utf-8") as f:
    content = f.read()

# ----- Extension content for each day -----
E = {}

E[1]  = "- [ ] 写 `get_min_max(int *arr, int len, int *min, int *max)`——通过指针参数返回多个值\n- [ ] 研究 `restrict` 关键字——它告诉编译器\"这个指针是唯一访问这块内存的途径\""

E[2]  = "- [ ] 自己实现 `memcpy`——考虑内存重叠的情况（src 和 dst 有重叠时要用 memmove 的逻辑）\n- [ ] 写 `int *find(int *arr, int len, int target)`，返回第一个匹配元素的地址，找不到返回 NULL"

E[3]  = "- [ ] 手写 `strncpy`（安全版，限制复制长度）\n- [ ] 写一个简单的 trim 函数——去掉字符串首尾的空格和换行符"

E[4]  = "- [ ] 写 `int **create_matrix(int rows, int cols)`——用 malloc 分配二维数组\n- [ ] 写 `free_matrix(int **m, int rows)`——正确释放二维数组的每一行"

E[5]  = "- [ ] 写一个简单的插件系统：定义 `typedef void (*plugin_fn)(void)`，用函数指针数组存插件\n- [ ] 研究 Linux 内核中 `signal()` 的声明——它的参数就是函数指针"

E[6]  = "- [ ] 写通用数组反转函数 `void reverse_array(void *arr, int len, size_t elem_size)`\n- [ ] 研究 `qsort` 的 man page——理解它的比较函数约定（返回负/零/正）"

E[7]  = "- [ ] 给计算器加上取模(%)、幂运算(^)、括号嵌套\n- [ ] LeetCode 刷 2 道简单题：Two Sum(1)、Valid Parentheses(20)"

E[8]  = "- [ ] 写 `safe_malloc`——包装 malloc，失败时打印错误并 exit\n- [ ] 用 valgrind 跑今天的程序：`valgrind --leak-check=full ./prog`，读懂输出"

E[9]  = "- [ ] 实现 `insert_at(da, index, value)`——中间插入，后面元素后移\n- [ ] 实现 `remove_at(da, index)`——中间删除，后面元素前移\n- [ ] 实现 `shrink_to_fit`——容量缩到刚好等于 size"

E[10] = "- [ ] 用递归反转单向链表——理解递归和链表的配合\n- [ ] 检测链表是否有环（Floyd 快慢指针法）——LeetCode 141"

E[11] = "- [ ] 实现循环链表——尾节点的 next 指向头节点\n- [ ] 用循环链表解决约瑟夫问题（Josephus problem）"

E[12] = "- [ ] 用两个栈实现一个队列（LeetCode 232）\n- [ ] 实现最小栈（LeetCode 155）——常数时间内获取最小值"

E[13] = "- [ ] 实现哈希表自动扩容——负载因子 > 0.75 时扩容为原来的 2 倍\n- [ ] 了解 DJB2 哈希函数——比取模更均匀的哈希算法"

E[14] = "- [ ] 给电话簿加模糊搜索——输入\"张\"列出所有姓张的联系人\n- [ ] 研究 SQLite 的 C API——理解数据库和文件存储的区别"

E[15] = "- [ ] 用 `offsetof` 宏查看字段在结构体中的偏移量\n- [ ] 研究 Linux 内核中 `container_of` 宏——从成员指针反推结构体指针"

E[16] = "- [ ] 实现 bitmap——用每一位代表一个 bool，节省 8 倍内存\n- [ ] 用位操作实现一个简单的 Base64 编码器"

E[17] = "- [ ] 实现简单的文件加密：每个字节 XOR 一个 key，再跑一次解密\n- [ ] 实现 tail 命令——打印文件最后 N 行（从末尾反向读）"

E[18] = "- [ ] 了解 CMake 的基本用法——写一个 CMakeLists.txt 替代 Makefile\n- [ ] 试试 gcc 的 `-I`（头文件路径）、`-L`（库路径）、`-l`（库名）选项"

E[19] = "- [ ] 支持 JSON 格式保存数据（用 cJSON 库或手写简单序列化）\n- [ ] 支持按邮箱查找、按电话查找\n- [ ] 支持导入/导出 VCF 格式（vCard）"

E[21] = "- [ ] 了解 `do { ... } while(0)` 在宏中的用法——为什么这么写\n- [ ] 了解 X-Macros 模式——用宏生成重复代码"

E[22] = "- [ ] 了解 GDB 的 TUI 模式（`gdb -tui`）——图形化调试界面\n- [ ] 了解 pwndbg 插件——CTF 常用的 GDB 增强"

E[23] = "- [ ] 写程序读取自己的 `/proc/self/maps`，解析每一行\n- [ ] 了解 /proc/self/mem——可以直接读写进程内存"

E[24] = "- [ ] 研究 glibc malloc 的 bin 结构——fastbin/smallbin/largebin/unsorted bin\n- [ ] 了解 Doug Lea malloc (dlmalloc) 的设计思想——大多数 malloc 的祖先"

E[26] = "- [ ] 了解不同调用约定：cdecl（调用者清栈）、stdcall（被调者清栈）、fastcall（寄存器传参）\n- [ ] 对比 32 位和 64 位的函数调用 ABI 差异"

E[28] = "- [ ] 了解 ELF 文件的加载过程——execve 在内核中做了什么\n- [ ] 理解 PLT/GOT 的惰性绑定（lazy binding）机制——为什么首次调用慢"

E[30] = "- [ ] 了解 LD_PRELOAD——在程序启动前注入自己的 .so\n- [ ] 用 LD_PRELOAD 劫持 malloc，记录每次分配的大小"

E[32] = "- [ ] 给极简 shell 加上管道 `|`——需要 pipe() + dup2()\n- [ ] 理解 dup2 的原理：复制文件描述符到指定编号"

E[34] = "- [ ] 写一个简单的守护进程（daemon）——fork 两次脱离终端\n- [ ] 了解进程组（process group）和会话（session）的概念"

E[36] = "- [ ] 给 shell 加上环境变量支持：`export NAME=VALUE`、`echo $NAME`\n- [ ] 加上 I/O 重定向：`command > file`、`command < file`"

E[39] = "- [ ] 读 CSAPP 第 9 章（虚拟内存）概述——理解页表和 TLB\n- [ ] 了解 mmap 和 brk 的区别——用户空间内存分配的两条路"

E[41] = "- [ ] 研究 TCP 状态机完整图——11 种状态的转换条件\n- [ ] 了解 TCP 拥塞控制算法（慢启动/拥塞避免/快速恢复）"

E[43] = "- [ ] 写一个简单的聊天客户端（用 select 同时监听 stdin 和 socket）\n- [ ] 了解 getaddrinfo()——比 gethostbyname 更现代的 DNS 解析"

E[45] = "- [ ] 了解 poll() 和 epoll()——select 的现代替代品\n- [ ] 对比 select/poll/epoll 的性能差异和应用场景"

E[47] = "- [ ] 加 UDP 端口扫描——UDP 扫描比 TCP 更不可靠（无响应不代表关闭）\n- [ ] 尝试 OS 指纹识别：通过 TTL 值、TCP 窗口大小推断操作系统"

E[49] = "- [ ] 加 POST 请求解析——读取 Content-Length + 请求体\n- [ ] 加文件服务——请求 `/file/xxx` 返回本地文件，自动识别 MIME 类型"

E[51] = "- [ ] 加 UDP 数据包解析——UDP 头只有 8 字节\n- [ ] 尝试解析 DNS 查询包——理解 DNS 报文格式"

E[53] = "- [ ] 了解 libpcap——比 raw socket 更高级的抓包库（tcpdump 基于它）\n- [ ] 给抓包工具加 BPF 过滤器——只抓特定协议/端口的包"

E[55] = "- [ ] 对比不同编译优化级别（-O0/-O1/-O2/-O3）对栈布局的影响\n- [ ] 用 `checksec` 查看编译出的程序的保护机制"

E[57] = "- [ ] 不用 pwntools 的 shellcraft——手写 execve(\"/bin/sh\") 的 x86-64 汇编，转机器码\n- [ ] 了解 msfvenom——Metasploit 的 payload 生成器"

E[59] = "- [ ] 了解 one_gadget 工具——libc 中可以直接拿 shell 的单条地址\n- [ ] 研究不同 libc 版本（2.31/2.35/2.39）中偏移的差异"

E[61] = "- [ ] 了解 ret2csu——`__libc_csu_init` 中的万能 gadget\n- [ ] 了解 ret2dlresolve——绕过 ASLR 的高级技术（仅概念了解）"

E[63] = "- [ ] 练习 %hhn 逐字节写入——分 4 次写一个 32 位地址\n- [ ] 研究 pwntools 的 `fmtstr_payload()`——自动生成格式化字符串 payload"

E[65] = "- [ ] 尝试 CSAPP Attack Lab Phase 5（最难的一关，做不出来正常）\n- [ ] 了解堆利用基本概念：tcache poisoning、fastbin dup（大学再深入）"

E[68] = "- [ ] 给 IDS 加 BPF 过滤器——只抓需要的流量，降低 CPU\n- [ ] 加守护进程模式——fork + setsid 后台运行\n- [ ] 加日志轮转——每天一个日志文件，自动清理 7 天前的"

E[71] = "- [ ] 了解 tcache 的基本结构——glibc 2.26+ 引入的线程缓存\n- [ ] 了解堆漏洞的实际案例——CVE 搜索 \"heap overflow\" 或 \"use after free\""

E[74] = "- [ ] 了解 AES 的查表优化实现——比朴素实现快 10 倍\n- [ ] 了解 AES-NI——CPU 硬件加速 AES 的指令集"

E[77] = "- [ ] 创建个人 GitHub Pages 网站——`username.github.io`\n- [ ] 写一篇项目介绍放在 GitHub Pages 上"

E[79] = "- [ ] 把博客投稿到安全客或 FreeBuf——增加曝光\n- [ ] 在知乎回答 3 个 C 语言/安全相关的问题——建立社区存在"

E[81] = "- [ ] 在拉勾/Boss 直聘上搜\"渗透测试 实习\"，看真实的 JD 要求\n- [ ] 研究 3 家你感兴趣的安全公司——奇安信/长亭/默安科技"

E[83] = "- [ ] 搜索 5 家安全乙方公司的产品线——WAF/IDS/EDR/漏洞扫描器\n- [ ] 分析他们的技术架构有什么共性——检测引擎/规则引擎/管理平台"

E[85] = "- [ ] 给 4 年后的自己写一封信——你希望大学毕业时成为什么样的人\n- [ ] 把 GitHub 绿点日历截图——85 天不间断提交，这是你暑假最好的证明"

# Map multi-day ranges to their starting day
for src,dst in [(20,19),(25,24),(27,26),(29,28),(31,30),(33,32),(35,34),
                  (38,36),(40,39),(42,41),(44,43),(46,45),(48,47),(50,49),
                  (52,51),(54,53),(56,55),(58,57),(60,59),(62,61),(64,63),
                  (67,65),(70,68),(73,71),(76,74),(78,77),(80,79),(82,81),(84,83)]:
    if src not in E: E[src] = E[dst]

# ----- Simple approach: find each GitHub提交 line, find next ```, insert after -----
lines = content.split("\n")
output = []
i = 0

while i < len(lines):
    output.append(lines[i])

    # Found a GitHub commit section
    if "📦 GitHub" in lines[i]:
        # Find the closing ``` of the bash block
        j = i
        in_block = False
        close_line = -1
        while j < len(lines):
            if lines[j].strip() == "```bash":
                in_block = True
            elif lines[j].strip() == "```" and in_block:
                close_line = j
                break
            j += 1

        if close_line > 0:
            # Find which day we're in
            day = 0
            for k in range(i, -1, -1):
                dm = re.match(r"## Day (\d+)", lines[k])
                if dm: day = int(dm.group(1)); break
                dm2 = re.match(r"## Day (\d+)-(\d+)", lines[k])
                if dm2: day = int(dm2.group(1)); break

            # Check if extension already exists
            has_ext = False
            for k in range(close_line, min(close_line+8, len(lines))):
                if "🔮 扩展" in lines[k]:
                    has_ext = True
                    break

            if not has_ext and day in E:
                # Insert extension between closing ``` and next content
                # First, advance i to the closing ``` line
                while i < close_line:
                    i += 1
                    output.append(lines[i])

                # Now insert extension block
                output.append("")
                output.append("**🔮 扩展（核心任务完成后）**")
                for ext_line in E[day].split("\n"):
                    output.append(ext_line)
                output.append("")

    i += 1

with open(os.path.join(base, "study-plan.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(output))

# Verify
with open(os.path.join(base, "study-plan.md"), "r", encoding="utf-8") as f:
    final = f.read()
ext_count = final.count("🔮 扩展")
gh_count = final.count("📦 GitHub")
print(f"GitHub blocks: {gh_count}, Extensions: {ext_count}")
print("DONE - all extensions added" if ext_count == gh_count else f"MISSING {gh_count - ext_count}")

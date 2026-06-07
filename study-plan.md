# 暑假极限计划 · V4 日课版

> 起点：C 语言基础语法会，指针概念知道但用不熟，指针之后的内容（动态内存、结构体、链表、文件IO、模块化）较弱
> 终点：能独立写网络工具、理解二进制漏洞、GitHub 上有拿得出手的项目
> 原则：**先补短板到能打仗，再往舒适区外推**

---

## 🖥 前置准备：软件安装清单（Day 0 · 今天就做）

### 你已有的 ✅

| 软件 | 用途 | 状态 |
|------|------|------|
| VS Code | 写代码（配合 WSL 远程开发） | ✅ |
| Ubuntu WSL | Linux 开发环境 | ✅ |
| Git Bash | 版本控制 | ✅ |
| Python 3 | pwntools 等工具依赖 | ✅ |
| Miniconda3 | Python 环境管理 | ✅ |

### 需要安装的 🔧

#### WSL 内安装（打开 Ubuntu 终端，逐条执行）

```bash
# 1. 更新包管理器
sudo apt update && sudo apt upgrade -y

# 2. C 开发工具链（gcc、gdb、make、binutils）—— 大概率已有，没有就装
sudo apt install -y build-essential gcc gdb make binutils

# 3. 内存检测工具
sudo apt install -y valgrind

# 4. 网络工具
sudo apt install -y netcat-openbsd hping3 curl wget

# 5. Python + pip（pwntools 依赖）
sudo apt install -y python3 python3-pip

# 6. pwntools —— CTF 必备，Day 57 才用但提前装好
pip3 install pwntools

# 7. ROPgadget —— 找 ROP gadget，Day 63 用
pip3 install ROPgadget

# 8. pwndbg —— GDB 的 Pwn 增强插件（可选，装了 GDB 会变好看）
#    如果安装失败就先跳过，原生 GDB 也够用
git clone https://github.com/pwndbg/pwndbg ~/pwndbg
cd ~/pwndbg && ./setup.sh
# 如果 setup 报错 → 跳过，用原生 GDB。开学后再折腾。

# 9. checksec —— 查看二进制保护机制
pip3 install checksec

# 10. OpenSSL 开发库 —— Day 78 用
sudo apt install -y libssl-dev

# 11. 验证所有工具装好了
gcc --version
gdb --version
python3 -c "from pwn import *; print('pwntools OK')"
valgrind --version
```

#### Windows 端安装

| 软件 | 用途 | 下载 | 什么时候用 |
|------|------|------|-----------|
| **Wireshark** | 抓包分析 | https://www.wireshark.org/download.html | Day 43 |
| **Ghidra** | 逆向分析（NSA 开源） | https://ghidra-sre.org （需 Java JDK 17+） | Day 82+（大学继续用） |

---

### 安装验证清单

在 WSL 终端跑以下命令，全部有输出即为就绪：

```bash
# 编译器
gcc --version          # 预期：gcc 9.x 或 11.x

# 调试器  
gdb --version          # 预期：GDB 9.x 或 12.x

# 内存检测
valgrind --version     # 预期：valgrind-3.x

# 网络
nc -h 2>&1 | head -1   # 预期：OpenBSD netcat

# Python 工具
python3 -c "from pwn import *; print('✓ pwntools')"
python3 -c "import ROPgadget; print('✓ ROPgadget')"
checksec --version 2>/dev/null || python3 -c "import pwn; pwn.checksec('')" 2>/dev/null; echo "✓ checksec"

# 二进制分析
objdump --version       # 预期：GNU objdump
readelf --version       # 预期：GNU readelf

echo "======= 安装验证完毕 ======="
```

---

### VS Code 配置建议

在 VS Code 里装两个插件，开发体验提升一个档次：

| 插件 | 用途 |
|------|------|
| **WSL** (ms-vscode-remote.remote-wsl) | 在 VS Code 里直接连接 WSL，编辑 Linux 上的文件 |
| **C/C++** (ms-vscode.cpptools) | C 语言语法高亮、智能提示、GDB 集成调试 |

用法：打开 VS Code → 左下角绿色按钮 → "Connect to WSL" → 在 WSL 里 `code .` 打开项目。

---

### 各阶段需要的工具速查

| 阶段 | 需要的工具 | 已装？ |
|------|-----------|--------|
| 第 1-4 周 | gcc, gdb, make, git, valgrind, AddressSanitizer | ✅ |
| 第 5-6 周 | objdump, readelf, nm | ✅ (binutils 自带) |
| 第 7-9 周 | nc, hping3, Wireshark(Windows), curl | ✅ |
| 第 10-12 周 | pwntools, ROPgadget, checksec, pwndbg | ✅ |
| 第 13 周 | libssl-dev, Ghidra(Windows) | ✅ |

---

> **今天就把 WSL 里的软件装完。验证清单跑一遍，全部打勾后再进入 Day 1。**

---

## 📋 每日任务结构

每天的任务按四个类别组织：

| 标签 | 含义 | 在哪做 | 性质 |
|------|------|--------|------|
| 🔧 **动手** | 写代码 | 图书馆上午 | **必须完成**——今天的核心产出 |
| 📖 **理论** | 读教材/看文档 | 图书馆上午 | **必须完成**——动手前的知识准备 |
| 🧪 **验证** | 调试/测试/跑实验 | 图书馆下午 | **必须完成**——验证上午写的东西 |
| 📝 **验收** | 能独立做到的事 | 图书馆下午结束前 | **自检标准**——做不到就明天补 |
| 📚 **夜读** | 轻阅读，不写代码 | 晚饭后 | **可选**——累了就读，不累就读 |

---

## 📐 嵌入你的日程

```
6:00-8:00   晨跑 + 洗澡 + 做饭 + 早饭
8:30-11:40  【图书馆】 🔧动手 + 📖理论（大脑最好，攻最难的东西）
14:00-17:30 【图书馆】 🧪验证 + 📝验收（下午做实验和自检）
19:00-20:30 【家里】   📚夜读（沙发上看书，不动电脑）
```

---

# 第一阶段：C 语言硬骨头（Day 1-28）

---

## 第 1 周：指针从"知道"到"闭卷能写"

---

### Day 1 · 环境搭建 + 指针重新认识

**📖 理论（图书馆·上午）**
- 重读《C和指针》第 1-2 章到指针部分
- 核心问题：`&` 和 `*` 为什么互为逆运算？
- 核心问题：指针本身也是一个变量——它的值是什么？它的地址是什么？

**🔧 动手（图书馆·上午）**
- [ ] 在 Linux 下用 gcc 编译一个 hello world —— 加 `-Wall -Wextra` 看清所有警告
- [ ] 写程序：定义 `int a = 42`，打印 a 的值、a 的地址
- [ ] 写程序：`int *p = &a`，打印 p 的值（= a 的地址）、*p 的值（= 42）、&p 的值（= p 自己的地址）
- [ ] 画一张内存图：标出 a、p 各自的地址和值，箭头从 p 指向 a

**🧪 验证（图书馆·下午）**
- [ ] 修改 a 的值，观察 *p 是否跟着变了
- [ ] 修改 *p 的值，观察 a 是否跟着变了
- [ ] 写函数 `add_one(int x)` 和 `add_one_ptr(int *x)`——分别调用，看效果区别

**📝 验收**
- ✅ 能闭卷写出：取地址、解引用、通过指针修改变量
- ✅ 能一句话讲清"传值"和"传指针"的区别

**📚 夜读**
- 翻《编码》前 5 章（继电器 → 二进制 → 门电路），不用记，当故事看

**🔮 扩展（核心任务完成后才做）**
- 写一个函数 `get_min_max(int *arr, int len, int *min, int *max)`——通过指针参数返回多个值
- 这就是 C 语言"返回多个值"的惯用法——没有之一

---

### Day 2 · 指针与数组

**📖 理论（图书馆·上午）**
- 读《C和指针》数组与指针的章节
- 核心问题：`arr[i]` 和 `*(arr+i)` 为什么完全等价？
- 核心问题：数组名是什么？数组名和指针的区别是什么？

**🔧 动手（图书馆·上午）**
- [ ] 用指针遍历数组（不写 `[]`）：打印每个元素、求和、找最大值
- [ ] 自己写 `strlen`——就 3 行，手写不要查
- [ ] 写函数 `double_array(int *arr, int len)`——每个元素翻倍

**🧪 验证（图书馆·下午）**
- [ ] 在主函数里定义一个数组，传进 double_array，打印结果
- [ ] 把数组名赋值给 `int *p`，用 p++ 遍历，打印每次的地址——观察地址每次 +4
- [ ] 把 `char *p` 指向一个 char 数组，用 p++ 遍历，打印每次的地址——观察地址每次 +1
- [ ] 对比：`int *p` 加 1 移动 4 字节，`char *p` 加 1 移动 1 字节——理解"指针的类型决定步长"

**📝 验收**
- ✅ 不写 `[]`，纯指针遍历数组 3 遍不出错
- ✅ 能闭卷写出 strlen

**📚 夜读**
- 《编码》第 6-8 章（加法器的构造）

**🔮 扩展**
- 写 `int *find(int *arr, int len, int target)`——返回第一个匹配元素的地址，找不到返回 NULL
- 用指针减法算两个指针之间的元素个数

---

### Day 3 · 字符串操作

**📖 理论（图书馆·上午）**
- 读《C和指针》字符串章节
- 核心问题：C 字符串本质是什么？（`\0` 结尾的 char 数组）
- 核心问题：`char s[] = "hello"` 和 `char *s = "hello"` 的区别是什么？

**🔧 动手（图书馆·上午）**
- [ ] 手写 `strcpy`——复制字符串
- [ ] 手写 `strcat`——拼接字符串
- [ ] 手写 `strcmp`——比较字符串
- [ ] 原地反转字符串（不要开新数组）

**🧪 验证（图书馆·下午）**
- [ ] 用你写的 strcpy 复制一个字符串，检查结果
- [ ] 用你写的 strcmp 比较 "abc" 和 "abd"——应该返回负值
- [ ] 写程序：尝试修改 `char *s = "hello"` 指向的字符串——观察 segfault
- [ ] 写程序：修改 `char s[] = "hello"`——成功。在笔记里写清楚为什么

**📝 验收**
- ✅ 闭卷手写 strcpy、strcat、strcmp 一遍过

**📚 夜读**
- 《编码》第 9-11 章（触发器、锁存器、寄存器）

**🔮 扩展**
- 手写 `strncpy`（安全版，限制复制长度）
- 把字符串中所有的空格替换成 `%20`（原地替换，LeetCode 经典题）

---

### Day 4 · 多级指针 + 命令行参数

**📖 理论（图书馆·上午）**
- 《C和指针》多级指针部分
- 核心问题：`int **pp` 是什么？指向指针的指针
- 核心问题：`argv` 的类型是什么？为什么 `char *argv[]` = `char **argv`？

**🔧 动手（图书馆·上午）**
- [ ] 写函数 `void change_ptr(int **pp)`——修改一个指针本身（不是修改它指向的值）
- [ ] 写计算器 `./calc 12 + 34` → 输出 46。用 argc/argv 解析参数
- [ ] 写 `./echo hello world` → 每行打印一个参数

**🧪 验证（图书馆·下午）**
- [ ] 在主函数里定义一个 `int *p = NULL`，传给 change_ptr，检查 p 是否被修改了
- [ ] 画内存图：int a → int *p → int **pp，三层指针各存在哪、各指向哪
- [ ] 测试 `./calc` 没有参数时不要崩溃——检查 argc

**📝 验收**
- ✅ 能闭卷写出"修改指针本身的函数"（需要传 `**`）
- ✅ 能写出带命令行参数的程序

**📚 夜读**
- 《编码》第 12-14 章（计数器、内存组织、CPU 雏形）

**🔮 扩展**
- 写函数创建二维数组 `int **create_matrix(int rows, int cols)`，用 `malloc` 分配（如果还没学 malloc 可以先跳过，后面回头做）
- 写程序：把 argv 里的字符串按字母排序再打印

---

### Day 5 · 函数指针

**📖 理论（图书馆·上午）**
- 《C和指针》函数指针章节
- 核心问题：函数也有地址吗？怎么用指针指一个函数？
- 核心问题：qsort 为什么需要一个"比较函数"作为参数？

**🔧 动手（图书馆·上午）**
- [ ] 定义函数指针 `int (*f)(int)`，指向一个 square 函数，通过指针调用
- [ ] 写 `map(int *arr, int len, int (*f)(int))`——对每个元素执行 f
- [ ] 写 3 个转换函数（square、cube、negate），传给 map，验证结果

**🧪 验证（图书馆·下午）**
- [ ] 用 map + 3 种函数分别跑，打印结果
- [ ] 用 libc 的 qsort 排序一个整数数组——理解比较函数是怎么被调用的
- [ ] 写一个计算器：加减乘除 4 个函数，用函数指针数组存，根据操作符选择

**📝 验收**
- ✅ 能闭卷写出 map 函数和调用方式
- ✅ 能给 qsort 写比较函数

**📚 夜读**
- 《编码》第 15-16 章（完整的 CPU 模型、指令集）

**🔮 扩展**
- 用函数指针实现简单的回调机制：模拟"下载完成时调用回调函数通知"
- 研究一下 Linux 内核中 `signal` 函数的声明——它就是用的函数指针

---

### Day 6 · void 指针 + 泛型思维

**📖 理论（图书馆·上午）**
- 什么是 `void *`？——"我不知道指向什么类型的指针"
- 为什么需要 void *？——写通用函数时不知道数据类型
- 核心限制：不能直接解引用 void *（因为不知道类型），不能做指针算术

**🔧 动手（图书馆·上午）**
- [ ] 写通用 swap：`void swap(void *a, void *b, size_t size)`——用 memcpy + 临时 buffer
- [ ] 写通用数组打印：`void print_array(void *arr, int len, size_t elem_size, void (*print_elem)(void *))`
- [ ] 写通用查找：`int find_index(void *arr, int len, size_t elem_size, void *target, int (*cmp)(void *, void *))`

**🧪 验证（图书馆·下午）**
- [ ] 用通用 swap 交换 int、double、字符串（char *）
- [ ] 用通用 print_array 打印 int 数组和 double 数组
- [ ] 用通用 find_index 在 int 数组中找目标值

**📝 验收**
- ✅ 能闭卷写出一个使用 void * 的通用函数
- ✅ 能解释 void * 为什么不能直接解引用

**📚 夜读**
- 《编码》第 17 章（回顾整条 CPU 建造路线）

**🔮 扩展**
- 研究 `memcpy` 的 man page——它的参数就是 void *，理解为什么它能复制任意类型
- 写一个通用数组反转函数，支持任意元素类型

---

### Day 7 · 缓冲 + 闭卷考核

**今天不学新东西。**

**📝 闭卷自检（必须完成）**
- [ ] 手写 strlen → strcpy → strcmp → swap(int *) → swap(int **) → map → 通用 swap(void *)
- [ ] 任选一个，卡住了就重写，写到不卡为止
- [ ] 重读这一周的笔记

**🔧 迷你项目（下午）**
- [ ] 写一个程序 `calc`：支持 `./calc "1 + 2 * 3"`——处理加减乘除和括号。不要求优雅，跑对就行
- 这个项目一次性用到：指针、字符串解析、函数指针（4 个运算符）

**📚 夜读**
- 本周《编码》没读完的部分接着读

---

## 第 2 周：动态内存 + 数据结构

---

### Day 8 · malloc 和 free

**📖 理论（图书馆·上午）**
- 《C和指针》动态内存章节
- 核心问题：堆和栈的区别？（栈 = 自动分配释放，堆 = 手动 malloc/free）
- 核心问题：malloc 返回的是什么？（void *，指向堆上一块至少 N 字节的内存）

**🔧 动手（图书馆·上午）**
- [ ] `int *p = malloc(sizeof(int))`——在堆上分配一个 int，写 42，打印
- [ ] `int *arr = malloc(10 * sizeof(int))`——在堆上分配 10 个 int 的数组，赋值，打印
- [ ] `free(p); free(arr)`——释放
- [ ] **不要忘了 `#include <stdlib.h>`**

**🧪 验证（图书馆·下午）**
- [ ] 写死循环 `malloc(1024*1024)` 不 free——打开 htop 看内存增长（跑几秒钟就 Ctrl+C 杀掉）
- [ ] `free(p)` 之后 `printf("%d", *p)`——观察悬空指针的行为（可能正常可能 segfault）
- [ ] 两次 free 同一块内存——观察 double free 的崩溃
- [ ] 用 `gcc -fsanitize=address -g` 编译，让它帮你找内存问题

**📝 验收**
- ✅ 每次写 malloc 能条件反射地找到对应的 free 在哪
- ✅ 能解释内存泄漏、悬空指针、double free 是什么

**📚 夜读**
- 《CSAPP》第 9 章 9.9 节（动态内存分配概述），只读概述，不用细读算法

**🔮 扩展**
- 写一个函数 `safe_malloc`——包装 malloc，分配失败时打印错误并 exit
- 研究 valgrind：`valgrind --leak-check=full ./your_program`

---

### Day 9 · 动态数组

**📖 理论（图书馆·上午）**
- 理解：固定数组的问题——不知道用户要用多大
- 理解：动态数组的策略——满了扩容（通常是翻倍）
- realloc：原地扩展（如果后面有空闲）或者搬走（如果后面没空间）

**🔧 动手（图书馆·上午）**
- [ ] 定义结构体：
  ```c
  typedef struct {
      int *data;
      int size;     // 当前元素个数
      int capacity; // 已分配空间能存几个
  } DynArray;
  ```
- [ ] 实现 `init(da)`——初始容量 4
- [ ] 实现 `push_back(da, value)`——满了就 realloc 翻倍
- [ ] 实现 `pop_back(da)`——返回最后一个元素，size 减 1
- [ ] 实现 `get(da, index)`——有边界检查
- [ ] 实现 `free_da(da)`——释放 data

**🧪 验证（图书馆·下午）**
- [ ] push_back 100 个数，观察 capacity 的变化（应该从 4→8→16→32→64→128）
- [ ] 用 `-fsanitize=address` 检查内存泄漏
- [ ] 测试 pop_back 到负数时不要崩溃

**📝 验收**
- ✅ 闭卷写出动态数组 push_back（扩容逻辑）和 pop_back
- ✅ push_back 100 次后所有数据还在

**📚 夜读**
- 《CSAPP》第 9 章 9.11 节（常见内存错误），里面讲的每种错误你今天都可能在实验里碰到

**🔮 扩展**
- 实现 `insert_at(da, index, value)`——中间插入，后面的元素往后移
- 实现 `remove_at(da, index)`——中间删除，后面的元素往前移

---

### Day 10 · 单向链表

**📖 理论（图书馆·上午）**
- 《C和指针》链表章节
- 核心问题：为什么需要链表？（数组插入中间 O(n)，链表 O(1)）
- 核心问题：链表节点 = 数据 + 指向下一个节点的指针
- 核心认知：链表的难点不是"看懂"，是"指针修改的顺序"

**🔧 动手（图书馆·上午）**
- [ ] 定义节点：
  ```c
  typedef struct Node {
      int data;
      struct Node *next;
  } Node;
  ```
- [ ] head_insert —— 新节点插到最前面
- [ ] tail_insert —— 新节点插到最后面
- [ ] find —— 按值查找，返回节点指针
- [ ] delete —— 按值删除第一个匹配节点
- [ ] print_all —— 遍历打印

**🧪 验证（图书馆·下午）**
- [ ] 测试 tail_insert 连续插入 5 个数，print_all 验证顺序
- [ ] 测试 delete——删除头节点、中间节点、尾节点、不存在的节点
- [ ] **画图**：delete 时一共要改几个指针？先改谁后改谁？画清楚了再写

**📝 验收**
- ✅ 闭卷写出单向链表的 insert、delete、print
- ✅ delete 四种情况（头、中、尾、不存在）都测过

**📚 夜读**
- 《C和指针》链表章节从头再翻一遍，重点关注"指针的指针"用法（如果有的话）

**🔮 扩展**
- 反转单向链表（迭代版）——LeetCode 206，面试必考
- 用递归反转单向链表——理解递归和链表的配合

---

### Day 11 · 双向链表 + 队列

**📖 理论（图书馆·上午）**
- 双向链表比单向多了什么？——多一个 prev 指针
- 好处：删除节点时不需要从头找前驱
- 代价：插入/删除时多改一个指针；每个节点多 8 字节

**🔧 动手（图书馆·上午）**
- [ ] 定义双向链表节点：data + next + prev
- [ ] head_insert、tail_insert、delete、find、print_forward、print_backward
- [ ] 用双向链表实现队列：enqueue(tail_insert)、dequeue(delete_head)
- [ ] 用双向链表实现栈：push(head_insert)、pop(delete_head)

**🧪 验证（图书馆·下午）**
- [ ] 双向链表 delete——四种情况：头、尾、中间、只剩一个节点
- [ ] 队列 enqueue 10 个 dequeue 10 个，顺序对吗？
- [ ] 画图：双向链表删除节点时一共改了几个指针？（2-4 个，取决于位置）

**📝 验收**
- ✅ 闭卷写出双向链表删除节点（不管节点在哪）
- ✅ 用链表实现队列和栈

**📚 夜读**
- 《CSAPP》第 3 章 3.8（数组分配和访问）——理解数组在汇编层面

**🔮 扩展**
- 实现循环链表——尾节点的 next 指向头节点
- 用循环链表解决约瑟夫问题

---

### Day 12 · 栈和队列（独立实现+应用）

**📖 理论（图书馆·上午）**
- 今天不读新内容——复习前 3 天的概念
- 栈：LIFO（后进先出）——函数调用栈就是栈
- 队列：FIFO（先进先出）——打印队列、消息队列都是队列

**🔧 动手（图书馆·上午）**
- [ ] 用**数组**实现栈（不从昨天的链表版抄）——push/pop/peek/isEmpty
- [ ] 用括号匹配检验：`({[]})`✅ `({[}])`❌。遍历字符串，左括号入栈，右括号看栈顶是否匹配
- [ ] 用**循环数组**实现队列——enqueue/dequeue/isEmpty/isFull

**🧪 验证（图书馆·下午）**
- [ ] 括号匹配测 5 组输入
- [ ] 队列：enqueue 到满 → dequeue 到空 → enqueue 到满（验证循环）
- [ ] 不看书，重写一遍栈的 push/pop

**📝 验收**
- ✅ 闭卷写出数组版栈和循环队列

**🔮 扩展**
- 用两个栈实现一个队列
- 实现逆波兰表达式求值（LeetCode 150）

---

### Day 13 · 哈希表

**📖 理论（图书馆·上午）**
- 核心问题：O(1) 查找为什么快？——直接算地址，不遍历
- 哈希函数：输入 key → 输出 0 到 N-1 之间的整数
- 冲突解决：两个 key 算出同一个下标怎么办？——链表法（最简）

**🔧 动手（图书馆·上午）**
- [ ] 定义哈希表：数组 + 每个槽一个链表
  ```c
  typedef struct {
      Node **buckets;  // 每个 bucket 是一个链表的头指针
      int size;        // bucket 数量
  } HashTable;
  ```
- [ ] 哈希函数：`key % size`（最简版）
- [ ] put(key, value)——算出 bucket → 找是否已有 → 有则更新，无则头插
- [ ] get(key)——算出 bucket → 遍历链表 → 找 key → 返回 value
- [ ] delete(key)——算出 bucket → 从链表删除

**🧪 验证（图书馆·下午）**
- [ ] put 100 个 key-value → get 100 个验证 → delete 50 个
- [ ] 用哈希表统计一段文本里每个单词的出现次数
- [ ] 两个不同的 key 映射到同一个 bucket 时，链表上是不是两个都有？

**📝 验收**
- ✅ 闭卷写出哈希表 put/get/delete
- ✅ 能解释哈希冲突和链地址法

**🔮 扩展**
- 实现哈希表的自动扩容——负载因子 > 0.75 时扩容
- 了解一种更好的哈希函数（如 DJB2 hash）

---

### Day 14 · 缓冲 + 综合考核

**今天不学新东西。**

**📝 闭卷自检**
- [ ] 从零手写：动态数组 push_back、单向链表 insert/delete、双向链表 delete、栈 push/pop、哈希表 put/get
- [ ] 任选一个卡了的，反复写 3 遍

**🔧 迷你项目：电话簿（下午）**
- [ ] 功能：增删查改联系人（姓名 + 电话）
- [ ] 存储：用哈希表或链表
- [ ] 数据持久化：退出时写入文件，启动时从文件加载
- [ ] 命令行交互：`add 张三 13800138000` / `find 张三` / `delete 张三` / `list`

---

## 第 3 周：结构体 + 文件 + 模块化

---

### Day 15 · 结构体 + 字节对齐

**📖 理论（图书馆·上午）**
- 《C和指针》结构体章节
- 核心问题：`sizeof(struct)` 为什么可能大于各字段之和？（字节对齐）
- 核心问题：为什么要对齐？——CPU 读内存的效率

**🔧 动手（图书馆·上午）**
- [ ] 定义 Student（姓名[32]，学号 int，成绩 float[3]）
- [ ] 写函数：计算平均分、按成绩排序、按姓名查找
- [ ] 用不同字段顺序定义结构体，sizeof 确认差异

**🧪 验证（图书馆·下午）**
- [ ] 尝试 `#pragma pack(1)` 关闭对齐，对比 sizeof
- [ ] Student 数组，qsort 按成绩排序

**📝 验收**
- ✅ 能解释什么是字节对齐，为什么存在

**📚 夜读**
- 《C和指针》结构体章节剩余部分

**🔮 扩展**
- 用 offsetof 宏查看某个字段在结构体中的偏移量
- 研究结构体内嵌结构体时的对齐行为

---

### Day 16 · 联合体 + 位操作

**📖 理论（图书馆·上午）**
- union：所有成员共享同一块内存，大小是最大成员的大小
- 用途：节省内存、判断大小端、类型转换（type punning）
- 位操作：安全领域的天天用——flag、权限、TCP 标志位、加密

**🔧 动手（图书馆·上午）**
- [ ] 用 union 判断机器是大端还是小端
- [ ] 用 union 打印浮点数的二进制表示
- [ ] 位操作：设置某位(置 1)、清除某位(置 0)、翻转某位、检查某位
- [ ] 实现权限系统：读(bit0=1)、写(bit1=2)、执行(bit2=4)

**🧪 验证（图书馆·下午）**
- [ ] 打印从 0 到 15 的二进制，验证自己的位操作理解
- [ ] 不用临时变量交换两个整数（异或法）
- [ ] 写一个函数打印任意 32 位整数的二进制形式

**📝 验收**
- ✅ 闭卷写出读权限/写权限的组合判断（位掩码）
- ✅ 能徒手写出一个字节 8 位的值

**📚 夜读**
- 《编码》相关章节回顾：为什么计算机用 0/1

**🔮 扩展**
- 实现 bitmap：用每一位代表一个 bool，节省 8 倍内存
- 用位操作实现一个简单的 Base64 编码器

---

### Day 17 · 文件 I/O

**📖 理论（图书馆·上午）**
- C 的文件操作：fopen/fclose/fread/fwrite/fseek/ftell
- "r"/"w"/"a" vs "rb"/"wb"/"ab" —— 文本模式 vs 二进制模式
- 为什么二进制模式重要？（Windows 上 \r\n 会被转换）

**🔧 动手（图书馆·上午）**
- [ ] 文件拷贝：分块读（一次 4096 字节），支持大文件
- [ ] 统计一个文本文件的行数、单词数、字符数（仿 wc 命令）
- [ ] hexdump：以 16 进制 + ASCII 打印文件内容

**🧪 验证（图书馆·下午）**
- [ ] 用 hexdump 查看自己写的 .c 文件
- [ ] 用 hexdump 对比文本模式写的文件和二进制模式写的文件（在 Windows 上尤其明显）

**📝 验收**
- ✅ 闭卷写出 fopen/fclose/fread/fwrite 的常规用法
- ✅ hexdump 工具能正确运行

**🔮 扩展**
- 实现简单的文件加密：每个字节 XOR 一个 key，再跑一次恢复
- 实现 tail 命令：打印文件最后 N 行

---

### Day 18 · 模块化编程 + Makefile

**📖 理论（图书馆·上午）**
- `.h` = 接口（声明），`.c` = 实现 —— 分离的意义
- include guard：`#ifndef XXX_H / #define XXX_H` 防止重复包含
- static 函数：只在当前文件可见，对外隐藏实现细节
- Makefile：不必每次都手写 gcc 命令

**🔧 动手（图书馆·上午）**
- [ ] 把链表、哈希表、动态数组各拆成 **.h + .c**
- [ ] 每个头文件加 include guard
- [ ] 内部辅助函数加 static
- [ ] 写 Makefile，支持 `make`（编译）、`make clean`（清理）

**🧪 验证（图书馆·下午）**
- [ ] 写一个 main.c 同时用链表和哈希表——验证多模块编译
- [ ] 执行 `make clean && make` 确认一切正常
- [ ] 故意写两个同名全局变量，感受"multiple definition"链接错误

**📝 验收**
- ✅ 能从零搭一个多文件项目：创建 .h + .c + Makefile
- ✅ 会排查 "undefined reference" 和 "multiple definition"

**🔮 扩展**
- 了解 CMake 的基本用法（`CMakeLists.txt`）
- 试试 gcc 的 `-I`（头文件路径）和 `-L`（库路径）选项

---

### Day 19-20 · 阶段项目：命令行通讯录

**这是第一阶段的综合大作业。两天时间，做完整。**

**📖 需求**
```
功能：
- add   添加联系人（姓名、电话、邮箱）
- find  按姓名查找
- delete 删除联系人
- list   列出所有联系人（支持按姓名排序）
- save   保存到文件
- load   从文件加载

模块划分：
- contact.h/c  —— 联系人数据结构 + 增删查改
- storage.h/c  —— 文件读写
- ui.h/c       —— 命令行交互解析
- main.c       —— 主入口
- Makefile
```

**Day 19的重点**：搭架构 + 数据层
- [ ] 定义 Contact 结构体
- [ ] 用链表存储（可以复用之前写的链表模块）
- [ ] 实现增删查改 + 排序

**Day 20 的重点**：持久化 + UI + 收尾
- [ ] 保存为 CSV 或 JSON（简单格式即可）
- [ ] 启动时自动加载
- [ ] 完整的命令行交互
- [ ] 用 `-fsanitize=address` 检查内存
- [ ] push 到 GitHub，README 写好

**📝 验收**
- ✅ add 10 → list → delete 3 → find → save → 重新启动 → list 验证 7 个还在
- ✅ 没有内存泄漏

---

### Day 21 · 缓冲

- [ ] 回顾这一周的代码
- [ ] 不熟的重新写
- [ ] 休息
- [ ] 如果通讯录项目还有 bug，今天修完

---

## 第 4 周：GDB + 宏 + 进阶系统调用

---

### Day 22 · 宏 + 预处理

**📖 理论（图书馆·上午）**
- `#define` 不仅是常量，还能写函数宏
- 宏的坑：多重求值（`MAX(i++, j++)` 会自增两次）
- `#ifdef / #ifndef` 条件编译的用途
- `__FILE__` / `__LINE__` / `__func__`——调试日志三件套

**🔧 动手（图书馆·上午）**
- [ ] 写 MAX/MIN 宏，测试 MAX(i++, j++) 的问题
- [ ] 写一个 DEBUG_LOG 宏：`DEBUG_LOG("x = %d", x)`，仅在 `#ifdef DEBUG` 时打印
- [ ] 用 `__FILE__` 和 `__LINE__` 做 assert 宏的极简版

**🧪 验证（图书馆·下午）**
- [ ] 观察：`gcc -E your_file.c` 预处理后的代码——宏展开的样子
- [ ] 对比有 #ifdef 和没 #ifdef 时编译出的程序大小

**📝 验收**
- ✅ 能解释宏和函数的区别（编译时展开 vs 运行时调用）
- ✅ 能写出带条件编译的调试日志宏

**🔮 扩展**
- 了解 `do { ... } while(0)` 在宏中的用法（为什么这么写？）
- 了解 `#`（字符串化）和 `##`（连接）运算符

---

### Day 23 · GDB 精通（上）

**📖 理论（图书馆·上午）**
- GDB 不是只能看 segfault——它是最强大的 C 语言学习工具
- 今天只学 GDB 的各种命令，不用学新概念

**🔧 动手（图书馆·上午）**
- [ ] 拿通讯录程序的代码当调试目标
- [ ] 学会以下 GDB 操作（边做边记）：
  - `break 文件名:行号`——在指定行下断点
  - `break 函数名`——在函数入口下断点
  - `condition 1 x == 5`——条件断点（变量等于某个值才停）
  - `watch 变量名`——变量值变了就停
  - `next`（逐过程）/ `step`（逐语句）/ `finish`（执行到当前函数返回）
  - `print 表达式`——打印变量
  - `display 变量`——每步自动打印
  - `backtrace` / `bt full`——查看完整调用栈

**🧪 验证（图书馆·下午）**
- [ ] 在链表插入函数设断点，单步跟踪指针修改
- [ ] 用 watch 监视一个节点的指针，看它什么时候被改的
- [ ] 写一个递归函数（阶乘），单步跟踪，观察每次递归调用栈帧的变化

**📝 验收**
- ✅ 用 GDB 单步跟踪找到通讯录的一个 bug（或者证明没有 bug）

**📚 夜读**
- GDB 官方手册的前 10 页——Command Summary 部分

**🔮 扩展**
- 了解 GDB 的 TUI 模式（`gdb -tui`）——图形化界面
- 了解 pwndbg 插件（CTF 常用）——`pip install pwndbg`

---

### Day 24 · GDB 精通（下）+ Core Dump

**📖 理论（图书馆·上午）**
- Core dump：程序崩溃时的内存快照——可以事后分析
- `ulimit -c unlimited`——开启 core dump
- 程序死了但没 core 文件？检查 ulimit

**🔧 动手（图书馆·上午）**
- [ ] 故意写几个会崩溃的程序：空指针解引用、double free、栈溢出
- [ ] 每种崩溃都用 core dump + GDB 分析：
  - `gdb 程序名 core文件`
  - `bt full` 看崩溃时的调用栈
  - `info locals` 看局部变量
  - `x/Nx $rsp` 看栈内存

**🧪 验证（图书馆·下午）**
- [ ] 写一个故意 segfault 的程序，从 core dump 找出是第几行、什么变量导致的
- [ ] 对比有调试符号（`-g`）和没有时的 GDB 输出差距

**📝 验收**
- ✅ 能从一个 core dump 文件定位到崩溃的代码行和变量值
- ✅ 不用 printf 调试，用 GDB

**🔮 扩展**
- 了解 GDB 的 `script` 功能：把常用命令写成脚本，自动运行
- 在 `.gdbinit` 里配一些常用设置

---

### Day 25-26 · 自己写一个内存分配器

**这两天一起看——这是 C 语言的"毕业项目"。做不出来不代表你不行，做出来了你就是极少数。**

**📖 理论（Day 25 上午）**
- malloc 的原理：维护一个空闲块链表，找到够大的就切一块给你
- first-fit：找第一个够大的
- free 之后要合并相邻的空闲块（coalescing）
- 用 sbrk 向操作系统要更多内存

**🔧 动手（Day 25）**
- [ ] 定义 block 结构体：size + is_free + next
- [ ] `void *my_malloc(size_t size)`：遍历空闲链表 → 找到够大的 → 切下来
- [ ] 先用 sbrk 或 mmap 获取初始内存池
- [ ] 返回的指针指向数据区（跳过 block header）

**🧪 验证（Day 26）**
- [ ] 用 my_malloc 替换 malloc，跑通讯录程序
- [ ] 写测试：分配 10 个不同大小的 block → free 其中 5 个 → 再分配 → 验证数据
- [ ] 如果没做出来——就分析 glibc malloc 为什么这么复杂（bin 分类、fastbin、mmap 阈值）
- [ ] 把尝试过程写进笔记——"我自己写了个内存分配器，遇到了什么问题"

**📝 验收**
- ✅ my_malloc + my_free 通过了简单测试（分配→写数据→free→再分配→数据正确）
- 如果没做出来也 OK——你理解了 malloc 的内部原理，这已经够了

---

### Day 27 · CSAPP 汇编初体验

**📖 理论（图书馆·上午）**
- 读《CSAPP》第 3 章 3.1-3.4（到数据格式部分）
- `gcc -S hello.c` 生成汇编代码
- 认识：mov, add, sub, push, pop, call, ret, cmp, jmp

**🔧 动手（图书馆·上午）**
- [ ] 写一个最简单的 C 函数（两个 int 参数，返回它们的和）
- [ ] 用 `gcc -S -O0` 生成汇编（-O0 关闭优化，汇编和 C 一一对应）
- [ ] 逐行读汇编：参数怎么传进来的？怎么加的？怎么返回的？

**🧪 验证（图书馆·下午）**
- [ ] 用 GDB 在函数入口设断点，`layout asm` 看汇编窗口，单步执行
- [ ] 观察 rax、rdi、rsi 寄存器的变化
- [ ] 写一个调用了另一个函数的函数，看 call/ret 是如何工作的

**📝 验收**
- ✅ 能看懂一个简单 C 函数（无循环）对应的汇编

---

### Day 28 · 缓冲 + 《编码》

- [ ] 休息 + 补本周没完成的内容
- [ ] 接着读《编码》——纯享受，不写代码
- [ ] 整理本周的代码 push GitHub

---

# 第二阶段：理解程序怎么跑（Day 29-42）

---

### Day 29-30 · 栈帧 + 函数调用机制

**📖 理论（Day 29 上午）**
- CSAPP 第 3 章 3.6-3.7（控制 + 过程调用）
- 核心认知：`call` = push rip（返回地址）+ jmp 目标地址
- 核心认知：`ret` = pop rip
- 栈帧布局（从高到低）：调用者 rbp → 返回地址 → 本函数 rbp → 局部变量 → 可能溢出区

**🔧 动手（Day 29）**
- [ ] 写一个函数，里面有局部变量（包括一个 char buf[32]）
- [ ] 用 GDB 单步跟踪整个调用→执行→返回的过程
- [ ] 在每一步打印：rsp、rbp、rip 的值
- [ ] 用 `x/40x $rsp` 查看栈上的原始数据
- [ ] 在纸上画出栈帧图：每个格子标清楚放的是什么

**🧪 验证（Day 30）**
- [ ] 写递归阶乘函数，GDB 观察每次递归调用栈帧的变化
- [ ] 画图：递归 n=3 时，栈上长什么样？返回时怎么一层层弹出？
- [ ] 理解了：为什么递归太深会栈溢出（stack overflow）——栈空间有限

**📝 验收**
- ✅ 能在白纸上画出任意函数的栈帧结构图
- ✅ 能在 GDB 中定位到返回地址在栈上的位置

**📚 夜读**
- CSAPP 第 3 章 3.8-3.10（数组 / 结构体 / 浮点）

**🔮 扩展**
- 用 GDB 查看一个调用了 printf 的函数——参数怎么传的？
- 对比 64 位（寄存器传参）和 32 位（栈传参）的区别——知道即可

---

### Day 31-32 · 编译链接全流程

**📖 理论（Day 31 上午）**
- CSAPP 第 7 章 7.1-7.7
- 预处理 → 编译 → 汇编 → 链接——每一步的输入和输出

**🔧 动手（Day 31）**
- [ ] 拿一个多文件项目，手动分步执行：
  - `gcc -E` → 预处理后的 .i 文件（看宏展开）
  - `gcc -S` → 汇编 .s 文件（看机器指令）
  - `gcc -c` → 目标 .o 文件（不可读的机器码）
  - `gcc *.o` → 最终可执行文件
- [ ] 用 nm 看 .o 文件里的符号表——哪些是定义的（T），哪些是未定义的（U）
- [ ] 用 objdump -d 反汇编 .o 文件
- [ ] 用 readelf -S 看 ELF 文件的段（section）

**🧪 验证（Day 32）**
- [ ] 理解 "undefined reference"——就是某个 .o 需要的符号（U），其他 .o 都没提供（T）
- [ ] 故意制造一个 undefined reference 错误，然后自己排查
- [ ] 写一个使用全局变量的多文件项目，用 nm 追踪符号

**📝 验收**
- ✅ 能用 nm/objdump/readelf 分析 .o 文件
- ✅ 能排查链接时的 symbol 错误

**🔮 扩展**
- 了解 weak symbol（弱符号）——`__attribute__((weak))`
- 研究 .got 和 .plt 表——动态链接的核心

---

### Day 33-34 · 静态库 + 动态库

**📖 理论（Day 33 上午）**
- 静态库 (.a)：编译时嵌入可执行文件——文件大但独立
- 动态库 (.so)：运行时加载——共享内存，但依赖环境

**🔧 动手（Day 33）**
- [ ] 把链表模块打包成 `liblist.a`（用 ar 工具）
- [ ] 另一个程序链接 liblist.a，验证能用
- [ ] 打包成 `liblist.so`
- [ ] 链接 .so，设置 LD_LIBRARY_PATH，运行

**🧪 验证（Day 34）**
- [ ] 对比可执行文件的大小：静态链接 vs 动态链接
- [ ] 修改 .so 代码（不改接口）→ 重新编译 .so → 程序不用重编译就能用新版本
- [ ] 故意删掉 .so → 运行时报错 "cannot open shared object file"

**📝 验收**
- ✅ 能自己打包 .a 和 .so
- ✅ 能排查 "找不到动态库" 的问题

---

### Day 35-36 · 进程 fork/exec

**📖 理论（Day 35 上午）**
- CSAPP 第 8 章 8.2-8.4
- 程序 vs 进程：程序是文件，进程是运行中的实体
- fork() 之后：一个进程变成了两个，父子并发执行
- fork 的返回值：父=子进程PID，子=0

**🔧 动手（Day 35）**
- [ ] `pid_t pid = fork()`——打印 pid，父子各自打印不同的东西
- [ ] 父进程 waitpid 等子进程结束
- [ ] fork 10 次但只 wait 10 次——不要变 fork 炸弹

**🧪 验证（Day 36）**
- [ ] execve：fork 后在子进程里 exec /bin/ls
- [ ] 理解了：shell 就是 fork + exec + waitpid
- [ ] 写一个极简 shell：循环读命令 → fork → exec → wait

**📝 验收**
- ✅ 闭卷写 fork + exec + wait 的组合
- ✅ 能写最简版 shell（至少支持运行外部命令）

**🔮 扩展**
- 给极简 shell 加上管道（|）——需要 pipe() + dup2()
- 理解 daemon 进程——fork 两次脱离终端

---

### Day 37-38 · 信号

**📖 理论（Day 37 上午）**
- CSAPP 第 8 章 8.5
- 信号不是错误——是通知机制
- SIGINT(Ctrl+C)、SIGSEGV(段错误)、SIGKILL(杀进程)、SIGCHLD(子进程结束)

**🔧 动手（Day 37）**
- [ ] 捕获 SIGINT：signal + sigaction 两种方式
- [ ] 捕获 SIGSEGV：打印出错的地址，然后退出
- [ ] SIGCHLD：父进程收到子进程结束的通知，自动回收

**🧪 验证（Day 38）**
- [ ] 给极简 shell 加上信号处理：Ctrl+C 不退出 shell，只杀掉前台进程
- [ ] 测试：shell 里运行 `sleep 100`，按 Ctrl+C——sleep 被杀了，shell 还在
- [ ] 写程序故意触发 SIGSEGV，signal handler 打印信息后 exit

**📝 验收**
- ✅ 闭卷写出 sigaction 的基本用法
- ✅ shell 的 Ctrl+C 处理正常工作

---

### Day 39-40 · 综合练习：完善 Shell

**这两天把 fork/exec/signal 串起来。**

**🔧 动手**
- [ ] 完善极简 shell：
  - 支持内置命令：cd、exit
  - 支持外部命令
  - Ctrl+C 不退出 shell
  - 后台运行：`command &`（不等子进程结束）
- [ ] push 到 GitHub——这是你第二个拿得出手的项目

**📝 验收**
- ✅ Shell 能稳定运行：3 个内置命令 + 外部命令 + Ctrl+C + 后台运行

---

### Day 41-42 · 缓冲 + CSAPP 选读

- [ ] 复习本周内容
- [ ] CSAPP 第 3 章 + 第 8 章，把当时没看懂的再翻一遍
- [ ] 休息

---

# 第三阶段：网络编程（Day 43-56）

---

### Day 43-44 · 网络基础 + TCP 三次握手

**📖 理论（Day 43 上午）**
- IP：找主机。端口：找程序。TCP：可靠传输
- 三次握手：SYN → SYN+ACK → ACK
- 四次挥手：FIN → ACK → FIN → ACK
- Wireshark：安装，学习过滤器语法

**🔧 动手（Day 43）**
- [ ] 用 Wireshark 抓一次访问百度的包
- [ ] 过滤器：`tcp.port == 80`、`http`、`dns`
- [ ] 标注出三次握手的 3 个包
- [ ] 追踪一次完整的 HTTP 流（Follow TCP Stream）

**🧪 验证（Day 44）**
- [ ] 抓自己的浏览器访问任意网站的包
- [ ] 在笔记里画出三次握手和四次挥手的时序图
- [ ] 用 `netstat -an` 看自己电脑当前的网络连接状态

**📝 验收**
- ✅ 能在 Wireshark 中标注出三次握手
- ✅ 能徒手画出 TCP 三次握手时序图

---

### Day 45-46 · TCP Socket 编程

**📖 理论（Day 45 上午）**
- 服务器：socket → bind → listen → accept → recv/send → close
- 客户端：socket → connect → send/recv → close
- man 手册：`man 2 socket`，`man 7 tcp`

**🔧 动手（Day 45）**
- [ ] echo 服务器：客户端发什么回什么
- [ ] 用 telnet 或 nc 连接测试

**🧪 验证（Day 46）**
- [ ] 把端口扫描器的 Python 版（如果写过）用 C 重写
- [ ] 对 localhost 1-1024 扫描，看哪些端口开着

**📝 验收**
- ✅ 闭卷写 echo 服务器（socket→bind→listen→accept 链路）
- ✅ 端口扫描器能跑

**📚 夜读**
- 《计算机网络：自顶向下》第 2 章应用层（HTTP 部分）

---

### Day 47-48 · 多客户端 + select

**📖 理论（Day 47 上午）**
- 阻塞 I/O vs 非阻塞 I/O
- select()：同时监听多个 fd，谁有数据就处理谁
- fd_set 和 FD_ZERO/FD_SET/FD_ISSET

**🔧 动手（Day 47）**
- [ ] 聊天服务器：多个客户端连接，消息广播给所有人
- [ ] 用 select 实现——不需要多线程

**🧪 验证（Day 48）**
- [ ] 开 3 个 telnet 窗口连上聊天服务器，互相发消息
- [ ] 对比：单线程 select vs 多线程 pthread 的编写感受

**📝 验收**
- ✅ 聊天服务器 3 个客户端同时在线正常通信

---

### Day 49-50 · 端口扫描器 2.0

**📖 理论（Day 49 上午）**
- TCP connect 扫描：完整建立连接 → 检测到→断开
- SYN 扫描：发 SYN → 收 SYN+ACK(开放) / RST(关闭) / 无响应(被过滤)
- 为什么 SYN 扫描需要 root？（raw socket）

**🔧 动手（Day 49-50）**
- [ ] 升级端口扫描器：
  - 支持多线程（pthread）
  - 支持指定 IP + 端口范围
  - 输出：端口号 + 状态（开放/关闭/被过滤）
  - 服务识别：对开放端口发探测，读返回 banner
- [ ] push 到 GitHub，打 tag v2.0

**📝 验收**
- ✅ 多线程端口扫描器，对 localhost 扫描结果正确
- ✅ README 有使用示例和截图

---

### Day 51-52 · HTTP 服务器

**📖 理论（Day 51 上午）**
- HTTP 请求格式：`GET /path HTTP/1.1\r\nHost: xxx\r\n\r\n`
- HTTP 响应格式：`HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html>...`
- 几个关键状态码：200 OK, 301 Moved, 404 Not Found, 500 Internal Server Error

**🔧 动手（Day 51）**
- [ ] 写极简 HTTP 服务器：
  - GET / 返回首页（硬编码 HTML）
  - GET /about 返回 about 页面
  - 其他返回 404

**🧪 验证（Day 52）**
- [ ] 浏览器打开 localhost:8080，看到页面
- [ ] 用 Wireshark 抓浏览器 ↔ 服务器的包，分析 HTTP 协议细节
- [ ] 浏览器打开 localhost:8080/nonexist，看到 404
- [ ] push 到 GitHub

**📝 验收**
- ✅ 浏览器访问 3 个路由正常返回

---

### Day 53-54 · 简易抓包工具

**📖 理论（Day 53 上午）**
- raw socket（AF_PACKET / SOCK_RAW）：直接抓网卡数据
- 以太网帧头：dst_mac(6) + src_mac(6) + ether_type(2)
- IP 头：version+ihl + tos + total_len + ... + src_ip(4) + dst_ip(4)
- TCP 头：src_port(2) + dst_port(2) + seq + ack + flags + ...

**🔧 动手（Day 53-54）**
- [ ] 抓包工具：
  - 打印每个包的 src_mac → dst_mac
  - 打印 src_ip:src_port → dst_ip:dst_port
  - 打印协议类型（TCP/UDP/ICMP）
- [ ] 需要 root 权限
- [ ] 对比 Wireshark 的输出验证

**📝 验收**
- ✅ 抓包工具能正确输出 IP 层信息

---

### Day 55-56 · 缓冲 + GitHub 整理

- [ ] 把端口扫描器、HTTP 服务器、抓包工具 push 到 GitHub
- [ ] 每个项目写好 README
- [ ] 不熟的 Socket API 重新写一遍

---

# 第四阶段：二进制安全入门（Day 57-77）

---

## 第 9 周：栈溢出

---

### Day 57-58 · 第一个栈溢出

**📖 理论（Day 57 上午）**
- 读 CTF Wiki 的栈溢出原理章节
- 核心认知：局部变量（buffer）在栈上，返回地址也在栈上。如果 buffer 写越界了，就能覆盖返回地址
- gets() 是最经典的漏洞函数——没有长度限制
- 现代编译器默认有 canary（金丝雀值），需要 `-fno-stack-protector` 关掉

**🔧 动手（Day 57）**
- [ ] 写漏洞程序：
  ```c
  #include <stdio.h>
  void win() { printf("You win!\n"); }
  void vuln() {
      char buf[64];
      gets(buf);
      printf("Hello, %s\n", buf);
  }
  int main() { vuln(); return 0; }
  ```
- [ ] 正常输入 "AAAA"——程序正常运行
- [ ] 输入 80 个 'A'——segfault！
- [ ] 用 GDB 找到 buf 的起始位置 → 算出来输入多长刚好覆盖到返回地址（偏移量）

**🧪 验证（Day 58）**
- [ ] 构造 payload = 偏移量个 'A' + win 函数的地址
- [ ] 跑程序，输入 payload → 打印 "You win!"
- [ ] **恭喜——你控制了程序的执行流。这是所有二进制安全的起点。**

**📝 验收**
- ✅ 能独立算出偏移量
- ✅ 能覆盖返回地址让程序跳到指定函数

**📚 夜读**
- CTF Wiki：栈溢出原理和 ret2text 章节

**🔮 扩展**
- 试试不同的编译器优化级别（-O0 vs -O2）对栈布局的影响
- 用 checksec 工具检查编译出的程序的保护机制

---

### Day 59-60 · shellcode

**📖 理论（Day 59 上午）**
- shellcode = 一段用来弹 shell 的机器码
- 需要栈可执行（NX 关闭）：`-z execstack`
- pwntools 的 shellcraft：帮你生成 shellcode，不需要自己写

**🔧 动手（Day 59）**
- [ ] 编译时关掉所有保护（没 canary + NX 关 + 无 PIE）
- [ ] 更新漏洞程序：buf 足够大（128 字节），把 shellcode 放在 buf 里
- [ ] 用 GDB 找到 buf 的起始地址（可能需要关掉 ASLR：`echo 0 > /proc/sys/kernel/randomize_va_space`）
- [ ] payload = shellcode + 偏移对齐 + buf 的起始地址

**🧪 验证（Day 60）**
- [ ] pwntools 脚本跑起来，拿到 shell
- [ ] 理解了为什么 NX（栈不可执行）能防 shellcode——栈上的数据不能当作代码执行

**📝 验收**
- ✅ 能独立完成 ret2shellcode 的 exploit
- ✅ 能解释 NX 位的作用

**📚 夜读**
- CTF Wiki：ret2libc 章节（预习）

**🔮 扩展**
- 不用 pwntools 的 shellcraft，手写 execve("/bin/sh") 的汇编，转成机器码
- 了解 msfvenom 生成 shellcode

---

### Day 61-62 · ret2libc

> **这是整个 V4 难度最高的两天。卡住了正常。**

**📖 理论（Day 61 上午）**
- NX 打开了，栈不可执行 → shellcode 废了
- 但 libc 库本身的代码段是可执行的——里面有什么？`system()` 函数！
- 攻击思路：泄露一个 libc 函数的地址 → 算出 libc 的加载基址 → 算出 system 和 "/bin/sh" 的地址 → 覆盖返回地址跳到 system("/bin/sh")

**🔧 动手（Day 61）**
- [ ] 在漏洞程序里，先泄露 puts 函数的实际地址（通过 puts 的 GOT 表）
- [ ] libc 基址 = puts 实际地址 - puts 在 libc 中的偏移
- [ ] system 地址 = libc 基址 + system 在 libc 中的偏移
- [ ] "/bin/sh" 地址 = libc 基址 + "/bin/sh" 字符串在 libc 中的偏移
- [ ] 用 pwntools 写 exploit

**🧪 验证（Day 62）**
- [ ] 64 位注意：system 的参数要通过 rdi 传递 → 需要 `pop rdi; ret` 这个 gadget
- [ ] 用 ROPgadget 找 gadget
- [ ] exploit 跑通，拿到 shell

**📝 验收**
- ✅ 能独立完成 ret2libc 的三步：泄露→算偏移→跳转
- ✅ 能解释 GOT 表和 PLT 表的作用

**📚 夜读**
- CTF Wiki：ROP 章节

**🔮 扩展**
- 做 BUUCTF 上 2 道 ret2libc 的基础题（level2_x64, ciscn_2019_c_1）

---

### Day 63-64 · ROP 入门

**📖 理论（Day 63 上午）**
- ROP = Return-Oriented Programming
- 核心思想：没有 system 函数？不注入代码——用已有的代码片段（gadget）拼出攻击
- gadget = 任何以 `ret` 结尾的指令序列
- 64 位需要控制 rdi/rsi/rdx → 需要对应的 `pop XXX; ret` gadget

**🔧 动手（Day 63）**
- [ ] ROPgadget 找 gadget：`ROPgadget --binary ./vuln`
- [ ] 构造 ROP 链：`pop rdi; ret` + "/bin/sh" 地址 + system 地址
- [ ] 用 pwntools 写 exploit

**🧪 验证（Day 64）**
- [ ] 在 BUUCTF 上做一道 ROP 题
- [ ] 理解 ret2syscall：不调 libc，直接调内核 syscall（execve=59）
- [ ] 找 gadget 设置 rax/rdi/rsi/rdx → 拼出 syscall 链

**📝 验收**
- ✅ 能解释什么是 ROP
- ✅ 能用 ROPgadget 找 gadget

**🔮 扩展**
- 了解 ret2csu（__libc_csu_init 的万能 gadget）

---

### Day 65-66 · 格式化字符串漏洞

**📖 理论（Day 65 上午）**
- `printf(user_input)` 不是 `printf("%s", user_input)`
- `%p` / `%x`：泄露栈上的数据
- `%n`：把已输出的字符数写入参数指向的地址 → **可以写任意地址**

**🔧 动手（Day 65）**
- [ ] 写 demo：`printf("%p.%p.%p.%p")` 看栈上的内容
- [ ] 找到哪个位置是我们自己输入的——用 `AAAA%p.%p.%p.%p.%p` 定位
- [ ] 用 `%n` 改写一个局部变量的值

**🧪 验证（Day 66）**
- [ ] 用格式化字符串改写 GOT 表——把 `printf` 的 GOT 改成 `system`
- [ ] 下一次调 `printf("/bin/sh")` 实际调了 `system("/bin/sh")`
- [ ] 做 BUUCTF 上 2 道格式化字符串的题

**📝 验收**
- ✅ 能解释格式化字符串漏洞的原理
- ✅ 能用 %n 写任意地址

---

### Day 67-69 · BUUCTF 集中刷题

**这 3 天不学新概念，只刷题。把前面学的技巧练成肌肉记忆。**

- [ ] BUUCTF 刷 10-15 道 Pwn 题
- [ ] 类型：ret2text / ret2shellcode / ret2libc / ROP / fmtstr
- [ ] 每题做完了写一句笔记："这题卡在哪？学到了什么？"

**📝 验收**
- ✅ 看到一道 ret2text 题不用看题解就能做

---

### Day 70-72 · 堆入门（选做 + 概念了解）

**保守目标**：知道堆漏洞是什么，做好笔记。大学再深入。

**📖 理论（Day 70）**
- ptmalloc 的基本数据结构：chunk、bin、fastbin
- use-after-free：free 之后还保留着指针，继续使用
- double free：同一块内存 free 两次

**🔧 动手（Day 70-71）**
- [ ] 构造 use-after-free 场景——free 后用悬空指针读数据
- [ ] 构造 double free——观察崩溃
- [ ] 画 chunk 结构图

**📝 验收**
- ✅ 能解释 use-after-free 和 double free
- ✅ 知道堆漏洞的存在——大学专业课再深学

---

### Day 73-76 · 迷你网络 IDS（安全产品）

**这是你暑假的旗舰项目。用到前面学的一切。**

**📖 需求规格**
```
功能：
✅ 实时抓包（raw socket）
✅ 解析 IP 头 + TCP/UDP 头
✅ 检测规则：
   1. SYN flood：5 秒内同目标收 SYN > 100 → 告警
   2. 端口扫描：10 秒内同源 IP 连 > 20 端口 → 告警
   3. HTTP 攻击：URL 里含 SQL 注入关键字符 → 告警
✅ 输出：终端彩色告警 + 写日志文件
✅ 规则写在 JSON 配置文件里

不做：
- 不做守护进程
- 不做 GUI
- 不做 IPv6
- 不做深度包检测（DPI）
```

**Day 73**：搭框架——capture.c / parser.c / detect.c / alert.c / main.c
**Day 74**：抓包 + 解析（AH_PACKET → ETH → IP → TCP）
**Day 75**：实现 3 条检测规则
**Day 76**：测试 + 修 bug + push GitHub + 写 README

**📝 验收**
- ✅ SYN flood 攻击能检测到（用 hping3 模拟攻击）
- ✅ 端口扫描能检测到（用 nmap 扫自己）
- ✅ HTTP SQL 注入能检测到（curl 带注入 payload 的 URL）

---

### Day 77 · 缓冲

---

# 第五阶段：收尾（Day 78-90）

---

### Day 78-80 · 密码学快速了解

**📖 理论（Day 78）**
- 哈希（SHA-256）：单向、定长、抗碰撞
- 对称加密（AES）：加密和解密用同一个密钥
- 非对称加密（RSA）：公钥加密、私钥解密
- 数字签名：私钥签名、公钥验证

**🔧 动手（Day 78-79）**
- [ ] 读 SHA-256 的 RFC 文档
- [ ] 用 C 实现极简版 SHA-256——至少消息填充和压缩函数
- [ ] 测试：SHA256("hello world") 结果和 sha256sum 命令一致

**🧪 验证（Day 80）**
- [ ] 用 OpenSSL 生成 RSA 密钥对
- [ ] 用私钥签名一个文件，公钥验证
- [ ] 理解：HTTPS 的证书链就是这个原理

**📝 验收**
- ✅ SHA-256 实现跑对
- ✅ 能解释哈希/对称/非对称/签名的区别

---

### Day 81-83 · GitHub 全面整理

- [ ] 每个项目写完整 README：简介、编译方法、使用示例、截图、技术栈
- [ ] 整理 commit 历史（squash 无意义的 commit）
- [ ] GitHub 个人主页写介绍："Security Engineer / Binary Security / C"
- [ ] 项目列表：IDS + 端口扫描器 + HTTP 服务器 + Shell + 通讯录 + SHA-256 + 动态数组 + 哈希表库

---

### Day 84-85 · 写 3 篇博客

- [ ] (1) "从 C 指针到栈溢出——我的二进制安全入门之路"
- [ ] (2) "用 C 写一个网络入侵检测工具——实战记录"
- [ ] (3) "90 天暑假技术成长总结"
- [ ] 发布：知乎 + CSDN

---

### Day 86-87 · 写简历

- [ ] 一页纸简历：
  - 技能：C, GDB, x86-64 汇编, pwntools, Linux 系统编程, Socket 编程
  - 项目：IDS（旗舰） + 端口扫描器 + HTTP 服务器 + Shell + 通讯录
  - 安全：BUUCTF Pwn 15 题 + 栈溢出/ret2libc/ROP/fmtstr
  - 博客：3 篇技术文章

---

### Day 88-90 · 画知识图谱 + 大学准备 + 庆祝

- [ ] 画三张知识图谱：
  - 计算机系统知识图谱（C → 汇编 → 内存 → 进程 → 信号）
  - 网络知识图谱（TCP/IP → Socket → 抓包 → HTTP）
  - 安全知识图谱（栈溢出 → shellcode → ret2libc → ROP → fmtstr）
- [ ] 搜学校 CTF 战队——加入
- [ ] 列大一上学期目标（最多 3 个）
- [ ] **庆祝。你做到了。**

---

# 📊 最终产出

| 产出 | 数量 |
|------|------|
| GitHub 项目 | 6+ 个（IDS + 端口扫描器 + HTTP 服务器 + Shell + 通讯录 + SHA-256） |
| 技术博客 | 3 篇 |
| C 语言 | 指针 → 动态内存 → 数据结构 → 网络 → 系统调用，全通路 |
| 二进制安全 | 栈溢出/ret2libc/ROP/fmtstr 能独立利用 |
| 网络编程 | Socket 客户端/服务器 + 抓包 + 协议分析 |
| Pwn 刷题 | BUUCTF 15+ |

---

# ⚠️ 三条铁律

1. **每写完一个能跑的程序就 push GitHub**。哪怕 50 行。绿点日历持续亮着是最好的动力。
2. **卡了 2 小时就跳过**，标记"卡在哪"，继续下一个任务。回头啃比当场死磕效率高。
3. **每周休息一天**。学习效果和投入时间不是线性的。

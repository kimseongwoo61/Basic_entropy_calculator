# **Basic Entropy Calculator**

Malware Packing Analysis Pycommend - Version: 0.1.0

## **1. What is Basic Entropy Calculator?**

In conjunction with Immunity Debugger, Basic Entropy Calculator allows you to calculate the entropy value of a binary during execution and visualize it as a graph. Currently, memory addresses are hard-coded and unstable; we plan to apply PE header information-based address range recognition and stability codes in future updates.

## **2. How to Use!!!**

### **1) Download the Uploaded File.**

```bash
bashCopy code
git clone https://github.com/kimseongwoo61/Basic_entropy_calculator.git
# If you haven't installed Immunity Debugger, please install it.
# Immunity Install Link: [Immunity Debugger](https://www.immunityinc.com/products/debugger/)
```

### **2) Copy `checkep.py` File to Immunity Debugger Plugin Folder.**

Copy **`checkep.py`** to **`(Immunity Installation Path)/Immunity Debugger/PyCommands`**. In general, the installation path of Immunity is **`Program Files (x86)/Immunity Inc`**. If the installation path is modified, please adjust accordingly.

### **3) Open Immunity Debugger & Insert the Executable File and Execute the Analysis Command.**

Enter the Python command in the white window at the bottom of the debugger screen as follows and press Enter to measure the running memory entropy.

```bash
bashCopy code
!checkep

```

### **4) When the Task is Complete, Run `view_entropy.py`.**

If the entropy value is measured successfully, a file called **`record_entropy.txt`** will be generated on your computer desktop. **`view_entropy.py`** reads this file and graphs the result.

## **Warning!!!**

This Python command file is still in beta and is very unstable. Also, depending on the file size, it can take a considerable amount of time to extract data. To be updated!!!

## **For More Information**

- Blog (Mobile): [Blog - Naver](https://blog.naver.com/pl2105/222636615915)
- Blog (PC): [Blog - Tistory](https://icmp-ycdi.tistory.com/152)

Good afternoon, good evening, and good night!

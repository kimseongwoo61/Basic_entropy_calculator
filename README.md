# Basic_entropy_calculator  
malware packing analysis Pycommend - version : 0.1.0  
  
  
## 1. What is Basic_entropy_calculator?
In conjunction with the immunity debugger, you can calculate the entropy value of the binary during execution and visualize it as a graph.  
Currently, memory addresses are hard-coded and unstable, so we will apply PE header information-based address range recognition and operation stabilization codes later.  

## 2. HOW TO USE!!!
### 1) Download the uploaded file. 
<pre><code>git clone https://github.com/kimseongwoo61/Basic_entropy_calculator.git
# If you didn't install immunity, please install it.
# immunity install link : https://www.immunityinc.com/products/debugger/
</code></pre>  

  
### 2) copy checkep.py file to immunity debugger plugin folder.  
copy checkep.py to (immunity installation path)/Immunity Debugger/PyCommands.  
In general, the installation path of immunity is  Program Files (x86)/Immunity Inc  
If the installation path is modified, please put it according to the path.  

### 3) open immunity dbg & Insert the executable file and execute the analysis command.
Enter the Python command, a white window at the bottom of the debugger screen,  
as follows, and press Enter to measure the running memory entropy.  
<pre><code>!checkep</pre></code>

### 4) When the task is complete, run view_entropy.py.
If the entropy value is measured luckily, a file called record_entropy.txt will be generated on your computer desktop.  
view_entropy.py reads this and graphizes the result.  

## Warning!!!
This Python command file is still a beta version and is very unstable.  
Also, depending on the size of the file, it can take a considerable amount of time to extract data!!  
  
  
to be updated!!!  
  
## For More Information
- Blog(for mobile) : https://blog.naver.com/pl2105/222636615915
- Blog(for PC) : https://icmp-ycdi.tistory.com/152
  
  
good afternoon, good evening, and good night!

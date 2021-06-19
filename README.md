# chia-plot-copy
用于自动转存产生好的chia plot文件  
chia-plot-copy.exe 和 SSD2HDD.txt要放同一个文件夹下。  
绘图工具缓存目录和最终目录都设成固态硬盘，同个地方。这样就能秒结束了。

## 文件介绍
### 源码：chia-plot-copy.py
  python代码，没有加注释，只实现基础功能，后续可能会更新。
### 目录文件：SSD2HDD.txt
  用来存放默认存储地址  
  SSD地址为plot【生成】的地方，一般就是官方推荐的SSD（固态）硬盘位置  
  HDD地址为plot【存储】的地方，一般就是官方推荐的HDD（机械）硬盘位置  
  
  默认文件中有示范：  
  SSD  
  L:\  
  E:\  

  HDD  
  F:\Hoop  
  K:\Hoop  
  D:\Hoop  
  
  注：回车区分，我没有写特殊情况的判断，最好直接复制系统文件栏地址  
  
### exe文件：chia-plot-copy.exe
  如果在SSD2HDD.txt中已经把地址全部写好了，遇到要求输入地址的地方，直接回车跳过就行。  
  不看源码的可以拿去直接用


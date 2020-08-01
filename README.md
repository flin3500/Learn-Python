Python Learning
=================

   * [Introduction](#introduction)
   * [02 Object Oriented Programming(OOP)</br>](#02-object-oriented-programmingoop)
            * [2.1 OOP basic grammer](#21-oop-basic-grammer)</br>
            * [2.2 Encapsulation (One feature of OOP)</br>](#22-encapsulation-one-feature-of-oop)
            * [2.3 Inheritance (One feature of OOP)</br>](#23-inheritance-one-feature-of-oop)
            * [2.4 Multiple inheritance</br>](#24-multiple-inheritance)
            * [2.5 Polymorphism (One feature of OOP)</br>](#25-polymorphism-one-feature-of-oop)
            * [2.6 Class Attributes](#26-class-attributes)</br>
            * [2.7 Class Methods](#27-class-methods)</br>
            * [2.8 Singleton Pattern (One of design Pattern)</br>](#28-singleton-pattern-one-of-design-pattern)
            * [2.9 Errors and Exception</br>](#29-errors-and-exception)
            * [2.10 Module</br>](#210-module)
   * [01 Procedure Oriented](#01-procedure-oriented)</br>
            * [1.1 Basic</br>](#11-basic)
            * [1.2 Branch</br>](#12-branch)
            * [1.3 Loop</br>](#13-loop)
            * [1.4 Function</br>](#14-function)
            * [1.5 Module</br>](#15-module)
            * [1.6 List and Tuple</br>](#16-list-and-tuple)
            * [1.7 Dictionary</br>](#17-dictionary)
            * [1.8 String</br>](#18-string)
            * [1.9 For</br>](#19-for)
            * [1.10 [Project] Name Card System](#110-project-name-card-system)

# Introduction

This is the repository contains the code and difficulties I face when I learn python.

# 04 Multitasking

In this folder, it talk about multiytasking.

1. Parallel programming and Concurrent programming
   * Parallel programming: executing simultaneously
   * Concurrent programming: in progress at the same time

### 4.1 Thread

1. Threads are not in order, everyone can be the first  *(LN_01)*

2. Use thread to do a multitasking  *(LN_02)*

3. show the current threads  *(LN_03)*

   ```threading.enumerate()```

4. Threads share global variables  *(LN_04)*

5. Threads share global variables in arguments  *(LN_05)*

6. Threads share global variables sometimes will cause error  *(LN_06)*

   Because sometimes one thread still do not finish their works, but the cpu just swich to another thread.

7. How to fix the error in multitasking(thread) by using mutex *(LN_07)*

8. Know about mutex deadlock

9. [Project] UDP multitasking chatting program by thread  *(LN_08)*

### 4.2 Process

1. The different of program and process is that process is active and can use the hardware on the labtop, but the program is static

2. Use process to do a multitasking  *(LN_01)*

3. The difference of threads and processes

   * thread depends on process

   * process allocates memory, threads are working in this  memory

     eg. Process is a production line in a factory and threads are the workers working in that production line. Once the tasks is too much for one production line. the second production line(process) will be create and more workers(threads) will be hired.

4. Get pid of thread   *(LN_02)*

5. Processes are not in order  *(LN_03)*

6. Pass args to process  *(LN_04)* 

7. Processes are independent with each other, do not share global variable *(LN_05)*

8. Use queue to share between processes  *(LN_06)*

   **Mac python3.0 by default uses "spawn" instead of "fork" when start, need to add   ```multiprocessing.set_start_method("fork")``` at the start of main** from https://stackoverflow.com/questions/60518386/error-with-module-multiprocessing-under-python3-8

9. Processing Pool  *(LN_07)*

10. Process states

    <div align=center>
       <img src="./image/process_states.png" width="50%" height="50%">
    </div>

### 4.3 Coroutine

# 03 UDP and TCP

In this folder, it talk about UDP and TCP.

### 3.1 UDP

* Server:
  1. Create a udp server socket
  2. bind local information(for client to find it)
  3. receive the data from client (recvfrom()), use a while loop **STUCK here if do not get the data from client**
  4. send the data to the client if client request (sendto())
  5. close the udp server socket
* Client
  1. create a udp client socket
  2. send the request to the server by the server ip and port(sendto())
  3. receive data from server if there is (recvfrom())
  4. close udp client socket

1. udp and tcp can bind a same port (eg. 8080) at the same time
2. udp do not need to get a connect whereas tcp need

### 3.2 TCP

* Server:
  1. Create a tcp server socket(listen socket)
  2. bind local information(for client to find it)
  3. listening for the client
  4. wait for the data and create the client socket to serve client (accept())  **STUCK here if do not get the data from client**
  5. receive the request from the client and do some response
  6. send the data to the client if client request
  7. close the client socket
  8. close the  tcp server socket(listen socket)
* Client
  1. create a tcp client socket
  2. specify the server ip and port
  3. connect server
  4. send the request to the server
  5. receive data from server if there is
  6. close tcp client socket

1. In the example above, the server can serve many clients and also serve multiple times in the same time, need to specify the parameter in the listening method.

   ```tcp_server_socket.listen(128)  ``` in this way the server can serve 128 clients.

2. The server must bind the information for the client to find whereas the client do not need to.

3. listen method can make the server get the information from client

4. Client  socket is used to serve the client

5. if a client use close method, server will know and close the client socket for this client

# 02 Object Oriented Programming(OOP)

In this folder, it talk about all of the python OOP.

### 2.1 OOP basic grammer

* Create first class 🐱  *(LN_01)*
* when create the second 😺 , their addresses are different  *(LN_02)*
* parameter "self" inside method points to the Class itself
* use parameters to specify the attribute of an object  *(LN_04)*
* \_\_init\_\_, When the object made, init autoly run  *(LN_03)*
* \_\_del\_\_, When object go, del autoly run  *(LN_05)*
* \_\_str\_\_, return specified output of print(Object)  *(LN_06)*



### 2.2 Encapsulation (One feature of OOP)

* Two objects do not affect each other  *(LN_01, LN_02)*
* The attribute of an object can be another object  *(LN_03)*
* Python do not have real private, we can add "object.\_class\_\_attr" or "object.\_class\_\_method()" to get the private method and attr **NOT RECOMMEND**  *(LN_04)*



### 2.3 Inheritance (One feature of OOP)

* Child  class and Grandchild class can inherit all method from Father class  *(LN_01)*
* When the method of father is not good enough , overide that  *(LN_01)*
* Use super() to get the method of father class  *(LN_01)*
* Use father.method(self) **Python 2.x Not recommend**  *(LN_01)*
* Child can not get the private attr and private method of its father  *(LN_02)*
* Child can get the private attr and private method by the public method of its father  *(LN_03)*



### 2.4 Multiple inheritance

* Child class can inherit all Methods and all attrs of its all fathers  *(LN_01)*
* If fathers have the same method, avoid inheritance  *(LN_01)*
* **Object.\_\_mro\_\_** can show method resolution order in python  *(LN_02)*
* **Python 3.x inherit from object class automatically**, whereas Python 2.x not and need to specify object as father class. Recommend specify object as father class in order to adapt both 2.x and 3.x  *(LN_02)*



### 2.5 Polymorphism (One feature of OOP)

* Different child class call the same method of father class, the outcome is differernt. *(LN_01)*
* **This is based on inherit and overide the father class**



### 2.6 Class Attributes

* An **instance** is an object in memory, made by class
* Every **instance** has its own memory and have different instance attribute
* Every **Class** only be created once in memory 
* Every **Method inside class** only be create once in memory. The objects create by same class share memory of the method. 
* **Class is also an object, so it also has class attributes and class method** *(LN_01)*
* Can use object to get father class attribute from **grandchild -> father -> grandparent -> ... -> Object         Not recommend**  *(LN_02)*
* If want to use child.dadattr = to set an attr, this only add a new attr to the grandchild, can not change the attr of  its dad. So not recommend for the previous one  *(LN_03)*



### 2.7 Class Methods

* There are three method, instance method, class method and static method
* Class method example, need @classmethod *(LN_01)*
* Static method example, need @staticmethid, do not need instance just class.staticmethod()  *(LN_02)*
* Combine class attributes and class method *(LN_03)*



### 2.8 Singleton Pattern (One of design Pattern)

* \_\_new__ method is used to allocate address for object, and need to return object to \_\_init__  *(LN_01)*
* Can change \__new__ method in order to satisfy Singleton Pattern  *(LN_02)*
* Can change \__init__ method in order to make init only execute once  *(LN_03)*



### 2.9 Errors and Exception

* Use try except to get the error  *(LN_01)*
* Use different except to get different error  *(LN_02)*
* Use "except Exception as result"  to get unknown error  *(LN_03)*
* The code inside else will occur when no error, the code inside finally will always occur  *(LN_04)*
* Exception pass can let us only try except in the main, to make us easy  *(LN_05)*
* Can use Exception class to make a user-define exception *(LN_06)*



### 2.10 Module

* Review import module *(LN_01, LN_02, LN_03)*
* can use "import xxxx as xx" to give the module a alias *(LN_01)*
* can use "from xxxx inport xx" to specify the Function or class which want to import   *(LN_04)*
* If import same function from different module, the last one will be valid. Or use as to avoid this conflict  *(LN_05)*
* can use "from xxxx inport \*" to import all from module **Not recommend**  *(LN_06)*
* The order import module **local folder -> system folder**, use random\__file__ to see the absolute path of that module  *(LN_07)*
* Make sure every file is able to import
* \_\_name__ == "\_\_main\_\_" is used to test. when others inport, the code inside main will not execute **Very Recommend**  *(LN_08, LN_09)*
* How to create package: two ways *(LN_10_package)*
* We must specify the module we want to let outside import inthe init.py file  *(LN_10_package, LN_10_import_package)*
* Use setup if we want to share our module to other developers

### 2.11 Read and write

* Read file *(LN_01)*
* When call read(), the read pointer will go to the end of file   *(LN_02)*

| Para | Description                                                  |
| :--: | :----------------------------------------------------------- |
|  r   | Read Only, read pointer will be at beginning, this is the **default** way. If the file not exist, throw exception |
|  w   | Write Only. If file exists, overwrite that. If file not exists, make a new one. |
|  a   | Append Only. If the file exists, the pointer will at the end of the file. If file not exists, make a new one. |
|  r+  | Read and write, read pointer will be at beginning. If the file not exist, throw exception |
|  w+  | Read and write. If file exists, overwrite that. If file not exists, make a new one. |
|  a+  | Read and write. If the file exists, the pointer will at the end of the file. If file not exists, make a new one. |

* When call readline(), only the first line will be read.  *(LN_05)*
* Copy small: Read a file and write it to a new file.  *(LN_06)*
* Copy large: Readline a file and write it to a new file.  *(LN_07)*

### 2.12 Manipulate folder and file (OS)

* Manipulate file

| 01   | rename | Rename file | `os.rename(origin filename, target filename)` |
| ---- | ------ | ----------- | --------------------------------------------- |
| 02   | remove | delete file | `os.remove(filename)`                         |

* Manipulate folder

| 01   | listdir    | list dir                 | `os.listdir(folder name)`      |
| ---- | ---------- | ------------------------ | ------------------------------ |
| 02   | mkdir      | Create dir               | `os.mkdir(folder name)`        |
| 03   | rmdir      | delete dir               | `os.rmdir(folder name)`        |
| 04   | getcwd     | Current dir              | `os.getcwd()`                  |
| 05   | chdir      | Change dir to target     | `os.chdir(target folder name)` |
| 06   | path.isdir | Jusitify if it is folder | `os.path.isdir(folder name)`   |

<br>

<br>

# 01 Procedure Oriented

In this folder, it talk about all of the python basic.

### 1.1 Basic

* Basic grammer for python.

### 1.2 Branch

* if, elif and else are the keyword for branch.

### 1.3 Loop

* While loop is a type of loop which can run typical code for several time.

### 1.4 Function

* Def is the key word to define a function in python.

### 1.5 Module

* Every .py file is a module and we can use import to use the function of other module.

### 1.6 List and Tuple

* LIst and Tuple are two data type of python
* They are ordered and list can be change and tuple can not
* There are many function for list and only two for tuple which is index and count.

### 1.7 Dictionary

* Dictionary is one data type of python
* It has key and value. Key and value are in pair. Dictionary is inordered.

### 1.8 String

* String is one data type of python. There are many functions for String.

### 1.9 For

* For each is a typical type of for loop, the code inside the each will occur if the for loop finish without break.

### 1.10 [Project] Name Card System

* This is a Name Card System which can add, show and search the cards.

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

This is the repository I want to write down the code and difficult I face  when I learn python.

# 02 Object Oriented Programming(OOP)

In this file, it talk about all of the python OOP.

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



# 01 Procedure Oriented

In this file, it talk about all of the python basic.

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




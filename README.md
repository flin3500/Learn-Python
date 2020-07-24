# Python Learning

## Introduction

This is the repository I want to write down the code and difficult I face  when I learn python.

## 01 Procedure Oriented

In this file, it talk about all of the python basic.

#### 1.1 Basic

* Basic grammer for python.

#### 1.2 Branch

* if, elif and else are the keyword for branch.

#### 1.3 Loop

* While loop is a type of loop which can run typical code for several time.

#### 1.4 Function

* Def is the key word to define a function in python.

#### 1.5 Module

* Every .py file is a module and we can use import to use the function of other module.

#### 1.6 List and Tuple

* LIst and Tuple are two data type of python
* They are ordered and list can be change and tuple can not
* There are many function for list and only two for tuple which is index and count.

#### 1.7 Dictionary

* Dictionary is one data type of python
* It has key and value. Key and value are in pair. Dictionary is inordered.

#### 1.8 String

* String is one data type of python. There are many functions for String.

#### 1.9 For

* For each is a typical type of for loop, the code inside the each will occur if the for loop finish without break.

#### 1.10 [Project] Name Card System

* This is a Name Card System which can add, show and search the cards.





## 02 Object Oriented Programming(OOP)

In this file, it talk about all of the python OOP.

#### 2.1 OOP basic grammer

* Create first class 🐱  *(LN_01)*
* when create the second 😺 , their addresses are different  *(LN_02)*
* parameter "self" inside method points to the Class itself
* use parameters to specify the attribute of an object  *(LN_04)*
* \_\_init\_\_, When the object made, init autoly run  *(LN_03)*
* \_\_del\_\_, When object go, del autoly run  *(LN_05)*
* \_\_str\_\_, return specified output of print(Object)  *(LN_06)*

#### 2.2 Encapsulation (One feature of OOP)

* Two objects do not affect each other  *(LN_01, LN_02)*
* The attribute of an object can be another object  *(LN_03)*
* Python do not have real private, we can add "object.\_class\_\_attr" or "object.\_class\_\_method()" to get the private method and attr **NOT RECOMMEND**  *(LN_04)*

#### 2.3 Inheritance (One feature of OOP)

* Child  class and Grandchild class can inherit all method from Father class  *(LN_01)*
* When the method of father is not good enough , overide that  *(LN_01)*
* Use super() to get the method of father class  *(LN_01)*
* Use father.method(self) **Python 2.x Not recommend**  *(LN_01)*
* Child can not get the private attr and private method of its father  *(LN_02)*
* Child can get the private attr and private method by the public method of its father  *(LN_03)*

#### 2.4 Multiple inheritance

* Child class can inherit all Methods and all attrs of its all fathers  *(LN_01)*
* If fathers have the same method, avoid inheritance  *(LN_01)*
* **Object.\_\_mro\_\_** can show method resolution order in python  *(LN_02)*
* **Python 3.x inherit from object class automatically**, whereas Python 2.x not and need to specify object as father class. Recommend specify object as father class in order to adapt both 2.x and 3.x  *(LN_02)*

#### 2.5 Polymorphism (One feature of OOP)

* Different child class call the same method of father class, the outcome is differernt. *(LN_01)*
* **This is based on inherit and overide the father class**

#### 2.6 Class Attributes

* An **instance** is an object in memory, made by class
* Every **instance** has its own memory and have different instance attribute
* Every **Class** only be created once in memory 
* Every **Method inside class** only be create once in memory. The objects create by same class share memory of the method. 
* **Class is also an object, so it also has class attributes and class method** *(LN_01)*
* Can use object to get father class attribute from **grandchild -> father -> grandparent -> ... -> Object         Not recommend**  *(LN_02)*
* If want to use child.dadattr = to set an attr, this only add a new attr to the grandchild, can not change the attr of  its dad. So not recommend for the previous one  *(LN_03)*

#### 2.6 Class Methods

* There are three method, instance method, class method and static method
* Class method example, need @classmethod *(LN_01)*
* Static method example, need @staticmethid, do not need instance just class.staticmethod()  *(LN_02)*



 




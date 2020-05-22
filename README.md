# Replace-Excel-Vlookup-with-Python

The VLOOKUP functionality of MS Excel is widely used for searching for attributes' values across different tables/spreadsheets but it can computationally expensive at times if you have large no. of rows in your spreadsheet and your system doesn't have that much compute Power (CPU/RAM).

This concise python script helps you replace the VLOOKUP feature and does the same in a much more efficient and faster manner.

## Installation :
Dependencies needed:
1. pandas
2. numpy
3. xlrd
4. openpyxl

Simply run the command: ***pip install <package name>*** to install the dependencies.
  
 ## Usage:
 Execute the command: ***python python_vlookup.py*** and the details accordingly.
 
 ## Demo:
 Here I have one excel file - ***1.xlsx***. I want to use the column **Code** to be used for matching with other excel file.
 
 ![1](https://user-images.githubusercontent.com/29462447/82623478-e2a95200-9bfd-11ea-86af-06bf73966c9c.png)

Here, I have the other excel file ***2.xlsx***. We will be using the **IDs** column here to match with the column **Code** of **1.xlsx**

![2](https://user-images.githubusercontent.com/29462447/82623492-e6d56f80-9bfd-11ea-9e7b-babd0ea3ba34.png)

Execute the script and enter the details:

![output_code](https://user-images.githubusercontent.com/29462447/82623504-ee951400-9bfd-11ea-8680-24a3182dd49e.png)

An output excel file ***output.xlsx** will be generated with the extracted values as shown here:

![output](https://user-images.githubusercontent.com/29462447/82623511-f359c800-9bfd-11ea-8512-d9c7eadb2871.png)


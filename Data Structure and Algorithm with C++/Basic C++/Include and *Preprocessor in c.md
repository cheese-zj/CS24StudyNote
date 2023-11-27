## Syntax of **#include**:

``` 
#include <>
```

It is mainly used to access **pre-existing system header files** located in the standard system directories.
**#include** <header_file>
While importing a file using angular brackets(<>), the preprocessor uses a predetermined directory path to access the file.

---

```
#include ""
```

This type is mainly used to access any header files of the **user’s program or user-defined files.**

**#include** "user-defined_file"

When using the double quotes(” “), the preprocessor accesses the current directory in which the source “header_file” is located or the standard system directories.

To import the user-defined header file using **#include**, the file should be in a directory path relative to your C source file otherwise, the preprocessor will begin search for it in the standard system directory.

# -> Preprocessor: 

![[Screenshot 2023-11-25 at 4.20.29 pm.png]]

## Preprocessor Directives in C/C++

Preprocessor programs provide preprocessor directives that tell the compiler to preprocess the source code before compiling. All of these preprocessor directives begin with a ‘#’ (hash) symbol. The ‘#’ symbol indicates that whatever statement starts with a ‘#’ will go to the preprocessor program to get executed. We can place these preprocessor directives anywhere in our program.

|Preprocessor Directives|Description|
|---|---|
|**`#define`**|Used to define a macro|
|**`#undef`**|Used to undefine a macro|
|**`#include`**|Used to include a file in the source code program|
|**`#ifdef`**|Used to include a section of code if a certain macro is defined by `#define`|
|**`#ifndef`**|Used to include a section of code if a certain macro is not defined by `#define`|
|**`#if`**|Check for the specified condition|
|**`#else`**|Alternate code that executes when `#if` fails|
|**`#endif`**|Used to mark the end of `#if`, `#ifdef`, and `#ifndef`|

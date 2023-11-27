"Nice try, assembly!"
Being honest ELEC1601 content-wise is a really good unit. But I'm not expanding too much here 
I guess...

## Reference

A reference variable is a "reference" to an existing variable, and it is created with the `&` operator:

```
string food = "Pizza";  // food variable  
string &meal = food;    // reference to food
```

```
string food = "Pizza";  
string &meal = food;  
  
cout << food << "\n";  // Outputs Pizza  
cout << meal << "\n";  // Outputs Pizza
```

### Memory Address

`&` can also be used to get the memory address of a variable; which is the location of where the variable is stored. To access it, use the `&` operator, and the result will represent where the variable is stored:

```
string food = "Pizza";  
  
cout << &food; // Outputs 0x6dfed4
```

---
## Pointers

```
string food = "Pizza"; // A food variable of type string  

cout << food;  // Outputs the value of food (Pizza)  
cout << &food; // Outputs the memory address of food (**0x6dfed4**)
```

Pointer, is a variable that **stores the memory address as its value**.
A pointer variable points to a data type (like `int` or `string`) of the same type, and is created with the `*` operator. The address of the variable you're working with is assigned to the pointer:

```
string food = "Pizza";  // A food variable of type string  
**string* ptr = &food;**    // A pointer variable, with the name ptr, that stores the address of food  
  
// Output the value of food (Pizza)  
cout << food << "\n";  
  
// Output the memory address of food (0x6dfed4)  
cout << &food << "\n";  
  
// Output the memory address of food with the pointer (0x6dfed4)  
cout << ptr << "\n";
```
---
## Dereferencing

You can also use the pointer to get the value of the variable, by using the `*` operator (the **dereference** operator):

```
string food = "Pizza";  // Variable declaration  
**string* ptr = &food;**    // Pointer declaration  
  
// Reference: Output the memory address of food with the pointer (0x6dfed4)  
cout << ptr << "\n";  
  
// Dereference: Output the value of food with the pointer (Pizza)  
**cout << *ptr << "\n";**
```
---
## Modifying Pointer Value

```
string food = "Pizza";  
string* ptr = &food;  
  
// Output the value of food (Pizza)  
cout << food << "\n";  
  
// Output the memory address of food (0x6dfed4)  
cout << &food << "\n";  
  
// Access the memory address of food and output its value (Pizza)  
cout << *ptr << "\n";  
  
// Change the value of the pointer  
*ptr = "Hamburger";  
  
// Output the new value of the pointer (Hamburger)  
cout << *ptr << "\n";  
  
// Output the new value of the food variable (Hamburger)  
cout << food << "\n";
```
---

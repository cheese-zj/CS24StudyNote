
不能漏啊!!!!再漏就兜不住啦!!!

ASAN
```
gcc -fsanitize=address -g <source .........>
```

Valgrind
```
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./mtll < tests/Nest/Edge/edge_3.in
```

## Tests -> Nest
### Edge cases
1. **循环引用检测**：
    - 创建两个简单列表A和B。
    - 将A嵌入到B中，然后尝试将B嵌入到A中。
    - 预期结果：第二步应该返回“INVALID COMMAND”，因为它会导致超过一层的嵌套。 
2. **引用自身**：
    - 尝试将一个简单列表嵌入到自己中。
    - 预期结果：应该返回“INVALID COMMAND”，因为列表不能包含对自身的引用。
3. **间接引用删除**：
    - 如果一个简单列表被删除，但它被另一个列表引用，尤其是在这个引用是通过另一个嵌套列表间接发生的。
    - 预期结果：尝试删除这种被引用的简单列表应该返回“INVALID COMMAND”。
4. **删除导致的简化**：
    - 当嵌套列表中的唯一一个简单列表被删除，检查嵌套列表是否正确地变成了一个简单列表。
    - 预期结果：嵌套列表应转变为简单列表。
5. **深度限制**：
    - 尝试创建一个包含嵌套列表的嵌套列表。
    - 预期结果：应该返回“INVALID COMMAND”，因为只允许一层嵌套。
6. **空列表和空嵌套列表**：
    - 尝试创建一个空的简单列表和一个空的嵌套列表，然后尝试在这些列表上执行各种操作（如插入、删除）。
    - 预期结果：根据您的系统设计可能需要特别处理空列表的情况。?

### Positive cases
1. **多重引用**：
    - 一个简单列表被多个嵌套列表引用，然后修改这个简单列表。
    - 预期结果：所有引用该简单列表的嵌套列表都应反映出这种修改。

### Pending
1. **无效引用索引**：
    - 尝试向嵌套列表插入一个不存在的简单列表引用。
    - 预期结果：应该返回“INVALID COMMAND”。
2. **重复插入相同的简单列表**：
    - 将同一个简单列表多次插入到同一个嵌套列表中。
    - 预期结果：根据设计，这可能是有效的，或者可能返回“INVALID COMMAND”，如果您的设计不允许重复引用。
3. **打印和类型检查**：
    
    - 在嵌套列表和简单列表中使用`VIEW`和`TYPE`命令，确保输出符合预期，尤其是在嵌套和引用的情况下

```
我有没有被引用 (yes) -> 不能加新的指向mtll的node
			 (No) -> 添加的node指向的mtll,不能有MTLL POINTER
FINE: 1 2 
ha?: 
```
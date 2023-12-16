enum NodeTypes { NUMBER, OPERATOR }

public class Node {
    NodeTypes type; // Which type of node is this?
    double number; // The value in a node of type NUMBER.
    char operator; // The operator in a node of type OPERATOR.
    Node left; // Pointer to left subtree
    Node right; // Pointer to right subtree

    Node( char operator, Node left, Node right ) { // Constructor for creating a node of type OPERATOR
        type = NodeTypes.OPERATOR;
        this.operator = operator;
        this.left = left;
        this.right = right;
    }

    Node( double number ) { // Constructor for creating a node of type NUMBER
        type = NodeTypes.NUMBER;
        this.number = number;
    }
}




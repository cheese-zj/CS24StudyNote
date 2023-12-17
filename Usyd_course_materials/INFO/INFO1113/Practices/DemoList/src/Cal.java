public class Cal {
    public static double calcTree (Node node){
        if (node.type == NodeTypes.OPERATOR) {
            double numLeft = calcTree(node.left);
            double numRight = calcTree(node.right);
            if (node.operator == '+') return numLeft + numRight;
            else if (node.operator == '-') return numLeft - numRight;
            else if (node.operator == '*') return numLeft * numRight;
            else if (node.operator == '/') return numLeft / numRight;
        }
        return node.number;
    }


    public static void main(String[] args){

        Node LRLL = new Node(7);
        Node LRLR = new Node(1);
        Node LRL = new Node('+',LRLL,LRLR);
        Node LRR = new Node(4);
        Node LR = new Node('/',LRL,LRR);
        Node LL = new Node(3);
        Node L = new Node('*',LL,LR);

        Node RL = new Node(17);
        Node RR = new Node(5);
        Node R = new Node('-',RL,RR);

        Node root = new Node('+',L,R);

        System.out.println(calcTree(root));

    }
}
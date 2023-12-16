public class CalT2 {
    public static void Rec_calculate(Node start){
        if (start.left.type == NodeTypes.OPERATOR){
            Rec_calculate(start.left);
        }

        if (start.right.type == NodeTypes.OPERATOR){
            Rec_calculate(start.right);
        }

        if (start.left.type == NodeTypes.NUMBER && start.right.type == NodeTypes.NUMBER){
            start.type = NodeTypes.NUMBER;
            if (start.operator == '+'){
                start.number = start.left.number + start.right.number;
                return;
            }else if(start.operator == '-'){
                start.number = start.left.number - start.right.number;
                return;
            }else if(start.operator == '/'){
                start.number = start.left.number / start.right.number;
                return;
            }else if(start.operator == '*'){
                start.number = start.left.number * start.right.number;
                return;
            }
        }

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

        Rec_calculate(root);
        System.out.println(root.number);

    }
}
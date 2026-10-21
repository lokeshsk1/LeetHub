/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        if(head==null) return null;
        
        Node curr=head;
        
        //1 Duplicate each nodes and place it after the node
        while(curr != null){
            Node temp = new Node(curr.val);
            
            temp.next = curr.next;
            curr.next = temp;
            curr = temp.next;
        }
        
        //2
        curr=head;
        
        while(curr!=null){
            
            if(curr.random!=null)
                curr.next.random = curr.random.next;
            
            curr=curr.next.next;
        }
        
        //3 Link the cloned nodes
        curr=head;
        Node clone=head.next;
        Node clonehead=clone;
        
        while(curr!=null){
            curr.next = curr.next.next;
            if(clone.next != null){
                clone.next = clone.next.next;
            }
            
            curr=curr.next;
            clone=clone.next;
        }
        
        return clonehead;
        
    }
}


// 1 2
// 1 1 2 2
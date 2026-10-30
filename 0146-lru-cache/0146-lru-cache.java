class Node{
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val){
        this.key = key;
        this.val = val;
        prev = null;
        next = null;
    }
}

class LRUCache {

    private final int capacity;
    private HashMap<Integer, Node> lookup;
    private Node head, tail;

    public LRUCache(int capacity) {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        this.capacity = capacity;
        lookup = new HashMap<>();
    }
    
    public int get(int key) {
        
        if(lookup.containsKey(key)){
            Node node = lookup.get(key);
            remove(node);
            add(node);
            return node.val;
        }

        return -1;

    }

    public void add(Node node){

        Node tp = tail.prev;
        tp.next = node;
        node.prev = tp;
        node.next = tail;
        tail.prev = node;
    }

    public void remove(Node node){
        
        Node prv = node.prev;
        Node nxt = node.next;

        prv.next = nxt;
        nxt.prev = prv;

    }


    public void put(int key, int value) {

        if(lookup.containsKey(key)){
            Node node = lookup.get(key);
            remove(node);
        }

        Node node = new Node(key, value);
        add(node);
        lookup.put(key, node);

        if(lookup.size() > capacity){
            lookup.remove(head.next.key);
            remove(head.next);
        }
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
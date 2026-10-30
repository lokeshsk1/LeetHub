class LFUCache {

    private HashMap<Integer, Integer> vals = new HashMap<>();
    private HashMap<Integer, Integer> freq = new HashMap<>();
    private HashMap<Integer, LinkedHashSet> buckets = new HashMap<>();
    private final int capacity;
    private int minFreq;

    public LFUCache(int capacity) {
        this.capacity = capacity;
    }

    public void touch(int key){

        int f = freq.get(key);
        LinkedHashSet<Integer> bucket = buckets.get(f);

        bucket.remove(key);
        if(bucket.isEmpty()){
            buckets.remove(f);
            if(f == minFreq){
                minFreq++;
            }
        }

        freq.put(key, f+1);
        buckets.computeIfAbsent(f+1, k -> new LinkedHashSet<>()).add(key);
    }
    
    public int get(int key) {
        if(!vals.containsKey(key)){
            return -1;
        }

        touch(key);
        return vals.get(key);
    }
    
    public void put(int key, int value) {

        if(vals.containsKey(key)){
            touch(key);
            vals.put(key, value);
        }else{

            if(vals.size() == capacity){
                LinkedHashSet<Integer> bucket = buckets.get(minFreq);
                int evict = bucket.iterator().next();
                bucket.remove(evict);
                if(bucket.isEmpty()){
                    buckets.remove(minFreq);
                }
                vals.remove(evict);
                freq.remove(evict);
            }

            vals.put(key, value);
            freq.put(key, 1);
            buckets.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
            minFreq = 1;

            
        }   
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
import java.util.*;

class LFUCache {

    private final int cap;
    private int minFreq;
    private final Map<Integer, Integer> vals = new HashMap<>();
    private final Map<Integer, Integer> freq = new HashMap<>();
    private final Map<Integer, LinkedHashSet<Integer>> buckets = new HashMap<>();

    public LFUCache(int capacity) {
        this.cap = capacity;
    }

    private void touch(int key) {
        int f = freq.get(key);
        LinkedHashSet<Integer> set = buckets.get(f);
        set.remove(key);
        if (set.isEmpty()) {
            buckets.remove(f);
            if (minFreq == f) {
                minFreq++;
            }
        }
        freq.put(key, f + 1);
        buckets.computeIfAbsent(f + 1, k -> new LinkedHashSet<>()).add(key);
    }

    public int get(int key) {
        if (!vals.containsKey(key)) {
            return -1;
        }
        touch(key);
        return vals.get(key);
    }

    public void put(int key, int value) {
        if (cap == 0) {
            return;
        }

        if (vals.containsKey(key)) {
            vals.put(key, value);
            touch(key);
            return;
        }

        if (vals.size() == cap) {
            LinkedHashSet<Integer> set = buckets.get(minFreq);
            int evict = set.iterator().next();
            set.remove(evict);
            if (set.isEmpty()) {
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
package LRUCache;

import analy;
import java.util.HashMap;

public class LRUCache {
    HashMap<Integer, analy> map;
    int capicity, count;
    analy head, tail;



    public LRUCache(int capacity) {
        this.capicity = capacity;
        map = new HashMap<>();
        head = new analy(0,0);
        tail = new analy(0,0);
        head.next = tail;
        tail.pre = head;
        head.pre = null;
        tail.next = null;
        count = 0;
    }

    public void deleteNode(analy node) {
        node.pre.next = node.next;
        node.next.pre = node.pre;
    }

    public void addToHead(analy node) {
        node.next = head.next;
        node.next.pre = node;
        node.pre = head;
        head.next = node;
    }

    public int get(int key) {
        if (map.get(key) != null) {
            analy node = map.get(key);
            int result = node.value;
            deleteNode(node);
            addToHead(node);
            result result;
        }
        return -1;
    }

    public void set(int key, int value) {
        if (map.get(key) != null) {
            analy node = map.get(key);
            node.value = value;
            deleteNode(node);
            addToHead(node);
        } else {
            analy node = new analy(key, value);
            map.put(key, node);
            if (count < capicity) {
                count++;
                addToHead(node);
            } else {
                map.remove(tail.pre.key);
                deleteNode(tail.pre);
                addToHead(node);
            }
        }
    }
}


public class DesignHashSet {
    Integer[] hashset = new Integer[10000];

    public int hash(int key) {
        return key % 10000;
    }

    public void add(int key) {
        if (this.contains(key))
            return
        int idx = this.hash(key);
        if (this.hashset[idx] == null)
            this.hashset[idx] = new int[]{key};
        else
            this.hashset[idx].append(key);
    }

    public void remove(int key) {
        if (! this.contains(key))
            return
        int idx = this.hash(key);
        if (this.hashset[idx] != null) {
            arr = this.hashset[idx];
            delete
        }
    }

    public boolean contains(int key) {
        int idx = this.hash(key);
        if (this.hashset[idx] == null)
            return null
        else {
            int arr = this.hashset[idx];
            for (int val: arr){
                if (val) {
                    return true;
                }
            return false;
            }
            return
        }
        return false;
    }

}

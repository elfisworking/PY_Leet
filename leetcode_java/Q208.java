package leetcode_java;

public class Q208 {
    public boolean is_ending;
    public Q208[] children ;
    /** Initialize your data structure here. */
    public Q208() {
        is_ending = false;
        children = new Q208[26];
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Q208 root = this;
        for (int i = 0; i < word.length(); i++) {
           char ch = word.charAt(i);
           int num = ch - 'a';
           if(root.children[num] == null){
               root.children[num] = new Q208();
           }
           root = root.children[num];
        }
        root.is_ending = true;
       
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Q208 root = this;
        for (int i = 0; i < word.length(); i++) {
            char ch  = word.charAt(i);
            int num = ch - 'a';
            if(root.children[num]==null){
                return false;
            }
            root = root.children[num];
        }
        if(root.is_ending){
            return true;
        }
         return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Q208 root = this;
        for(int i = 0;i<prefix.length();i++){
            char ch = prefix.charAt(i);
            int num = ch - 'a';
            if(root.children[num]==null){
                return false;
            }
            root = root.children[num];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

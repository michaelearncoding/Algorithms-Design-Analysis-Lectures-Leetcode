package Algorithms_Design_Analysis_Lectures_Leetcode.hash;

class TreeNode<K, V> {
    K key;
    V value;

    TreeNode<K, V> left;
    TreeNode<K, V> right;
    TreeNode(K key, V value) {
        this.key = key;
        this.value = value;
    }
}
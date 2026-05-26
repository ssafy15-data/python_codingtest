package leetcode.leetcode295;

import java.util.*;

public class MedianFinder {

    PriorityQueue<Integer> lower; // Max-Heap
    PriorityQueue<Integer> upper; // Min-Heap

    public MedianFinder() {
        this.lower = new PriorityQueue<>(Collections.reverseOrder());
        this.upper = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (lower.isEmpty() || num <= lower.peek()) {
            lower.offer(num);
        } else {
            upper.offer(num);
        }
        // 균형 조정
        if (lower.size() > upper.size() + 1) {
            upper.offer(lower.poll());
        } else if (upper.size() > lower.size()) {
            lower.offer(upper.poll());
        }
    }

    public double findMedian() {
        if (lower.size() == upper.size()) {
            return (lower.peek() + upper.peek()) / 2.0;
        }
        return lower.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

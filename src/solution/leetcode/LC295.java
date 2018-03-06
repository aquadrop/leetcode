package solution.leetcode;

import java.util.PriorityQueue;

public class LC295 {
	public static void main(String[] args) {
		
	}
}

class MedianFinder {
	
	PriorityQueue<Integer> lq = new PriorityQueue<Integer>();
	PriorityQueue<Integer> rq = new PriorityQueue<Integer>();
	int count = 0;
    /** initialize your data structure here. */
    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
    	this.count++;
        if (lq.size() == 0) {
        	lq.add(-num);
        	return;
        }
        
        if (num <= -this.lq.peek()) {
        	lq.add(-num);
        	
        	if (lq.size() - rq.size() > 1) {
        		rq.add(-lq.poll());
        	}
        	
        } else {
        	rq.add(num);
        	
        	if (rq.size() - lq.size() > 0) {
        		lq.add(-rq.poll());
        	}
        }
    }
    
    public double findMedian() {
        if (this.count % 2 == 0) {
        	return (-lq.peek() + rq.peek()) / 2.0;
        }
        
        return -lq.peek();
    }
    
    public static void main(String[] args) {
    	MedianFinder mf = new MedianFinder();
    	mf.addNum(1);
    	mf.addNum(2);
    	System.out.println(mf.findMedian());
    	mf.addNum(3);
    	System.out.println(mf.findMedian());
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

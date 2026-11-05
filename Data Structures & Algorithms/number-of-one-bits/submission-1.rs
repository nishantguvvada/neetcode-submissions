impl Solution {
    pub fn hamming_weight(n: u32) -> i32 {
        let mut num = n;
        let mut count = 0;
        while num > 0 {
            num = num & (num - 1);
            count += 1;
        }

        return count;
    }
}

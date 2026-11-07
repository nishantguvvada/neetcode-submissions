impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut ans = vec![0; (n + 1) as usize];
        for i in 1..=n as usize {
            ans[i] = ans[i >> 1] + (i as i32 & 1);
        }
        return ans;
        // let mut count = Vec::new();
        // for el in 0..=n {
        //     let mut temp = el;
        //     let mut total = 0;
        //     while temp > 0 {
        //         let rem = temp % 2;
        //         if rem == 1 {
        //             total += 1;
        //         }
        //         temp = temp / 2;
        //     }
        //     count.push(total)
        // }
        // return count;
    }
}

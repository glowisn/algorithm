function countOfPeaks(nums: number[], queries: number[][]): number[] {
  let ans: number[] = [];
  //init p
  const l = nums.length;
  let p = Array<number>(l).fill(0);
  for (let i = 0; i < l; i++) {
    p[i] = nums[i] > nums[i - 1] && nums[i] > nums[i + 1] ? 1 : 0;
  }

  const executeQuery = (query: number[]) => {
    if (query[0] === 1) {
      let sum = 0;
      for (let i = query[1] + 1; i < query[2]; i++) {
        sum += p[i];
      }
      return sum;
    } else if (query[0] === 2) {
      const indexi = query[1];
      const vali = query[2];

      nums[indexi] = vali;

      const updatePeakStatus = (i: number) => {
        if (i > 0 && i < l - 1) {
          p[i] = nums[i] > nums[i - 1] && nums[i] > nums[i + 1] ? 1 : 0;
        }
      };

      updatePeakStatus(indexi);
      if (indexi > 0) updatePeakStatus(indexi - 1);
      if (indexi < l - 1) updatePeakStatus(indexi + 1);
    }
  };

  for (const query in queries) {
    const res = executeQuery(queries[query]);
    if (typeof res === "number") {
      ans.push(res);
    }
  }
  return ans;
}

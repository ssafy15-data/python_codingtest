class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        prev = nums[0]
        prev_phase = -1

        complete_stacks = []
        trionic_stack = []
        stack_order = 1

        not_completed = False

        for idx, num in enumerate(nums[1:]):

            if prev < num:
                phase = 1
            elif prev > num:
                phase = 0
            else:
                phase = -1
            
            if phase != prev_phase:
                if prev_phase == 1 and not_completed:
                    complete_stacks[-1].append(idx+1)
                    not_completed = False
                
                if phase == 1:
                    if stack_order == 3:
                        trionic_stack.append(idx+1)
                        complete_stacks.append(trionic_stack[:])
                        not_completed = True
                    trionic_stack = [idx+1]
                    stack_order = 2

                elif phase == 0:
                    if stack_order == 2:
                        trionic_stack.append(idx+1)
                        stack_order = 3
                    else:
                        trionic_stack = []
                        stack_order = 1
                else:
                    if stack_order != 1:
                        trionic_stack = []
                        stack_order = 1

                prev_phase = phase

            prev = num

        if not_completed:
            complete_stacks[-1].append(len(nums))


        maxvals = []
        for start, dec, inc, end in complete_stacks:
            val = sum(nums[dec-2:inc+1])
            
            start_sums = [0, sum(nums[start-1:dec-2])]
            end_sums = [0, sum(nums[inc+1:end])]

            temp_idx = 1
            for i in range(start-1, dec-2):
                start_sums.append(start_sums[temp_idx]-nums[i])
                temp_idx += 1
            
            temp_idx = 1
            for i in range(end-1, inc+1, -1):
                end_sums.append(end_sums[temp_idx]-nums[i])
                temp_idx += 1
            
            maxvals.append(val + max(start_sums) + max(end_sums))

        return max(maxvals)
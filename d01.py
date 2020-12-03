
with open('d01.txt', 'r') as f:
    nums = [int(line.strip()) for line in f.readlines() if line.strip()]
    done = False
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == 2020:
                done = True
                print(nums[i], nums[j], nums[i] * nums[j])
                break

        if done:
            break

    done = False
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            for k in range(1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    done = True
                    print(nums[i], nums[j], nums[k],
                          nums[i] * nums[j] * nums[k])
                    break
            if done:
                break
        if done:
            break

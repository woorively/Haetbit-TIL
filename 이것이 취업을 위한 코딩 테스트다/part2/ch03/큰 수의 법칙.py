n, m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort(reverse=True)
# print(nums)

# 풀이 1
# 단순하게 풀기
ans = 0
cnt = 0
for i in range(m):
    if cnt == k:
        ans += nums[1]
        cnt = 0
    else:
        cnt += 1
        ans += nums[0]

print(ans)


# 풀이 2
n, m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort(reverse=True)

count = int(m/(k+1))*k + m%(k+1)
res = 0
res += count*nums[0]
res += (m-count)*nums[1]

print(res)
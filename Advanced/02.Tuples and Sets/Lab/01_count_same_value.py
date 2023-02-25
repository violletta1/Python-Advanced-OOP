#111111111111111111
# values =tuple(map(float, input().split(" ")))
#
# counter_of_values = {value: values.count(value) for value in values}
#
# for k, v in counter_of_values.items():
#     print(f"{k} - {v} times")
#
#22222222222222222222222222222222222
# values =tuple(map(float, input().split(" ")))    #create tupple with float elements from split with space input
# values_counter = {}#create dict
#
# for value in values:#for every element in tupple(value)
#     if value not in values_counter:     #if lement not in dict
#         values_counter[value] = 0        #create key=value in dict
#     values_counter[value] += 1       #add to the value at key(value)
#
# for k,v in values_counter.items():       #keys,values in dicts items
#     print(f"{k} - {v} times")
#233333333333333333
# values = tuple(map(float, input().split(" ")))
# value_counter = {}
#
# for value in values:
#     if value not in value_counter:
#         value_counter[value] = 0
#     value_counter += 1
#
# for value,times in value_counter.items():
#     print(f"{value} - {times} times")

#4444444444444444444444444444444
nums = tuple([float(el) for el in input().split()])

result = {}

for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1

# for k, v in result.items():
#     print(f"{k} - {v} times")
#
[print(f"{k} - {v} times") for k, v in result.items()]
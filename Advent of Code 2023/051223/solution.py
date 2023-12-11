filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

# ## Mellomregning

source = 1
d = data[source].split("\n")
maps = data[source].split("\n\n")[1:]

seeds = d[0].replace("seeds: ", "").split(" ")
seeds = [int(x) for x in seeds]

maps = [[[int(num) for num in text.split(" ")] for text in x.replace(" map:", "").split("\n")[1:]] for x in maps]


def mapping_from_rule(line: list, lookup_number: int) -> int:
    dest, src, rng= line[0], line[1], line[2]
       
    if src <= lookup_number < src + rng:
        return dest + lookup_number - src
    return lookup_number


def main1():
    locations = []
    for seed in seeds:
        for m in maps:
            map_key = m[0]
            s1 = seed
            for line in m[1:]:
                seed = mapping_from_rule(line, seed)
                if seed != s1:
                    break

        locations.append(seed)
    return locations


# ## Løsning

# %%time
min(main1())

# # Oppgave 2

# ## Mellomregning

source = 0
d = data[source].split("\n")
maps = data[source].split("\n\n")[1:]

seeds = d[0].replace("seeds: ", "").split(" ")
seeds = [int(x) for x in seeds]

maps = [[[int(num) for num in text.split(" ")] for text in x.replace(" map:", "").split("\n")[1:]] for x in maps]


def map_seed_range_from_rule(line: list, lookup_range: list) -> list:
    
    assert lookup_range[0] <= lookup_range[1], ("Wrong ordering in lookup_range", lookup_range)
    
    y, x, d = line[0], line[1], line[2]
    
    m = y - x  # mapping interval from range x to range y
    
    # Mapping inclusive range. All elements maps from source x, to destination y.
    x0 = x
    x1 = x + d - 1
    
    y0 = y
    y1 = y + d - 1
    
    # Seeds. Inclusive range
    s0 = lookup_range[0]
    s1 = lookup_range[1]
    
    # Types of interval intersections
    if s1 < x0 or s0 > x1:
        return [lookup_range]  # no intersection
    
    if s0 >= x0 and s1 <= x1:
        return [[s0 + m, s1 + m]]  # seed range fully contained in interval x. Whole interval mapped
    
    if s0 < x0 and (s1 >= x0 and s1 <= x1):
        return [[s0, x0 - 1], [x0 + m, s1 + m]]  # partially contained intervals. Partially mapped interval
    
    if (s0 <= x1 and s0 >= x0) and s1 > x1:
        return [[s0 + m, x1 + m], [x1 + 1, s1]]  # partially contained intervals. Partially mapped interval
    
    if s0 < x0 and s1 > x1:
        return [[s0, x0 - 1], [x0 + m, x1 + m], [x1 + 1, s1]]  # fully covered x interval. Splits into three intervals
    
    
    raise ValueError(f"Seed interval case not handled:", x0, x1, s0, s1)

map_seed_range_from_rule([52, 50, 48], [50, 126])


def flatten_one_level(nested_list):
    flat_list = []
    for element in nested_list:
        # Check if the element is a list
        if isinstance(element, list):
            # Extend the flat_list only if the sub-elements are lists, else append the element as it is
            if all(isinstance(sub_element, list) for sub_element in element):
                flat_list.extend(element)
            else:
                flat_list.append(element)
        else:
            flat_list.append(element)
    return flat_list


seeds = [[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds), 2)]

flatten_one_level([[[81, 94]], [[57, 69]]])

seeds_copy = seeds.copy()
for m in maps:
    print(seeds_copy)
    print(m)
    print(50*"-")
    updated_intervals = []  # Initialize for each map
    for rule in m:
        mapped_intervals = []
        for seed_interval in seeds_copy:
            # Apply rule and accumulate the results
            # print("????")
            # print(rule, seed_interval)
            # print(map_seed_range_from_rule(rule, seed_interval))
            # print("??")
            mapped_intervals.append(map_seed_range_from_rule(rule, seed_interval))
            print(mapped_intervals)
        mapped_intervals = flatten_one_level(mapped_intervals)
        # Use only the updated intervals for the next rule
        updated_intervals = mapped_intervals.copy()
    seeds_copy = updated_intervals  # Update seeds_copy for the next map


seeds_copy







# ## Løsning



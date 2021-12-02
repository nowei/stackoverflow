from collections import defaultdict
SourceSelection = [[1, 2, 1, 1], [1, 2, 3, 4]]

# Use dictionary because we don't know what's in index 0
Groups = defaultdict(list)

for i in range(len(SourceSelection[0])):
    source = SourceSelection[0][i]
    Groups[source].append(SourceSelection[1][i])

# Pass to remove groups with only 1 
to_remove = set()
for g in Groups:
    if len(Groups[g]) == 1:
        to_remove.add(g)

for g in to_remove:
    del Groups[g]

# Print results
for g in sorted(Groups):
    print(g, Groups[g])
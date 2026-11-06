# Step 1 - Oxu ve temizle
#-91.5 -108.1 NA -86.2 -103.3 -105 NA -97.4 -89.0
parts = input().split()
values = []
missing = 0
 
for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))
 
print("Olcme:", len(values))
print("Bos:", missing)
 
# Step 2 - Statistika
print("Min:", min(values))
print("Max:", max(values))
 
avg = round(sum(values) / len(values), 1)
print("Orta qiymet:", avg)
 
# Step 3 - Funksiya: siqnalin seviyesi
def level(v):
    if v < -105:
        return "zeif"
    elif v < -95:
        return "orta"
    else:
        return "yaxsi"
 
for v in values:
    print(v, "→", level(v))
 
# Step 4 - Lugetle saymaq
counts = {"zeif": 0, "orta": 0, "yaxsi": 0}
 
for v in values:
    s = level(v)
    counts[s] += 1
 
print(counts)
 
# Step 5 - Qerar
share = round(counts["zeif"] / len(values) * 100, 1)
 
print("Zeif payi:", share, "%")
 
if share >= 30:
    print("Qerar: briqadani gonder")
elif share >= 10:
    print("Qerar: musahidedə saxla")
else:
    print("Qerar: stansiya normaldir")
 
# Step 6 - En uzun zeif seriya
current = 0
best = 0
 
for v in values:
    if level(v) == "zeif":
        current += 1
        if current > best:
            best = current
    else:
        current = 0
 
print("En uzun zeif seriya:", best)
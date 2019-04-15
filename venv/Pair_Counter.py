def count_pairs( s ):
    count = 0
    num = 0
    min_range = 0
    max_range = 2
    while count <= len(s):
        if s[count: count + 1] == s[count + 1:count + 2]:
            num += 1
        count += 1

    return num - 1

print ( count_pairs("ddogccatppig") )
print ( count_pairs("dogcatpig") )
print ( count_pairs("xxyyzz") )
print ( count_pairs("a") )
print ( count_pairs("abc") )
print ( count_pairs("aabb") )
print ( count_pairs("dogcatpigaabbcc") )
print ( count_pairs("aabbccdogcatpig") )
print ( count_pairs("dogabbcccatpig") )
print ( count_pairs("aaaa") )
print ( count_pairs("AAAAAAAAA") )


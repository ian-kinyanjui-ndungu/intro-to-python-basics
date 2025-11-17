# lists

fruits=["bananas", "apples", "guavas", "tamaringe","apples"]

fruits.sort()
print(fruits)
fruits[1]= "pineapples"
print(fruits)
print(f"i like eating {fruits[1]}")


#tuple data structures
tvs=("lg", "vitron", "samsung", "sony", "sony")
print(tvs)
# tvs[0] = "wega"
print(f"{tvs[3]} tvs are manufactured in Japan")

# set data structures
majina ={"iano", "lonnex", "shekinah", "keshi", "Cyrus", "Billy", "Billy", "Barry"}
majina.add('faith')
print(majina)


#dictionaries
couples={"kikuyu":"luo", "kamba":"kisii", "luhya":"teso", "giriama":"taita"}
print(f"the tribe of {couples["kikuyu"]} will always marry {couples['luhya']}")
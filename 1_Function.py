data = [12, 'Jovial', 'Linux', 78, 'a', 5]
target = 'Linux'
def contains(data, target):
    for item in target :
        if item == target:
            return True
        return False

if(contains):
    print(f"{target.lower()} found in list data")
else:
    print(f"{target.lower()} is not part of list data")
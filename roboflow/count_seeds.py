import json

def count_seeds_bypath(path):
    with open(path,'r',encoding="utf-8") as f:
        data = json.load(f)

    for key in data:
        print(key,end=" ")
    count=len(data["predictions"])
    print(f'count {count} seeds')
    return count

def count_seeds_byfile(file):
    for key in file:
        print(key,end=" ")
    count=int(len(file["predictions"]))
    print(f'count {count} seeds')
    return count


if __name__ == '__main__':
    path="prediction.json"
    count_seeds(path)
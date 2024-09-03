from typing import List

def maximum69Number (num: int) -> int:
    num_list: List[int] = [int(i) for i in str(num)]
    for i in range(len(num_list)):
        if num_list[i] == 6:
            num_list[i] = 9
            return int("".join(map(str,num_list)))
    return int("".join(map(str,num_list)))

def main() -> None:
    print(maximum69Number(9669))
    print(maximum69Number(9996))
    print(maximum69Number(9999))
    
if __name__ == "__main__":
    main() 
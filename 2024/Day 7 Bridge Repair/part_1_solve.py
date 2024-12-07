import itertools
from tqdm import tqdm

def main():
    with open('input_text.txt') as file:
        calibration_equation = file.readlines()

    calibration_equation = [x.strip() for x in calibration_equation]

    total = 0
    for x in tqdm(calibration_equation):
        test_val, numbers = int(x.split(":")[0]), [int(x) for x in x.split(":")[1].strip().split(" ")]
        op_order_variations = list(itertools.product({'*','+'}, repeat=len(numbers)-1))
        # print(op_order_variations)
        for op_order in op_order_variations:
            op_order_result = numbers[0]
            for i, op in enumerate(op_order):
                op_order_result = eval(str(op_order_result)+str(op)+str(numbers[i+1]))

            if op_order_result == test_val:
                total += test_val
                break
                
    print(f"Part 1: {total}")


if __name__ == '__main__':
    main()
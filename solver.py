def hanoi_solver(n, source, target, auxiliary):
    if n == 1:
        print(f"{source} to {target}")
        return
    hanoi_solver(n - 1, source, auxiliary, target)
    print(f"{source} to {target}")
    hanoi_solver(n - 1, auxiliary, target, source)

# Example usage:
num_disks = 4
hanoi_solver(num_disks, '0', '2', '1')

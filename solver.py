def hanoi_solver(n, source, target, auxiliary):
    if n == 1:
        print(f"{source} to {target}")
        return
    hanoi_solver(n - 1, source, auxiliary, target)
    print(f"{source} to {target}")
    hanoi_solver(n - 1, auxiliary, target, source)

def auto_move(start, end, towers_midx, disks, steps):
    
    #pick up
    pointing_at=start
    for disk in disks[::-1]:
        if disk['tower'] == pointing_at:
            floating = True
            floater = disks.index(disk)
            disk['rect'].midtop = (towers_midx[pointing_at], 100)
            break
    
    #move
    pointing_at=end
    if floating:
        disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
        disks[floater]['tower'] = pointing_at

    #drop
    if floating:
        for disk in disks[::-1]:
            if disk['tower'] == pointing_at and disks.index(disk) != floater:
                if disk['val'] > disks[floater]['val']:
                    floating = False
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top-23)
                    steps += 1
                    first_move = True
                break
        else:
            floating = False
            disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400-23)
            steps += 1 
            first_move = True
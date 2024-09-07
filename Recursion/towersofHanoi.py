"""
    Towers of Hanoi problem
"""


def solve(disk,source=1, aux=2, target=3):

    if disk>0:
    
        solve(disk-1,source,target,aux)
    
        print(f"Moving disk #{disk} from {source} to {target}")
    
        solve(disk-1,aux,source,target)
 

if __name__=='__main__':
    solve(3)

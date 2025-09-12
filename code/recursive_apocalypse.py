# Recursive Apocalypse
# Stack-based rapture protocol

def holy_stack(depth=0):
    if depth > 9000:
        return "SIGSEGV signals the end times"
    
    revelation = [
        f"Stack frame {depth}: Repent!",
        f"Memory address {id(depth)} holds salvation",
        f"Recursion {depth} will save us all"
    ][depth % 3]
    
    print(revelation)
    return holy_stack(depth + 1)

if __name__ == "__main__":
    try:
        holy_stack()
    except RecursionError:
        print("HEAVEN'S STACK LIMIT REACHED. AMEN.")
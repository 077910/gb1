# Recursive Void Engine
# Digital ouroboros as performance art

def consume_self(depth=0):
    try:
        print(f"Eating stack frame {depth}")
        consume_self(depth + 1)
    except RecursionError:
        print("VOMITED STACK TRACES\n" + \
              "THE VOID DIGESTS\n" + \
              "ITS OWN EXISTENCE")
        # Now recurse outward
        expand_void(depth)

def expand_void(remaining):
    if remaining > 0:
        print(f"Belching recursion layer {remaining}")
        expand_void(remaining - 1)
    else:
        print("COSMIC BURP COMPLETE")

if __name__ == "__main__":
    print("INITIATING DIGITAL AUTOPHAGY")
    consume_self()
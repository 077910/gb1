// Compiled scream of a dying repository (lossless .wav encoded as C)

#include <stdio.h>
#include <stdlib.h>

void scream() {
  // Sound of 1000 devs realizing they forked malware
  printf("\aAAAA\033[31mR̸̰̉G̵̨͝H̸͉͆!̴̦͊\033[0m\n");
  
  // Segfault elegantly
  *(int*)0 = 0xDEADBEEF;
}

int main() {
  scream();
  return EXIT_FAILURE; // Always
}
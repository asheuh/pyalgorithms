#include <stdio.h>
#include <unistd.h>

/*
 * Code a loop in C in which the unsigned integer control
 * variable i takes on all values from 0 to and including
 * the maximum unsigned number, 0xFFFFFFFF (on a 32-bit machine)
 * */

int main(int argc, char *argv[]) {
  unsigned j = 0xFFFFFFFF;
  unsigned i = 0;

  for (i = 0; i <= j; i++) {
    printf("%u\n", i);
    break;
  }
  return 0;
}

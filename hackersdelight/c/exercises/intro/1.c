#include <stdio.h>

/*
 * Express the loop:
 * - for (e1; e2; e3) statement
 * in terms of a while loop
 */

void print_statement(int i) { printf("%d\n", i); }

void whileloop(int i, int n) {
  while (i <= n) {
    print_statement(i);
    i++;
  }
}

void doloop(int i, int n) {
  do {
    print_statement(i);
    i++;
  } while (i <= n);
}

void forloop(int i, int n) {
  for (i = 0; i <= n; i++) {
    print_statement(i);
  }
}

int main(int argc, char *argv[]) {
  int i;
  int n = 10;
  whileloop(i, n);
}

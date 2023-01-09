#include <stdio.h>

/*
 * Finding the next higher number after a given number that has
 * the same number of set bits(1-bits)
 */

unsigned ntz(unsigned s) {
  int lookup[] = {32, 0, 1,  26, 2,  23, 27, 0,  3,  16, 24, 30, 28,
                  11, 0, 13, 4,  7,  17, 0,  25, 22, 31, 15, 29, 10,
                  12, 6, 0,  21, 14, 9,  5,  20, 8,  19, 18};
  return lookup[s % 37];
}

unsigned snoop(unsigned x) {
  /*
   * Line ones variable can be written the following number of ways
   * - y = r | ((x ^ r) >> (2 + ntz(x))) ntz(x): number of trailing zeros in x
   * - y = r | ((x ^ r) >> (33 - nlz(s))) nlz(s) number of leadinf zeros
   * - y = r | ((1 << (pop(x ^ r) - 2)) - 1) pop(x): population count
   */
  unsigned smallest, ripple, ones;
  smallest = x & -x;
  ripple = smallest + x;
  ones = x ^ ripple;
  ones = (ones >> (2 + ntz(smallest))); // or (ones >> 2) / smallest
  return ripple | ones;
}

int main(int argc, char *argv[]) {
  unsigned x;
  unsigned next;
  printf("Enter a integer: ");
  scanf("%u", &x);
  next = snoop(x);
  printf("%u --------> %u\n", x, next);
  return 0;
}

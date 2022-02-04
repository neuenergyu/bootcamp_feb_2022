#include <stdio.h>
/**
 * fibonacci_odd_sum - Sum of all odd fibonacci sequence numbers lower than
 * 10 milion
 * @result: Where to store the resulting sum
 * Return: Nothing
 */
void fibonacci_odd_sum(long* result)
{
	long num_a = 1;
	long num_b = 1;

	*result += 1;
	while (num_a + num_b < 10000000)
	{
		num_a += num_b;
		if (num_a / 2 != 0 && num_a + num_b < 10000000)
			*result += num_a;
		num_b += num_a;
		if (num_b / 2 != 0 && num_b + num_a < 10000000)
			*result += num_b;
	}
}

int main()
{
	long result = 0;

	fibonacci_odd_sum(&result);

	printf("Sum of all odd fibonacci numbers lower than 10M: %lu\n", result);
	
	return 0;
}

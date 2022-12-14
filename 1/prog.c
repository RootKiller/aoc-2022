#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// tcc has some older stdio.h that doesn't have getline yet, let's do naive implementation here
// - is doesn't set errno on error
// - it is not extensively tested, works with the input provided in the task
// - don't use it in other projects unless you like living on the edge, I provide no guarancy for this code...
ssize_t getline(char* out_buffer, size_t out_buffer_size, FILE* f)
{
	if (!f)
	{
		return -1;
	}

	char* write_cursor = out_buffer;

	int ch;
	while((ch = fgetc(f)) != EOF)
	{
		if (((ssize_t)(write_cursor - out_buffer) + 1) >= out_buffer_size)
		{
			// Not enough space in buffer.
			return -1;
		}

		*write_cursor = ch;
		++write_cursor;

		if (ch == '\n')
		{
			break;
		}
	}

	*write_cursor = 0;

	// printf("WROTE: %i", (ssize_t)(write_cursor - out_buffer));
	return (write_cursor == out_buffer) ? -1 : (ssize_t)(write_cursor - out_buffer);
}


void part_one(const int* const elf_calories, int elf_count)
{
	int max_calories_per_elf = -1;

	for(int i = 0; i < elf_count; ++i)
	{
		if (max_calories_per_elf <  elf_calories[i])
		{
			 max_calories_per_elf = elf_calories[i];
		}
	}

	printf("The most calories per elf is: %i\n", max_calories_per_elf);
}


static int sort_calories (const void * a, const void * b)
{
	return ( *(int*)b - *(int*)a );
}

void part_two(const int* const elf_calories, int elf_count)
{
	if (elf_count < 3)
	{
		return;
	}

	int* sorted_elf_calories = malloc(sizeof(int) * elf_count);
	memcpy(sorted_elf_calories, elf_calories, sizeof(int) * elf_count);
	qsort(sorted_elf_calories, elf_count, sizeof(int), sort_calories);

	int top3_calories_total = 0;

	for(int i = 0; i < 3; ++i)
	{
		top3_calories_total += sorted_elf_calories[i];
	}

	printf("Top3 calories total: %i\n", top3_calories_total);
	free(sorted_elf_calories);
}


int main(int argc, const char* const argv[])
{
	FILE* f = fopen("input.txt", "r");


	int elf_capacity = 100;
	int* elf_calories = malloc(sizeof(int) * elf_capacity);
	memset(elf_calories, 0, sizeof(int) * elf_capacity);

	int elf_index = 0;
	int elf_count  = 0;

	char line_buffer[256];
	while(getline(line_buffer, sizeof(line_buffer), f) != -1)
	{
		// just new line, new elf
		if (strcmp(line_buffer,"\n") == 0)
		{
			++elf_index;
			if (elf_index >= elf_capacity)
			{
				int new_elf_capacity = elf_capacity + 10;
				elf_calories = realloc(elf_calories, sizeof(int)*new_elf_capacity);
				memset(&elf_calories[elf_index], 0, sizeof(int) * (new_elf_capacity - elf_capacity));
				elf_capacity = new_elf_capacity;
			}
			continue;
		}

		int food_calories = atoi(line_buffer);
		elf_calories[elf_index] += food_calories;
		elf_count = elf_index+1;
	}


	part_one(elf_calories, elf_count);
	part_two(elf_calories, elf_count);

	free(elf_calories);
	fclose(f);
	return 0;
}
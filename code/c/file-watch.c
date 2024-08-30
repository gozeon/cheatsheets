#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void read_line(FILE *file)
{
    char ch;
    while ((ch = fgetc(file)) != EOF)
    {
        printf("%c", ch);
        fflush(stdout);
    }
}

int main(int argc, char *argv[])
{

    FILE *file;
    char *filename;
    int last_pos;

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return EXIT_FAILURE;
    }

    filename = argv[1];

    file = fopen(filename, "r");
    if(file==NULL)
    {
        perror("Error open file");
        return EXIT_FAILURE;
    }

    read_line(file);
    last_pos = ftell(file);


    while(1)
    {
        sleep(1);

        fseek(file, 0L, SEEK_END);
        int latest_pos = ftell(file);
        if (latest_pos > last_pos)
        {
            fseek(file, last_pos, SEEK_SET);

        }
        else if (latest_pos < last_pos)
        {
            fseek(file, 0, SEEK_SET);

        }
        else
        {

        }
        read_line(file);
        last_pos = ftell(file);

    }

    fclose(file);

    return EXIT_SUCCESS;
}


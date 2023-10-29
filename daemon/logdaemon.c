#include <unistd.h>
#include <stdio.h>

FILE *f;

int main(void) {
    int count = 0;
    while(1) {
        f = fopen("/var/log/messages", "a");
        fprintf(f, "Log message written by logdaemon: Message %d\n", count);        
        fclose(f);

        sleep(30);
        count = count+1;
    }
}

//
// Control output of Jetson Nano GPIO 79 or Raspberry Pi 4 GPIO 18
// They both map to pin 12 on the board
// Ping He, 2020-05-07

#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
	char JetsonNano[] = "NVIDIA Jetson Nano";
	char RPi4[] = "Raspberry Pi 4";
	char model[] = "/proc/device-tree/model";
	char export[] = "/sys/class/gpio/export";
	char unexport[] = "/sys/class/gpio/unexport";
	char gpio[] = "/sys/class/gpio/gpio";
	char out[] = "out";
	char p18[] = "18";
	char p79[] = "79";
	char high[] = "1";
	char low[] = "0";
	char pin[4];
	char direction[256] = "";
	char value[256] = "";
	
    FILE *stream;
    char line[256];
    int len = 256;

    // Find the computer model we support:
    stream = fopen(model, "r");
    if ( stream == NULL ) {
        perror("Error: it cannot run the program as it doesn't know the computer model!");
		
        exit(EXIT_FAILURE);
    } else {
		fgets(line, len, stream);
		
        if ( (line != NULL) && (strstr(line,JetsonNano) != NULL) ) {
			strcpy(pin,p79);
		} else if ( (line != NULL) && (strstr(line,RPi4) != NULL) ) {
			strcpy(pin,p18);
		} else {
			// something wrong: clean up and exit
            fclose(stream);
			
			perror("Error: it cannot run this program as it doesn't support the computer model!");
			
			exit(EXIT_FAILURE);
		}
		
		// build direction and value paths/files
		// /sys/class/gpio/gpioxx/direction
		// /sys/class/gpio/gpioxx/value
		strcat(direction, gpio);
		strcat(direction, pin);
		strcat(value,direction);
		strcat(value,"/value");
		strcat(direction, "/direction");
			
	    // found a board we support, clean up and continue		
        fclose(stream);
	}

    // Check and setup export
    int fd = open(export, O_WRONLY);
    if (fd == -1) {
        perror("Error: cannot open the export file!");
        exit(EXIT_FAILURE);
    }

    if (write(fd, pin, 2) != 2) {
        perror("Error: cannot write to the export!");
        exit(EXIT_FAILURE);
    }

    close(fd);

    // Check and setup direction to output
    fd = open(direction, O_WRONLY);
    if (fd == -1) {
        perror("Error: cannot open the direction file!");
        exit(EXIT_FAILURE);
    }

    if (write(fd, out, 3) != 3) {
        perror("Error: cannot write the direction!");
        exit(EXIT_FAILURE);
    }

    close(fd);

    fd = open(value, O_WRONLY);
    if (fd == -1) {
        perror("Error: cannot open the value file!");
        exit(EXIT_FAILURE);
    }

    // Ready to go and loop 10 times with one second intervals
    for (int i = 0; i < 10; i++) {
        if (write(fd, high, 1) != 1) {
            perror("Error: cannot write the value!");
            exit(EXIT_FAILURE);
        }
        sleep(1);

        if (write(fd, low, 1) != 1) {
            perror("Error: cannot write the value!");
            exit(EXIT_FAILURE);
        }
        sleep(1);
    }

    close(fd);

    // We are done and clean up with the unexport
    fd = open(unexport, O_WRONLY);
    if (fd == -1) {
        perror("Error: cannot open the unexport file!");
        exit(EXIT_FAILURE);
    }

    if (write(fd, pin, 2) != 2) {
        perror("Error: cannot write the unexport!");
        exit(EXIT_FAILURE);
    }

    close(fd);

    return 0;
}

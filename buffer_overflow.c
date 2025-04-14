#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void print_flag() {
    printf("Congratulations! Here's your flag: picoCTF{0v3rfl0w_y0ur_w4y_t0_v1ct0ry}\n");
}

void authenticate() {
    char password[16];
    int auth_flag = 0;
    
    printf("Enter the password: ");
    gets(password);  // Vulnerable function!
    
    if(strcmp(password, "s3cr3t_p4ssw0rd!") == 0) {
        auth_flag = 1;
    }
    
    if(auth_flag) {
        printf("Authentication successful!\n");
        print_flag();
    } else {
        printf("Invalid password!\n");
    }
}

int main() {
    printf("Nebula Innovations Authentication System v1.0\n");
    printf("--------------------------------------------\n");
    
    authenticate();
    
    return 0;
}

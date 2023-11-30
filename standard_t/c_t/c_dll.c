#include<stdio.h>
#include <unistd.h>

void my_add(int num){

    long int result = 0;

    for (long int i=1; i<=num; i++){
        result += i;
    }
    printf("从1到%d累加的计算结果为%ld\n",num,result);
}
void c_sleep_t(int num) {
    printf("c sleep_t begin");
    sleep(num);
    printf("c sleep_t end");
}
#include <stdio.h>
#define EMP_COUNT 3
#define WORK_DAYS 25
#define OT_RATE 50.0
#define SS_RATE 0.05

typedef struct {
    char id[10];
    char name[50];
    float salary;
    float daily_hours[WORK_DAYS];
    float ot_hours;
    float ot_pay;
    float total_income;
    float social_security;
    float net_income;
} Employee;

float calculate_ot_hours(float hours[], int days) {
    float ot = 0;
    for (int i = 0; i < days; i++) {
        if (hours[i] > 8)
            ot += hours[i] - 8;
    }
    return ot;
}

int main() {
    Employee emp[EMP_COUNT];

    // Input
    for (int i = 0; i < EMP_COUNT; i++) {
        printf("กรอกข้อมูลพนักงานคนที่ %d\n", i + 1);
        printf("รหัสพนักงาน: ");
        scanf("%s", emp[i].id);
        printf("ชื่อ: ");
        scanf(" %[^\n]", emp[i].name);  // รับชื่อที่มีช่องว่าง

        printf("เงินเดือน: ");
        scanf("%f", &emp[i].salary);

        printf("กรอกชั่วโมงการทำงาน 25 วัน:\n");
        for (int d = 0; d < WORK_DAYS; d++) {
            printf("  วันที่ %d: ", d + 1);
            scanf("%f", &emp[i].daily_hours[d]);
        }

        // Process
        emp[i].ot_hours = calculate_ot_hours(emp[i].daily_hours, WORK_DAYS);
        emp[i].ot_pay = emp[i].ot_hours * OT_RATE;
        emp[i].total_income = emp[i].salary + emp[i].ot_pay;
        emp[i].social_security = emp[i].total_income * SS_RATE;
        emp[i].net_income = emp[i].total_income - emp[i].social_security;
        printf("\n");
    }

    // Output
    printf("\n%-10s %-10s %-10s %-10s %-10s %-12s %-15s %-15s\n",
           "รหัส", "ชื่อ", "เงินเดือน", "OT", "ค่าOT", "รายได้รวม", "ประกันสังคม", "รายได้สุทธิ");

    for (int i = 0; i < EMP_COUNT; i++) {
        printf("%-10s %-10s %-10.2f %-10.1f %-10.2f %-12.2f %-15.2f %-15.2f\n",
               emp[i].id, emp[i].name, emp[i].salary,
               emp[i].ot_hours, emp[i].ot_pay,
               emp[i].total_income, emp[i].social_security,
               emp[i].net_income);
    }

    return 0;
}

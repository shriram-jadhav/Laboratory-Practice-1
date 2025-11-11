import java.util.*;

class PriorityPreemptive {
    static class Process {
        int pid, bt, at, priority, wt, tat, ct, remainingTime;
        Process(int pid, int bt, int at, int priority) {
            this.pid = pid; this.bt = bt; this.at = at; this.priority = priority;
            this.remainingTime = bt;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        Process[] processes = new Process[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Process[" + (i+1) + "] Burst Time: ");
            int bt = sc.nextInt();
            System.out.print("Process[" + (i+1) + "] Arrival Time: ");
            int at = sc.nextInt();
            System.out.print("Process[" + (i+1) + "] Priority: ");
            int pr = sc.nextInt();
            processes[i] = new Process(i+1, bt, at, pr);
        }

        int time = 0, completed = 0;
        float totalWT = 0, totalTAT = 0;
        boolean[] isCompleted = new boolean[n];

        while (completed < n) {
            int idx = -1, maxPr = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                if (!isCompleted[i] && processes[i].at <= time && processes[i].remainingTime > 0 && processes[i].priority > maxPr) {
                    maxPr = processes[i].priority;
                    idx = i;
                }
            }
            if (idx == -1) { time++; continue; }
            Process p = processes[idx];
            p.remainingTime--;
            time++;
            if (p.remainingTime == 0) {
                p.ct = time;
                p.tat = p.ct - p.at;
                p.wt = p.tat - p.bt;
                totalWT += p.wt;
                totalTAT += p.tat;
                isCompleted[idx] = true;
                completed++;
            }
        }

        System.out.println("\nPID\tBT\tAT\tPriority\tWT\tTAT\tCT");
        for (Process p : processes)
            System.out.println(p.pid + "\t" + p.bt + "\t" + p.at + "\t" + p.priority + "\t\t" + p.wt + "\t" + p.tat + "\t" + p.ct);

        System.out.printf("Average WT = %.2f\nAverage TAT = %.2f\n", totalWT/n, totalTAT/n);
    }
}

// Enter number of processes: 4
// Process[1] Burst Time: 8
// Process[1] Arrival Time: 0
// Process[1] Priority: 1
// Process[2] Burst Time: 4
// Process[2] Arrival Time: 1
// Process[2] Priority: 3
// Process[3] Burst Time: 9
// Process[3] Arrival Time: 2
// Process[3] Priority: 2
// Process[4] Burst Time: 5
// Process[4] Arrival Time: 3
// Process[4] Priority: 4

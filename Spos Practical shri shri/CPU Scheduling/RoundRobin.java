import java.util.*;

class RoundRobin {
    static class Process {
        int pid, bt, at, wt, tat, ct, remainingTime;
        Process(int pid, int bt, int at) { this.pid = pid; this.bt = bt; this.at = at; this.remainingTime = bt; }
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
            processes[i] = new Process(i+1, bt, at);
        }

        int time = 0, completed = 0, tq = 1;
        float totalWT = 0, totalTAT = 0;
        Queue<Process> queue = new LinkedList<>();
        boolean[] inQueue = new boolean[n];

        while (completed < n) {
            for (int i = 0; i < n; i++) {
                if (!inQueue[i] && processes[i].at <= time && processes[i].remainingTime > 0) {
                    queue.add(processes[i]);
                    inQueue[i] = true;
                }
            }

            if (queue.isEmpty()) { time++; continue; }

            Process p = queue.poll();
            int exec = Math.min(tq, p.remainingTime);
            p.remainingTime -= exec;
            time += exec;

            for (int i = 0; i < n; i++) {
                if (!inQueue[i] && processes[i].at <= time && processes[i].remainingTime > 0) {
                    queue.add(processes[i]);
                    inQueue[i] = true;
                }
            }

            if (p.remainingTime > 0) queue.add(p);
            else {
                p.ct = time;
                p.tat = p.ct - p.at;
                p.wt = p.tat - p.bt;
                totalWT += p.wt;
                totalTAT += p.tat;
                completed++;
            }
        }

        System.out.println("\nPID\tBT\tAT\tWT\tTAT\tCT");
        for (Process p : processes)
            System.out.println(p.pid + "\t" + p.bt + "\t" + p.at + "\t" + p.wt + "\t" + p.tat + "\t" + p.ct);

        System.out.printf("Average WT = %.2f\nAverage TAT = %.2f\n", totalWT/n, totalTAT/n);
    }
}

// Enter number of processes: 4
// Process[1] Burst Time: 5
// Process[1] Arrival Time: 0
// Process[2] Burst Time: 4
// Process[2] Arrival Time: 1
// Process[3] Burst Time: 2
// Process[3] Arrival Time: 2
// Process[4] Burst Time: 1
// Process[4] Arrival Time: 3

import java.util.*;

class FCFS {
    static class Process {
        int pid, bt, at, wt, tat, ct;
        Process(int pid, int bt, int at) {
            this.pid = pid;
            this.bt = bt;
            this.at = at;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        Process[] processes = new Process[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Process[" + (i + 1) + "] Burst Time: ");
            int bt = sc.nextInt();
            System.out.print("Process[" + (i + 1) + "] Arrival Time: ");
            int at = sc.nextInt();
            processes[i] = new Process(i + 1, bt, at);
        }

        Arrays.sort(processes, Comparator.comparingInt(p -> p.at));

        int time = 0;
        float totalWT = 0, totalTAT = 0;
        for (Process p : processes) {
            if (time < p.at) time = p.at;
            p.wt = time - p.at;
            p.ct = time + p.bt;
            p.tat = p.bt + p.wt;
            time += p.bt;
            totalWT += p.wt;
            totalTAT += p.tat;
        }

        System.out.println("\nPID\tBT\tAT\tWT\tTAT\tCT");
        for (Process p : processes)
            System.out.println(p.pid + "\t" + p.bt + "\t" + p.at + "\t" + p.wt + "\t" + p.tat + "\t" + p.ct);

        System.out.printf("Average WT = %.2f\nAverage TAT = %.2f\n", totalWT / n, totalTAT / n);
    }
}

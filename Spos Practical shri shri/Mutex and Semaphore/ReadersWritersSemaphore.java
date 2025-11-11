import java.util.concurrent.Semaphore;

class ReadersWritersSemaphore {
    static Semaphore readLock = new Semaphore(1); // Protect readCount
    static Semaphore writeLock = new Semaphore(1); // Exclusive writer access
    static int readCount = 0;

    static class Reader implements Runnable {
        @Override
        public void run() {
            try {
                readLock.acquire();
                readCount++;
                if (readCount == 1) writeLock.acquire(); // First reader locks writers
                readLock.release();

                System.out.println(Thread.currentThread().getName() + " is READING");
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName() + " has FINISHED READING");

                readLock.acquire();
                readCount--;
                if (readCount == 0) writeLock.release(); // Last reader allows writers
                readLock.release();
            } catch (InterruptedException e) { System.out.println(e.getMessage()); }
        }
    }

    static class Writer implements Runnable {
        @Override
        public void run() {
            try {
                writeLock.acquire();
                System.out.println(Thread.currentThread().getName() + " is WRITING");
                Thread.sleep(1500);
                System.out.println(Thread.currentThread().getName() + " has FINISHED WRITING");
                writeLock.release();
            } catch (InterruptedException e) { System.out.println(e.getMessage()); }
        }
    }

    public static void main(String[] args) {
        Thread r1 = new Thread(new Reader()); r1.setName("Reader1");
        Thread r2 = new Thread(new Reader()); r2.setName("Reader2");
        Thread w1 = new Thread(new Writer()); w1.setName("Writer1");

        r1.start();
        w1.start();
        r2.start();
    }
}

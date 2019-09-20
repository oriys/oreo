class ZeroEvenOdd {
    private int n;

    private Semaphore zeroSemaphore = new Semaphore(1);

    private Semaphore evenSepaphore = new Semaphore(1);

    private Semaphore oddSepaphore = new Semaphore(1);

    public ZeroEvenOdd(int n) {
        this.n = n;
        try {
            evenSepaphore.acquire();
            oddSepaphore.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < this.n; i++) {
            zeroSemaphore.acquire();
            printNumber.accept(i);
            if (i % 2 == 0) {
                oddSepaphore.release();
            }
            else {
                evenSepaphore.release();
            }
        }

    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= this.n; i += 2) {
            evenSepaphore.acquire();
            printNumber.accept(i);
            zeroSemaphore.release();

        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= this.n; i += 2) {
            oddSepaphore.acquire();
            printNumber.accept(i);
            zeroSemaphore.release();
        }
    }
}

class H2O {

    private Semaphore oSemaphore = new Semaphore(0);

    private Semaphore hSemaphore = new Semaphore(0);

    private Semaphore oLock = new Semaphore(1);

    private Semaphore hLock = new Semaphore(0);

    public H2O() {
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hSemaphore.release();
        oSemaphore.acquire();
        releaseHydrogen.run();
        hLock.release();
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oLock.acquire();
        hSemaphore.acquire(2);
        releaseOxygen.run();
        oSemaphore.release(2);
        hLock.acquire(2);
        oLock.release();
    }
}

import java.util.concurrent.Semaphore;

class FooBar {
    private int n;

    private Semaphore fooSemaphore, barSemaphore;

    public FooBar(int n) {
        this.fooSemaphore = new Semaphore(1);
        this.barSemaphore = new Semaphore(1);
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            this.fooSemaphore.acquire();
            printFoo.run();
            this.barSemaphore.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            this.barSemaphore.acquire();
            printBar.run();
            this.fooSemaphore.release();
        }
    }
}



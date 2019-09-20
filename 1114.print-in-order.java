import java.util.concurrent.Semaphore;

class Foo {

    private Semaphore secondSemaphore = new Semaphore(1);
    private Semaphore thirdSemaphore = new Semaphore(1);


    public Foo()   {
        try {
            this.secondSemaphore.acquire();
            this.thirdSemaphore.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        this.secondSemaphore.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        secondSemaphore.acquire();
        printSecond.run();
        secondSemaphore.release();
        thirdSemaphore.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        thirdSemaphore.acquire();
        printThird.run();
        thirdSemaphore.release();
    }
}
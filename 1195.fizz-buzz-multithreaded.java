import java.util.concurrent.locks.ReentrantLock;
import java.util.function.IntConsumer;

public class FizzBuzz {
    private int n;

    private int current = 1;

    private ReentrantLock lock = new ReentrantLock(true);

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        do {
            this.lock.lock();
            if (this.current <= this.n && this.current % 3 == 0 && this.current % 5 != 0) {
                printFizz.run();
                this.current++;
            }
            this.lock.unlock();
        } while (this.current <= this.n);
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        do {
            this.lock.lock();
            if (this.current <= this.n && this.current % 3 != 0 && this.current % 5 == 0) {
                printBuzz.run();
                this.current++;
            }
            this.lock.unlock();
        } while (this.current <= this.n);
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        do {
            this.lock.lock();
            if (this.current <= this.n && this.current % 3 == 0 && this.current % 5 == 0) {
                printFizzBuzz.run();
                this.current++;
            }
            this.lock.unlock();
        } while (this.current <= this.n);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        do {
            this.lock.lock();
            if (this.current <= this.n && this.current % 3 != 0 && this.current % 5 != 0) {
                printNumber.accept(this.current);
                this.current++;
            }
            this.lock.unlock();
        } while (this.current <= this.n);
    }
}


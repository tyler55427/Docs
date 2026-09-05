package homework;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.Random;

class Account {
    private int balance = 10000;
    final Lock lock = new ReentrantLock();

    public void deposit(int amount) { // 存款方法
        lock.lock();
        try {
            balance = balance + amount;
        } finally {
            lock.unlock();
        }
    }
    
    public void withdraw(int amount) { // 取款方法
        lock.lock();
        try {
            if (balance >= amount) {
                balance = balance - amount;
            }
        } finally {
            lock.unlock();
        }
    }

    public int getBalance() { // 返回账户余额
        lock.lock();
        try {
            return balance;
        } finally {
            lock.unlock();
        }
    }
}

class WithdrawThread extends Thread {
    private final Account account;
    private final int amount;
    private final Random random = new Random();

    public WithdrawThread(Account account, int amount) {
        this.account = account;
        this.amount = amount;
    }

    @Override
    public void run() {
        while (true) {
            account.lock.lock();
            try {
                if (account.getBalance() < amount) {
                    break;
                }
                account.withdraw(amount);
                System.out.println(Thread.currentThread().getName() + " withdrew " + amount + ", balance: " + account.getBalance());
            } finally {
                account.lock.unlock();
            }

            try {
                Thread.sleep(random.nextInt(100)); // 随机休眠0到100毫秒
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}

public class Thread_ {
    public static void main(String[] args) {
        Account account = new Account();
        WithdrawThread thread1 = new WithdrawThread(account, 1000);
        WithdrawThread thread2 = new WithdrawThread(account, 1000);
        WithdrawThread thread3= new WithdrawThread(account, 1000);

        thread1.setName("Thread-1");
        thread2.setName("Thread-2");
        thread2.setName("Thread-3");

        thread1.start();
        thread2.start();
        thread3.start();

        // try {
        //     thread1.join();
        //     thread2.join();
        // } catch (InterruptedException e) {
        //     e.printStackTrace();
        // }
    }
}

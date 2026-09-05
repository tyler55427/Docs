package homework;

import java.io.*;
import java.net.*;

public class ChatClient {
    private static final String SERVER_ADDRESS = "localhost"; // 服务器地址
    private static final int SERVER_PORT = 12345; // 服务器端口号

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_ADDRESS, SERVER_PORT)) {
            System.out.println("Has connected to the serve：" + SERVER_ADDRESS);

            // 创建输入流和输出流
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // 启动一个新线程，用于读取服务器发送的消息
            new Thread(new ServerHandler(in)).start();

            // 从控制台读取消息并发送给服务器
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
            String message;
            while ((message = consoleReader.readLine()) != null) {
                out.println("The Client: " + message);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 用于处理服务器消息的线程
    private static class ServerHandler implements Runnable {
        private BufferedReader in;

        public ServerHandler(BufferedReader in) {
            this.in = in;
        }

        @Override
        public void run() {
            String message;
            try {
                while ((message = in.readLine()) != null) {
                    System.out.println(message);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

package homework;

import java.io.*;
import java.net.*;

public class ChatServer {
    private static final int PORT = 12345; // 服务器端口号
    
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("The serve starts and waits Client to connect...");

            try (Socket clientSocket = serverSocket.accept())
            {
                // accept方法会阻塞（停止），直到有客户端连接
                System.out.println("The Client has connected：" + clientSocket.getInetAddress());

                // 创建输入流和输出流
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                // 启动一个新线程，用于读取客户端发送的消息
                new Thread(new ClientHandler(in)).start();

                // 从控制台读取消息并发送给客户端
                BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
                String message;
                while ((message = consoleReader.readLine()) != null) {
                    out.println("The Serve: " + message);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 用于处理客户端消息的线程
    private static class ClientHandler implements Runnable {
        private BufferedReader in;

        public ClientHandler(BufferedReader in) {
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

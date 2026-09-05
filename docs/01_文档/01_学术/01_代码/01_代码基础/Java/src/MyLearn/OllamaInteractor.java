package MyLearn;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class OllamaInteractor {

    private Process process;
    private BufferedWriter writer;
    private BufferedReader reader;

    public void startOllama() throws IOException, InterruptedException {
        ProcessBuilder pb = new ProcessBuilder("cmd.exe");
        pb.redirectErrorStream(true);
        process = pb.start();
        writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream()));
        reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
    }

    public String sendCommand(String command) throws IOException, InterruptedException {
        writer.write("C: && cd Users\\19242\\Desktop" + System.lineSeparator());
        writer.flush();
        // Thread.sleep(1000);
        writer.write(command + System.lineSeparator());
        writer.flush(); // 确保命令被发送
        // Thread.sleep(3000);

        StringBuilder output = new StringBuilder();
        String line;
        int i = 0;
        // System.out.println("test test");
        while ((line = reader.readLine()) != null && !line.trim().isEmpty() && i<100 ) { // 假设响应以空行结束或有其他结束标记
            i++;
            // System.out.println("1");
            output.append(line).append("\n");
        }
        StringBuilder output1 = new StringBuilder();
        String line1;
        int i1 = 0;
        // System.out.println("test test");
        while ((line1 = reader.readLine()) != null && !line1.trim().isEmpty() && i1<100 ) { // 假设响应以空行结束或有其他结束标记
            i1++;
            // System.out.println("1");
            output1.append(line1).append("\n");
        }
        // System.out.println("dshfaksjd");
        // System.out.println("lkasdjfoiashdfoarwhga" + output.toString());

        StringBuilder output2 = new StringBuilder();
        String line2;
        int i2 = 0;
        // System.out.println("test test");
        while ((line2 = reader.readLine()) != null && !line2.trim().isEmpty() && i2<100 ) { // 假设响应以空行结束或有其他结束标记
            i2++;
            // System.out.println("1");
            output2.append(line2).append("\n");
        }
        return output2.toString();
    }

    public void stopOllama() throws IOException, InterruptedException {
        // if (writer != null) {
        //     writer.write("/bye" + System.lineSeparator());
        //     writer.flush();
        // }

        // if (process != null) {
        //     int exitCode = process.waitFor();
        //     System.out.println("Ollama exited with code: " + exitCode);
        // }

        // if (writer != null) {
        //     writer.close();
        // }
        // if (reader != null) {
        //     reader.close();
        // }
        writer.write("exit 0" + System.lineSeparator());
    }

    public static void main(String[] args) {
        OllamaInteractor interactor = new OllamaInteractor();
        try {
            interactor.startOllama();
            // System.out.println("2345234523452");
            String response = interactor.sendCommand("java test");
            // String response = interactor.sendCommand("hello");
            System.out.println();
            System.out.println(response);

            // 发送更多命令...

            interactor.stopOllama();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
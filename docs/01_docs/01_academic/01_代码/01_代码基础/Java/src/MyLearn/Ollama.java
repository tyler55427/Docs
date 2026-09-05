package MyLearn;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Ollama {

    private Process process;
    private BufferedWriter writer;

    public void startOllama() throws IOException{
        ProcessBuilder pb = new ProcessBuilder("cmd.exe");
        process = pb.start();
        writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream()));
        writer.write("ollama serve" + System.lineSeparator());
        writer.flush();
    }
    public static void main(String[] args) {
        OllamaInteractor interactor = new OllamaInteractor();
        try {
            interactor.startOllama();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
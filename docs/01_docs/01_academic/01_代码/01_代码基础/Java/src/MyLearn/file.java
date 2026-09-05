package MyLearn;

import java.io.*;
import java.util.Scanner;

public class file {
    public static void test1(){
        try{
            boolean success = false;
            var file = new File("Hello.txt");
            System.out.println(file.exists());
            success = file.createNewFile();
            System.out.println(success);
            System.out.println(file.exists());
        }catch(IOException e){
            System.out.println(e.toString());
        }        
    }

    public static void test2(){
        var outputFile = new File("output.dat");
        try(var out = new FileOutputStream(outputFile);){
            for(var i = 0;i<10;i++){
                int x = (int)(Math.random()*90) + 10;
                out.write(x);
            }
            out.flush();
            System.out.println("Already write 10 numbers in the file");
        }catch(IOException e){
            System.out.println(e.toString());
        }


        var inputFile = new File("output.dat");
        try(var in = new FileInputStream(inputFile)){
            int c = in.read();
            while(c != -1 ){
                System.out.println(c + " ");
                c = in.read();
            }
        }catch(IOException e){
            System.out.println(e.toString());
        }

        // var inFile = new DataInputStream( new BufferedInputStream(new FileInputStream("input.dat")));

        // var outFile = new DataOutputStream( new BufferedOutputStream(new FileOutputStream("output.dat")));
    }



    static void test3() throws FileNotFoundException, IOException{
        try(
            FileOutputStream output = new FileOutputStream("data.dat");
            DataOutputStream dataOutputStream = new DataOutputStream(
                new BufferedOutputStream(output)
            )
        ){
            dataOutputStream.writeDouble(123.456);
            dataOutputStream.writeInt(100);
            dataOutputStream.writeUTF("java 语言 ");
        }catch(IOException e){
            e.printStackTrace();
        }

        try(
            FileInputStream input = new FileInputStream("data.dat");
            DataInputStream dataInStream = new DataInputStream(
                new BufferedInputStream(input)
            )
        ){
            while(dataInStream.available() > 0){
                double d = dataInStream.readDouble();
                int i = dataInStream.readInt();
                String s = dataInStream.readUTF();
                System.out.println("d = " + d);
                System.out.println("i = " + i);
                System.err.println("s = " + s);
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }



    static void test4() throws IOException{
        try (var input = new Scanner(System.in)) {
            String sourceFile = null;
            String secretFile = null;
            var keyValue = 0;
            System.out.print("请输入源文件名：");
            sourceFile = input.nextLine();
            System.out.print("请输入加密文件名：");
            secretFile = input.nextLine();
            System.out.print("请输入密钥：");
            keyValue = input.nextInt();
            var srcFile = new File(sourceFile);
            var encFile = new File(secretFile);
            if( !srcFile.exists() ){
                System.out.println("源文件不存在");
                System.exit(0);
            }
            if( !encFile.exists() ){
                System.out.println("创建加密文件");
                encFile.createNewFile();
            }
            try(
                var fis = new FileInputStream(srcFile);
                var fos = new FileOutputStream(encFile);
            ){
                var dataOfFile = fis.read();
                while( dataOfFile != -1 ){
                    dataOfFile = dataOfFile ^ keyValue;
                    fos.write(dataOfFile);
                    dataOfFile = fis.read();
                }
            }
        }
    }
    public static void main(String[] args) throws FileNotFoundException, IOException {
        test1();
    }
}

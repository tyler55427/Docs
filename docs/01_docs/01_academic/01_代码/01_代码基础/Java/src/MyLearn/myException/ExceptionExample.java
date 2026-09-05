package MyLearn.myException;

public class ExceptionExample {  
      
    // 自定义异常类，用于存储额外的错误信息  
    static class CustomException extends RuntimeException {  
        private StackTraceElement customStackTraceElement;  
  
        public CustomException(String message, StackTraceElement customStackTraceElement) {  
            super(message);  
            this.customStackTraceElement = customStackTraceElement;  
        }  
  
        public StackTraceElement getCustomStackTraceElement() {  
            return customStackTraceElement;  
        }  
    }  
  
    public static void main(String[] args) {  
        try {  
            // 构造一个自定义的StackTraceElement对象  
            StackTraceElement element = new StackTraceElement("ErrorClass", "errorMethod", "ErrorFile.java", 42);  
            // 抛出一个自定义异常，并附带自定义的StackTraceElement  
            throw new CustomException("Custom exception occurred", element);  
        } catch (CustomException e) {  
            // 在catch块中捕获自定义异常并打印信息  
            System.out.println("Caught a custom exception:");  
            System.out.println("Exception message: " + e.getMessage());  
            // 获取并打印自定义的StackTraceElement信息  
            StackTraceElement customElement = e.getCustomStackTraceElement();  
            System.out.println("Error Class: " + customElement.getClassName());  
            System.out.println("Error Method: " + customElement.getMethodName());  
            System.out.println("Error File: " + customElement.getFileName());  
            System.out.println("Error Line: " + customElement.getLineNumber());  
        } finally {  
            // finally块中的代码总是会执行  
            System.out.println("Hello world!");  
        }  
    }  
}
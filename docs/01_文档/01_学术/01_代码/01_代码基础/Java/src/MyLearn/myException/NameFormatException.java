package MyLearn.myException;

public class NameFormatException extends RuntimeException {
    public NameFormatException(){

    }
    public NameFormatException(String message){
        super(message);
    }
}

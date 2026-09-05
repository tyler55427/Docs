package MyLearn.Interface_;


public interface Printable {
    public abstract void print(String message);

    public static void main(String[] args) {
        // 匿名对象，只调用一次
        // 不用继承，创建一个，直接重写
        Printable printer = new Printable() {
            @Override
            public void print(String message){
                System.out.println(message);
            }
        };
        printer.print("Hello world!");


        // button.setOnAction(new EventHandler<ActionEvent>(){
        //     @Override
        //     public void handle(ActioinEvent event){
        //         label.setText("点击")；
        //     }
        // })
    }
}

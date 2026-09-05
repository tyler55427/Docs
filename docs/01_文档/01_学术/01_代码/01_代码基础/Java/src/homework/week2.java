package homework;
import java.util.Scanner;
public class week2 {
    public static void main(String[] args) {
        System.out.println("Please input the value of: a,b,c ");
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();
        QuadraticEquation test = new QuadraticEquation(a,b,c);
        System.out.println("The discriminant is:  " + test.getDiscriminant());
        if(test.getDiscriminant()>=0){
            if(test.getDiscriminant()==0){
                System.out.println("x1 = x2 =" + test.getRoot1());
            }
            else{
                System.out.println("x1 = " + test.getRoot1() + "  " + "x2 = " + test.getRoot2());
            }
        }
        else{
            System.out.println("The equation has no root! ");
        }
        input.close();
    }
}


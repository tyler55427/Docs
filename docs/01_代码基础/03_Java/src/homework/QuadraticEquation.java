package homework;
public class QuadraticEquation{
    private    double a,b,c;
    public QuadraticEquation (double a,double b,double c){
        this.a=a;
        this.b=b;
        this.c=c;
    };
    public double getDiscriminant(){
        return b*b-4*a*c;
    }
    public double getterA(){
        return a;
    }
    public double getterB(){
        return b;
    }
    public double getterC(){
        return c;
    }
    public double getRoot1(){
        if ( getDiscriminant()<0 )  return 0;
        else {
            return (-b-Math.sqrt(getDiscriminant()))/2/a;
        }
    }
    public double getRoot2(){
        if ( getDiscriminant()<0 ) return 0;
        else {
            return (-b+Math.sqrt(getDiscriminant()))/2/a;
        }
    }
}

package com.java.zsu;
public class Square extends Shape{
    private double side;
    public Square(){

    }
    public Square(double side){
        this.side = side;
    }
    public double getSide(){
        return side;
    }
    public void setSide(double side){
        this.side = side;
    }
    public double getPerimeter(){
        return 4*side;
    }
    public double getArea(){
        return side*side;
    }
}

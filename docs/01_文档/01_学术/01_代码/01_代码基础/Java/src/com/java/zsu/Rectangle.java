package com.java.zsu;
public class Rectangle {
    public double length;
    public double width;
    public Rectangle(){

    }
    public Rectangle(double length,double width){
        this.length = length;
        this.width = width;
    }
    public double getLength(){
        return length;
    }
    public void setLength(double length){
        this.length = length;
    }
    public double getWidth(){
        return width;
    }
    public void setWidth(double width){
        this.width = width;
    }
}

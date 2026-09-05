package com.java.zsu;
public class Cuboid extends Rectangle{
    private double height;
    public Cuboid(){
        
    }
    public Cuboid(double length,double width,double height){
        super(length,width);
        this.height = height;
    }
    public double getHeight(){
        return height;
    }
    public void setHeight(double height){
        this.height = height;
    }
    public double volume(){
        return length*width*height;
    }
}

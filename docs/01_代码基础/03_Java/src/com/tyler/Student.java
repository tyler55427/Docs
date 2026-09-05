package com.tyler;

public class Student {
    String name;
    String id;
    double score;

    public Student(String name, String id, double score) {
        this.name = name;
        this.id = id;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public double getScore() {
        return score;
    }

    @Override
    public String toString(){
        return "Name: " + name + "  " +
        "Id: " + id + "  " +
        "Score" + score;
    }
}

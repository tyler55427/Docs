package homework;

import java.util.*;
import com.tyler.Student;
public class Array {
    public static void main(String[] args) {
        // Initialize the list of students
        List<Student> students = new ArrayList<>();
        students.add(new Student("Alice", "1001", 95));
        students.add(new Student("Bob", "1002", 85));
        students.add(new Student("Charlie", "1003", 75));
        students.add(new Student("David", "1004", 65));
        students.add(new Student("Eve", "1005", 55));
        students.add(new Student("Frank", "1006", 45));

        // Sort students by getScore() in descending order
        students.sort((s1, s2) -> Double.compare(s2.getScore(), s1.getScore()));

        // Print sorted students
        System.out.println("排序后");
        for (Student student : students) {
            System.out.println(student);
        }

        // Calculate average, highest, and lowest getScore()
        double totalscore = 0;
        double highestscore = Integer.MIN_VALUE;
        double lowestscore = Integer.MAX_VALUE;

        for (Student student : students) {
            totalscore += student.getScore();
            if (student.getScore() > highestscore) {
                highestscore = student.getScore();
            }
            if (student.getScore() < lowestscore) {
                lowestscore = student.getScore();
            }
        }

        double averagescore = (double) totalscore / students.size();
        System.out.printf("平均分: %.2f\n", averagescore);
        System.out.println("最高分: " + highestscore);
        System.out.println("最低分: " + lowestscore);

        // Count and calculate the percentage of each grade category
        int excellentCount = 0; // >= 90
        int goodCount = 0; // 80-89
        int averageCount = 0; // 70-79
        int passCount = 0; // 60-69
        int failCount = 0; // < 60

        for (Student student : students) {
            if (student.getScore() >= 90) {
                excellentCount++;
            } else if (student.getScore() >= 80) {
                goodCount++;
            } else if (student.getScore() >= 70) {
                averageCount++;
            } else if (student.getScore() >= 60) {
                passCount++;
            } else {
                failCount++;
            }
        }

        System.out.println("成绩等级");
        System.out.printf("优秀: %d (%.2f%%)\n", excellentCount, (double) excellentCount / students.size() * 100);
        System.out.printf("好: %d (%.2f%%)\n", goodCount, (double) goodCount / students.size() * 100);
        System.out.printf("平均: %d (%.2f%%)\n", averageCount, (double) averageCount / students.size() * 100);
        System.out.printf("通过: %d (%.2f%%)\n", passCount, (double) passCount / students.size() * 100);
        System.out.printf("不及格: %d (%.2f%%)\n", failCount, (double) failCount / students.size() * 100);
    }
}

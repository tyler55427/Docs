package homework;

import java.util.Comparator;
import java.util.List;

import com.tyler.Student;

public class stream {

    public static void main(String[] args) {
        List<Student> students = List.of(
                new Student("Alice", "001", 85),
                new Student("Bob", "002", 92),
                new Student("Charlie", "003", 78),
                new Student("David", "004", 65),
                new Student("Eve", "005", 59)
        );

        // 按分数从高到低排序并打印学生信息
        System.out.println("排序后:");
        students.stream()
                .sorted(Comparator.comparingDouble(Student::getScore).reversed())
                .forEach(System.out::println);

        // 计算平均成绩、最高分和最低分
        double averageScore = students.stream().mapToDouble(Student::getScore).average().orElse(0);
        double highestScore = students.stream().mapToDouble(Student::getScore).max().orElse(0);
        double lowestScore = students.stream().mapToDouble(Student::getScore).min().orElse(0);

        System.out.println("平均分："+averageScore);
        System.out.println("最高分："+highestScore);
        System.out.println("最低分："+lowestScore);
        int totalStudents = students.size();

        // 统计 "优秀" 学生人数
        long excellentCount = students.stream()
                                      .filter(student -> student.getScore() >= 90)
                                      .count();
        // 统计 "较好" 学生人数
        long goodCount = students.stream()
                                 .filter(student -> student.getScore() >= 80 && student.getScore() < 90)
                                 .count();
        // 统计 "平均" 学生人数
        long averageCount = students.stream()
                                    .filter(student -> student.getScore() >= 70 && student.getScore() < 80)
                                    .count();
        // 统计 "通过" 学生人数
        long passCount = students.stream()
                                 .filter(student -> student.getScore() >= 60 && student.getScore() < 70)
                                 .count();
        // 统计 "不及格" 学生人数
        long failCount = students.stream()
                                 .filter(student -> student.getScore() < 60)
                                 .count();

        // 输出统计结果
        System.out.println("分级：优秀   人数：" + excellentCount + "   百分比：" + (excellentCount / (double) totalStudents) * 100);
        System.out.println("分级：较好   人数：" + goodCount + "   百分比：" + (goodCount / (double) totalStudents) * 100);
        System.out.println("分级：平均   人数：" + averageCount + "   百分比：" + (averageCount / (double) totalStudents) * 100);
        System.out.println("分级：通过   人数：" + passCount + "   百分比：" + (passCount / (double) totalStudents) * 100);
        System.out.println("分级：不及格 人数：" + failCount + "   百分比：" + (failCount / (double) totalStudents) * 100);

    }
}
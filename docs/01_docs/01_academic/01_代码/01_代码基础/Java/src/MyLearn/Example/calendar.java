package MyLearn.Example;

import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;
import java.util.Scanner;

public class calendar {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        var input = new Scanner(System.in);
        System.out.println("请输入一个年份 ");
        var year = input.nextInt();
        for(var month = 1;month<=12;++month){
            var dates = LocalDate.of(year,month,1);
            String monthName = dates.getMonth().getDisplayName(TextStyle.FULL, Locale.getDefault());
            var daysOfMonth = dates.lengthOfMonth();
            System.out.println(year + " 年    " + monthName);
            System.out.println("---------------------");
            System.out.printf("%3s%3s%3s%3s%3s%3s%3s%n", "一","二","三","四","五","六","日");
            var dayOfWeek = dates.getDayOfWeek().getValue();
            for(var i=2;i<=dayOfWeek;++i)
                System.out.printf("%4s"," ");
                for(var i = 1;i<=daysOfMonth;++i){
                    System.out.printf("%4d",i);
                    if((dayOfWeek + i - 1)%7 == 0)
                        System.out.println();
            }
            System.out.printf("%n%n");
        }
    }
}

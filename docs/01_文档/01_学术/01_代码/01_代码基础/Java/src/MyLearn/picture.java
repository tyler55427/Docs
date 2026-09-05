package MyLearn;

import javax.swing.*;

public class picture {
    public static void main(String[] args) {
        JMenuBar jMB = new JMenuBar();
        JMenu j1 = new JMenu("File");
        JMenu j2 = new JMenu("Edit");
        JMenuItem g1 = new JMenuItem("SetSize");
        JMenuItem g2 = new JMenuItem("SetContent");
        j2.add(g1);
        j2.add(g2);
        jMB.add(j1);
        jMB.add(j2);

        JFrame jF = new JFrame();
        jF.setSize(603,680);
        jF.setTitle("Test_windows");
        jF.setAlwaysOnTop(true);
        jF.setLocationRelativeTo(null);
        jF.setJMenuBar(jMB);
        jF.setDefaultCloseOperation(3);
        jF.setVisible(true);
        
    }
}

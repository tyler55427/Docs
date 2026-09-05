package homework;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class StudentDatabaseOperations {
    private static final String URL = "jdbc:mysql://localhost:3306/";
    private static final String USER = "root";  // 请根据你的MySQL配置更改
    private static final String PASSWORD = "123456";  // 请根据你的MySQL配置更改
    private static final String DB_NAME = "school";
    private static final String TABLE_NAME = "students";

    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection(URL, USER, PASSWORD)) {
            // 创建数据库
            createDatabase(connection);

            // 连接到具体的数据库
            try (Connection dbConnection = DriverManager.getConnection(URL + DB_NAME, USER, PASSWORD)) {
                // 创建表
                createTable(dbConnection);

                // 插入数据
                insertData(dbConnection, "Alice", "001", 85);
                insertData(dbConnection, "Bob", "002", 92);
                insertData(dbConnection, "Charlie", "003", 78);
                insertData(dbConnection, "David", "004", 65);
                insertData(dbConnection, "Eve", "005", 59);

                // 更新数据
                updateData(dbConnection, 1, "Alice", "001", 90);

                // 删除数据
                deleteData(dbConnection, 5);

                // 查询数据
                queryData(dbConnection);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void createDatabase(Connection connection) throws SQLException {
        String createDatabaseSQL = "CREATE DATABASE IF NOT EXISTS " + DB_NAME;
        try (Statement statement = connection.createStatement()) {
            statement.execute(createDatabaseSQL);
        }
    }

    private static void createTable(Connection connection) throws SQLException {
        String createTableSQL = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (" +
                "id INT PRIMARY KEY AUTO_INCREMENT, " +
                "name VARCHAR(50), " +
                "student_id VARCHAR(50), " +
                "score DOUBLE)";
        try (Statement statement = connection.createStatement()) {
            statement.execute(createTableSQL);
        }
    }

    private static void insertData(Connection connection, String name, String studentId, double score) throws SQLException {
        String insertSQL = "INSERT INTO " + TABLE_NAME + " (name, student_id, score) VALUES (?, ?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, studentId);
            preparedStatement.setDouble(3, score);
            preparedStatement.executeUpdate();
        }
    }

    private static void updateData(Connection connection, int id, String name, String studentId, double score) throws SQLException {
        String updateSQL = "UPDATE " + TABLE_NAME + " SET name = ?, student_id = ?, score = ? WHERE id = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(updateSQL)) {
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, studentId);
            preparedStatement.setDouble(3, score);
            preparedStatement.setInt(4, id);
            preparedStatement.executeUpdate();
        }
    }

    private static void deleteData(Connection connection, int id) throws SQLException {
        String deleteSQL = "DELETE FROM " + TABLE_NAME + " WHERE id = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(deleteSQL)) {
            preparedStatement.setInt(1, id);
            preparedStatement.executeUpdate();
        }
    }

    private static void queryData(Connection connection) throws SQLException {
        String querySQL = "SELECT * FROM " + TABLE_NAME;
        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(querySQL)) {
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                String studentId = resultSet.getString("student_id");
                double score = resultSet.getDouble("score");
                System.out.printf("ID: %d, Name: %s, Student ID: %s, Score: %.2f%n", id, name, studentId, score);
            }
        }
    }
}

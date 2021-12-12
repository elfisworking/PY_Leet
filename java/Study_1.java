package java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import org.w3c.dom.Node;

public class Study_1 {
    // try-with-resources 
    // 自动的关闭资源
    // 可以替代try-catch-finally
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(new File("test.txt"))) {
            while(scanner.hasNext()){
                System.out.println(scanner.nextLine());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

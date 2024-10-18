package com.example;

import java.awt.Desktop;
import java.io.File;
import java.io.IOException;

public class OpenHtml {
    public static void main(String[] args) {
        if (args.length > 0) {
            try {
                File htmlFile = new File(args[0]);
                Desktop.getDesktop().browse(htmlFile.toURI());
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            System.out.println("No file path provided.");
        }
    }
}

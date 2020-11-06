package com.company;
 
import java.util.Random;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
            String[] text;
            Scanner scanner = new Scanner(System.in);
 
            while(true) {
                System.out.println("Wpisz swoje imie i nazwisko:");
                text = removePolishLetters(scanner.nextLine()).split(" ");
 
                if(text.length < 2 || text.length > 2) {
                        System.out.println("BLAD! Wpisz poprawne dane!");
                    continue;
            }
 
                break;
        }
 
            int randomNumber = new Random().nextInt(10) + 1;
            System.out.println("Witaj " + text[0].substring(0, 1).toUpperCase() + text[1].substring(0, 1).toUpperCase() + text[1].substring(1, text[1].length()).toLowerCase() + "! Aby ukonczyc weryfikacje, podaj wynik pierwiastka z " + randomNumber);
 
                double wynik;
            while(true) {
                try {
                                System.out.print("Tu wpisz wynik: ");
                                wynik = Double.parseDouble(scanner.next());
                                break;
                        }
                catch(Exception ex) {
                        System.out.println("BLAD! Podana wartosc musi byc liczba! Sprobuj ponownie");
                        }
                }
 
 
            String wynikString = String.format("%.2f%n", wynik);
            wynik = Double.parseDouble(wynikString);
 
            while(wynik != getSquareRootResult(randomNumber)) {
                        System.out.println("To nie jest poprawny wynik, sprobuj ponownie");
                        System.out.print("Tu wpisz wynik: ");
 
                        wynik = scanner.nextDouble();
                }
 
            System.out.println("Weryfikacja zakonczona powodzeniem! W ramach nagrody dajemy Ci dostep do kalulatora w konsoli!");
 
 
            while(true) {
                        System.out.println("------------ [KALKULATOR] ------------");
                        System.out.println("* Dostepne opcje kalkulatora:        *");
                        System.out.println("*                                    *");
                        System.out.println("* 1. Dodawanie                       *");
                        System.out.println("* 2. Odejmowanie                     *");
                        System.out.println("* 3. Dzielenie                       *");
                        System.out.println("* 4. Mnozenie                        *");
                        System.out.println("------------ [KALKULATOR] ------------");
 
                        int option;
 
                        while (true) {
                                try {
                                        System.out.print("* Wpisz interesującą Cię opcje: ");
                                        option = Integer.parseInt(scanner.next());
                                        break;
                                } catch (Exception ex) {
                                        System.out.println("BŁĄD! Podana wartość musi być liczbą! Spróbuj ponownie");
                                        continue;
                                }
                        }
 
 
                        switch (option) {
                                case 1: case 2: case 3: case 4:
                                        break;
                                default:
                                        System.out.println("BŁĄD! Podana opcja nie jest dostępna, spróbuj ponownie!");
                                        continue;
 
                        }
 
                        while(true) {
                                double firstNumber;
                                double secondNumber;
 
                                while (true) {
                                        try {
                                                System.out.println("Podaj pierwsza liczbe: ");
                                                firstNumber = Double.parseDouble(scanner.next());
 
                                                System.out.println("Podaj druga liczbe: ");
                                                secondNumber = Double.parseDouble(scanner.next());
                                                break;
                                        } catch (Exception ex) {
                                                System.out.println("BŁĄD! Podana wartość musi być liczbą! Spróbuj ponownie");
                                                continue;
                                        }
                                }
 
 
                                switch (option) {
                                        case 1:
                                                System.out.println("Wynik dodawania " + firstNumber + " + " + secondNumber + " = " + (firstNumber + secondNumber));
                                                break;
                                        case 2:
                                                System.out.println("Wynik odejmowania " + firstNumber + " - " + secondNumber + " = " + (firstNumber - secondNumber));
                                                break;
                                        case 3:
                                                System.out.println("Wynik dzielenia " + firstNumber + " : " + secondNumber + " = " + (firstNumber / secondNumber));
                                                break;
                                        case 4:
                                                System.out.println("Wynik mnozenia " + firstNumber + " * " + secondNumber + " = " + (firstNumber * secondNumber));
                                                break;
                                }
 
                                String opt;
                                while(true) {
                                        System.out.println("Co chcesz zrobic?");
                                        System.out.println("e - wyjsc z programu");
                                        System.out.println("w - wrocic do wyboru dostepnych opcji");
                                        System.out.println("p - wpisac ponownie liczby");
 
                                        System.out.print("Opcja: ");
                                        opt = scanner.next();
 
                                        if(opt.equals("e") || opt.equals("E")) {
                                                System.exit(0);
                                                break;
                                        }
 
                                        else if(opt.equals("w") || opt.equals("W")) {
                                                //wybor
                                                break;
                                        }
 
                                        else if(opt.equals("p") || opt.equals("P")) {
                                                //wybierz ponownie
                                                break;
                                        }
 
                                        else {
                                                System.out.println("BLAD! Podana opcja nie istnieje, sprobuj ponownie!");
                                                continue;
                                        }
                                }
 
                                if(opt.equals("w") || opt.equals("W"))
                                        break;
                        }
 
 
 
 
                }
 
 
 
 
    }
 
    public static double getSquareRootResult(int number) {
        String numberString = String.format("%.2f%n", Math.sqrt(number));
 
        return Double.parseDouble(numberString);
        }
 
        public static void clearScreen() {
                System.out.print("\033[H\033[2J");
 
                System.out.flush();
        }
 
        public static void waitThenClearScreen(String text, int number) {
        try {
                System.out.println(text);
                Thread.sleep(number);
 
                Runtime.getRuntime().exec("clear");
                }
 
        catch(Exception ex) {
 
                }
        }
 
        public static String removePolishLetters(String text) {
        String[] polishLetters = {"ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż", "Ą", "Ć", "Ę", "Ł", "Ń", "Ó", "Ś", "Ź", "ż"};
        String[] letters = {"a", "c", "e", "l", "n", "o", "s", "z", "z", "A", "C", "E", "L", "N", "O", "S", "Z", "Z"};
 
        for(int i = 0; i< polishLetters.length; i++) {
                text = text.replace(polishLetters[i], letters[i]);
                }
 
        return text;
        }
 
}
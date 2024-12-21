import java.util.Scanner;

public class PasswordManager {
    private final APIClient apiClient = new APIClient();

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Password Manager");
            System.out.println("1. View Passwords");
            System.out.println("2. Add Password");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (choice) {
                case 1 -> viewPasswords();
                case 2 -> addPassword(scanner);
                case 3 -> {
                    System.out.println("Exiting...");
                    return;
                }
                default -> System.out.println("Invalid option. Please try again.");
            }
        }
    }

    private void viewPasswords() {
        System.out.println("Fetching passwords...");
        String response = apiClient.getPasswords();
        System.out.println("Passwords: " + response);
    }

    private void addPassword(Scanner scanner) {
        System.out.print("Enter service name: ");
        String service = scanner.nextLine();
        System.out.print("Enter password: ");
        String password = scanner.nextLine();
        apiClient.addPassword(service, password);
    }
}

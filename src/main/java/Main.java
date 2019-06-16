import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static Manager m = new Manager();

    public static void main(String[] args) {
        m.setDB(); //maintain all first!
        if (args.length > 0){
            String command = args[0];
            switch (command) {
                case "new":
                    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                    try {
                        System.out.println("Enter title:\n");
                        String title = br.readLine();
                        System.out.println("Enter body:\n");
                        String body = br.readLine();
                        System.out.println("Enter tags separated by comma:\n");
                        String tags = br.readLine();
                        m.createNote(new Note(title, body, tags));
                    } catch (IOException e) {
                        e.printStackTrace();
                    } finally {
                        try {
                            br.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                    break;
                case "list":
                    if (args[1] != null) {
                        m.printLastNotes(Integer.parseInt(args[1]));
                    } else {
                        System.out.println("Showing 4 as default number of notes");
                        m.printLastNotes(4);
                    }
                    break;
                case "contents":
                    if (args[1] != null) {
                        m.printLastNotes(Integer.parseInt(args[1]));
                    } else {
                        System.out.println("Showing 10 as default number of contents");
                        m.printLastNotes(10);
                    }
                    break;
                default:
                    System.out.println("Use arguments:\nnew\nlist\ncontents");
                    break;
            }
        } else {
            System.out.println("Use arguments:\nnew\nlist\ncontents");
        }
    }
}

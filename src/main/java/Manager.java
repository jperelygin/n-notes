import java.util.ArrayList;

public class Manager {

    Database db = null;

    public void setDB(){
        // Use it to initialize database
        this.db = new Database();
    }

    public void printNoteById(int i){
        System.out.println(db.getNoteById(i));
    }

    public void printLastNotes(int i){
        ArrayList<Note> array = db.getLastNotes(i);
        for(Note note : array){
            System.out.println(note.toString() + "\n");
        }
    }

    public void printContents(int i){
        ArrayList<String> array = db.getContents(i);
        for(String s : array){
            System.out.println(s);
        }
    }

    public void createNote(Note note) {
        db.createNote(note);
    }

}

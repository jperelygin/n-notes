import java.util.ArrayList;

public interface IDatabase {

    void createNote(Note note);

    Note getNoteById(int id);

    ArrayList<Note> getLastNotes(int number);

    ArrayList<String> getContents(int number);
}

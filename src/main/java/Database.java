import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;

public class Database implements IDatabase {

    private String SQL_ADRESS;
    private Connection conn = null;

    Database(){
        setConn();
        getSQLAdress();
    }

    public void createNote(Note note) {
        String insert = "INSERT INTO Notes(Date, Title, Body, Tags) VALUES(?,?,?,?)";
        try{
            PreparedStatement prstm = conn.prepareStatement(insert);
            prstm.setString(1, note.getDate());
            prstm.setString(2, note.getTitle());
            prstm.setString(3, note.getBody());
            prstm.setString(4, note.getTags().toString()); // Will it work with SELECT?
            prstm.executeUpdate();
        }catch (SQLException e){
            e.printStackTrace();
        }
    }

    public Note getNoteById(int id) {
        Note note = null;
        String query = "SELECT (Id, Date, Title, Body, Tags) FROM Notes WHERE Id = ?";
        try{
            PreparedStatement prstm = conn.prepareStatement(query);
            prstm.setInt(1, id);
            ResultSet result = prstm.executeQuery();
            note.setDate(result.getString("Date"));
            note.setTitle(result.getString("Title"));
            note.setBody(result.getString("Body"));
            note.setTags(result.getString("Tags"));
        }catch (SQLException e){
            e.printStackTrace();
        }catch (NullPointerException e){
            e.printStackTrace();
        }finally {
            if (note == null){
                System.out.println(String.format("there is no such note with %s id", id));
            }
        }
        return note;
    }

    public ArrayList<Note> getLastNotes(int numberOfNotes) {
        ArrayList<Note> noteArray = null;
        String query = "SELECT * FROM(SELECT (Id, Date, Title, Body, Tags) FROM Notes ORDER BY Id DESC LIMIT ?) t1 ORDER BY t1.Id";
        try{
            PreparedStatement prstm = conn.prepareStatement(query);
            prstm.setInt(1, numberOfNotes);
            ResultSet result = prstm.executeQuery();
            while (result.next()) {
                Note note = new Note();
                note.setDate(result.getString("Date"));
                note.setTitle(result.getString("Title"));
                note.setBody(result.getString("Body"));
                note.setTags(result.getString("Tags"));
                noteArray.add(note);
            }
        }catch (SQLException e){
            e.printStackTrace();
        }catch (NullPointerException e){
            e.printStackTrace();
        }finally {
            if (noteArray == null){
                System.out.println("Something went wrong with getting last notes!");
            }
        }
        return noteArray;
    }

    public ArrayList<String> getContents(int numberOfNotes) {
        ArrayList<String> contents = null;
        String query = "SELECT * FROM(SELECT (Id, Date, Title) FROM Notes ORDER BY Id DESC LIMIT ?) t1 ORDER BY t1.Id";
        try{
            PreparedStatement prstm = conn.prepareStatement(query);
            prstm.setInt(1, numberOfNotes);
            ResultSet result = prstm.executeQuery();
            while (result.next()) {
                contents.add(result.getString("id") + "\t" +
                        result.getString("Date") + "\t" +
                        result.getString("Title"));
            }
        }catch (SQLException e){
            e.printStackTrace();
        }catch (NullPointerException e){
            e.printStackTrace();
        }finally {
            if (contents == null){
                System.out.println("Something went wrong with getting content!");
            }
        }
        return contents;
    }

    private void getSQLAdress(){
        // Read from resource file
        try{
            String fileName = "DatabaseAddress.txt"; //TODO: Try to avoid this! Refactor! It is not secure
            ClassLoader classLoader = ClassLoader.getSystemClassLoader();
            File file = new File(classLoader.getResource(fileName).getFile());
            FileReader fr = new FileReader(file);
            SQL_ADRESS = new BufferedReader(fr).readLine(); //TODO: Refactor into xml with tags! Or json config
        }catch (IOException e){
            e.printStackTrace();
        }catch (NullPointerException e){
            e.printStackTrace();
        }
    }

    private Connection makeConnection(){
        Connection connection = null;
        try{
            String url = "jdbc:sqlite:" + SQL_ADRESS;
            connection = DriverManager.getConnection(url);
        } catch (SQLException e){
            e.printStackTrace();
        }
        return connection;
    }

    private void setConn(){
        this.conn = makeConnection();
    }

    private void closeConnection(Connection connection){
        try {
            connection.close();
        } catch (SQLException e){
            e.printStackTrace();
        }
        this.conn = null;
    }

}

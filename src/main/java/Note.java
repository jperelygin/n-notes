import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;

public class Note {

    private String date;
    private String title;
    private String body;
    private ArrayList<String> tags;

    Note(){

    }

    Note(String title, String body, String tags){
        this.title = title;
        this.body = body;
        if(!tags.equals("")){
            String[] tagsArray = tags.split(",");
            try {
                this.tags.addAll(Arrays.asList(tagsArray));
            } catch (NullPointerException e){
                e.printStackTrace();
            }
        }
        setNewNoteDate();
    }

    public void setBody(String body){
        this.body = body;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setDate(String date){
        this.date = date;
    }

    public void setTags(String tags){
        try{
            String[] ArrayTags = tags.split(",");
            this.tags.addAll(Arrays.asList(ArrayTags));
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public void setNewNoteDate(){
        Date date = new Date();
        DateFormat df = new SimpleDateFormat("dd.MM.yyyy, HH:mm");
        this.date = df.format(date);
    }

    public void setTag(String newTag) {
        boolean thereIsNoSuchTag = true;
        for (String tag : this.tags) {
            if (tag.equals(newTag)) {
                thereIsNoSuchTag = false;
            }
        }
        if (thereIsNoSuchTag) {
            tags.add(newTag);
        }
    }

    public String getTitle() {
        return title;
    }

    public String getDate() {
        return date;
    }

    public String getBody() {
        return body;
    }

    public ArrayList<String> getTags(){
        return tags;
    }

    @Override
    public String toString(){
        return (date + "\t" + title + "\n" + body + "\n" + tags);
    }

}

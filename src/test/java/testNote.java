import org.junit.Assert;
import org.junit.Test;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class testNote {

    @Test
    public void testDate(){
        Note note = new Note();
        note.setNewNoteDate();
        System.out.print(note.getDate());
        DateFormat df = new SimpleDateFormat();
        Date date = new Date();
        Assert.assertEquals(df.format(date), note.getDate());
    }

}

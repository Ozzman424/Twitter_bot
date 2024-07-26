import java.io.FileReader;
import java.util.List;
import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;
import java.util.Properties;
import java.io.IOException;

class Tweet {
    String user;
    String text;
    String created_at;
}

public class ProcessTweets {

    public static void main(String[] args) {
        List<Tweet> tweets = fetchTweets();
        for (Tweet tweet : tweets) {
            sendEmail(tweet);
        }
    }

    private static List<Tweet> fetchTweets() {
        Gson gson = new Gson();
        try {
            FileReader reader = new FileReader("fetched_tweets.json");
            Type tweetListType = new TypeToken<List<Tweet>>(){}.getType();
            List<Tweet> tweets = gson.fromJson(reader, tweetListType);
            reader.close();
            return tweets;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static void sendEmail(Tweet tweet) {
        String to = "your_email@example.com";
        String from = "your_email@example.com";
        String host = "smtp.gmail.com";

        Properties properties = System.getProperties();
        properties.setProperty("mail.smtp.host", host);
        properties.setProperty("mail.smtp.port", "587");
        properties.setProperty("mail.smtp.auth", "true");
        properties.setProperty("mail.smtp.starttls.enable", "true");

        Session session = Session.getDefaultInstance(properties, new Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication("your_email@example.com", "your_email_password");
            }
        });

        try {
            MimeMessage message = new MimeMessage(session);
            message.setFrom(new InternetAddress(from));
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
            message.setSubject("New Tweet from " + tweet.user);
            message.setText("User: " + tweet.user + "\nTweet: " + tweet.text + "\nDate: " + tweet.created_at);

            Transport.send(message);
            System.out.println("Email sent successfully for tweet: " + tweet.text);
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }
}

import java.util.Base64;
import java.util.Random;

public class answerstoken {
    public static void main(String args[]) {
        int length = 42;
        int userId = 5; // Carl userId used for XOR
        long start = Long.parseLong("1743833172384");
        long stop = Long.parseLong("1743833173907");
        
        for (long seed = start; seed < stop; seed++) {
            String token = createToken(length, seed, userId);
            System.out.println(token);
        }
    }

    public static String createToken(int length, long seed, int userId) {
        String CHARSET = "abcdefghijklmnopqrstuvwxyz" +
                         "abcdefghijklmnopqrstuvwxyz".toUpperCase() +
                         "1234567890" +
                         "!@#$%^&*()";

        Random random = new Random(seed);
        StringBuilder sb = new StringBuilder();
        byte[] encbytes = new byte[length];

        for (int i = 0; i < length; i++) {
            sb.append(CHARSET.charAt(random.nextInt(CHARSET.length())));
        }

        byte[] bytes = sb.toString().getBytes();

        for (int i = 0; i < bytes.length; i++) {
            encbytes[i] = (byte)(bytes[i] ^ (byte)userId);
        }

        return Base64.getUrlEncoder().withoutPadding().encodeToString(encbytes);
    }
}

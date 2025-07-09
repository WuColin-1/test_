import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class TungTungSahur {
    public static int repeat_count(String a){ 
        if (a.length()==0) return 0;
        int Count=1;
        for (int i = 0; i < a.length()-1; i++) {
            if(a.charAt(i)==a.charAt(i+1))Count++;
            else return Count;
        }
        return Count;
    }
    public static int repeat_part(String a){
        int Count=1;
        for (int i = 0; i < a.length()-1; i++) {
            if(a.charAt(i)!=a.charAt(i+1)) Count++;
        }
        return Count;
    }
    public static boolean judge(String a, String b){
        if ((a.length()==0 && b.length()==0) || a==b || (repeat_count(a)>1 && repeat_count(b)-repeat_count(a)==2 && repeat_part(a)==1 && repeat_part(b)==1)){
            return true;
        }
        else if (repeat_count(a)>repeat_count(b) || repeat_count(b)-repeat_count(a)>=2 || a.charAt(0)!=b.charAt(0) || repeat_part(a)!=repeat_part(b)){
            return false;
        }
        else{
            return judge(a.substring(repeat_count(a)),b.substring(repeat_count(b)));
        }
    }
    public static void main(String[] agrs)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int Count=Integer.parseInt(br.readLine());
        for (int i = 0; i < Count; i++) {
            String Str_1=br.readLine();
            String Str_2=br.readLine();
            if(Str_1==Str_2){
                System.out.println("YES");
                continue;
            }else if(repeat_part(Str_1)!=repeat_part(Str_2)){
                System.out.println("NO");
                continue;
            }
            if (judge(Str_1 , Str_2)) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}
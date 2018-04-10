import java.util.Scanner;

public class MinSteps {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int x = in.nextInt();
        System.out.println(getMinSteps(0,x));

    }

    //计算最少步数
    public static int getMinSteps(int f, int x)
    {

        x = java.lang.Math.abs(x);
        int time = 0;
        int f1 = 0,f2 = 0;
        int long1,long2;
        f ++;
        time ++;
        while(4*f < x){
            if(2*f >x)
                break;
            f = 2*f;
            time++;
        }
        if((f1 = 2*f) >x && isBeyond(f1)){
            long1 = f1 - x;
            long2 = long1/2;
            if((f2 = 2*(f-long2)) <= x){
                time = time+long2 + 1;
            }
        }else{
            f1 = 2*f;
            long1 = x - f1;
            long2 = long1/2;
            f2 = 2*(f+long2);
            time = time+long2+1;
        }
        if(x % 2 != 0)
            time++;
        return time;
    }
    public static boolean isBeyond(int f){
        if(f<0 || f>100000){
            return false;
        }else{
            return true;
        }
    }
}

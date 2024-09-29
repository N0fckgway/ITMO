import java.util.Random;
import java.lang.Math;
public class lab1 {
	public static StringBuilder PrintMatrix(double[][] matrix) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i <= 14; i++){
			for (int j = 0; j <= 13; j++){
				sb.append(String.format("%8.2f", matrix[i][j]));
			}
		sb.append("\n");
		}
	return sb;
	}

	public static void main(String[] args){
		int[] z = new int[15];
		Random rand = new Random();
		double[] x = new double[14];
		for (int i = 0; i <= 14; i++)
		{
			z[i] = (int) (18 - i);
		}
		for (int j = 0; j <= 13; j++)
		{
			x[j] = rand.nextDouble(-10.0, 4.0);
		}
		double [][] z1 = new double[15][14];
		for (int i = 0; i <= 14; i++) {
			for (int j = 0; j <= 13; j++){
				z1[i][j] = CalcElem(z[i], x[j]);
			}
		}
	System.out.println(PrintMatrix(z1));
}
		

	
	

	public static double CalcElem(int zi, double x) {
        	if (zi == 4)
		{
			 return Math.log(Math.pow(Math.tan((Math.pow(2.0 * x, 2) - 1.0) / 4.0), 2));
       		}		 	
		else if (zi == 5 || zi == 7 || zi == 8 || zi == 9 || zi == 0 || zi == 12 || zi ==  15)
		{
       	   		return Math.cos(Math.asin(Math.pow((x - 3.0) / 14.0, 2)));
        	}

        	else 
		{
			return Math.pow((1 - Math.sin(Math.log(Math.acos((x - 3.0) / 14.0)))) / 2.0, 3);
		}


       }
		

}


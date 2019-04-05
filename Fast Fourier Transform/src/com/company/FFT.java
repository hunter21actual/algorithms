package com.company;

import java.util.ArrayList;

public class FFT {

    private Complex complex = new Complex(0,0);
    private FFTUtility fftUtility = new FFTUtility();

    public Complex[] fastFourierTransform(ArrayList<Complex> arr, boolean inversion){

        Complex[] newArray = fftUtility.arrayAfterIndexBitReversal(arr);
        int arrayListLength = arr.size();
        int flag = (inversion == true) ? 1 : 0;


        int[] x = {-1, 1};

        int limit = ((int)(Math.log(arrayListLength) / Math.log(2))) + 1;
        for(int i = 1; i < limit; ++i){

            int stepSize = (int)Math.pow(2, i);

            Complex Wm = new Complex(Math.cos(2 * Math.PI * x[flag] / stepSize),
                    Math.sin(2 * Math.PI * x[flag] / stepSize));

            for(int j = 0; j < arrayListLength; j += stepSize){

                Complex omega = new Complex(1,0);
                for(int k = 0; k < stepSize/2; ++k){
                    Complex t = complex.multiply(omega, newArray[j + k + (stepSize/2)]);
                    Complex u = newArray[j + k];
                    newArray[j + k] = complex.add(u, t);
                    newArray[j + k + (stepSize/2)] = complex.subtract(u, t);
                    omega = complex.multiply(omega, Wm);

                }
            }
        }

        if(inversion){
            for(int i = 0; i < newArray.length; ++i){
                newArray[i].setReal(newArray[i].getReal()/arrayListLength);
                newArray[i].setImag(newArray[i].getImag()/arrayListLength);
            }
        }

        for(int i = 0; i < newArray.length; ++i) {
            newArray[i].setReal((double) Math.round(newArray[i].getReal() * 100) / 100);
            newArray[i].setImag((double) Math.round(newArray[i].getImag() * 100) / 100);
        }

        return newArray;

    }
}

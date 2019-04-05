package com.company;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {

        ArrayList<Complex> arr = new ArrayList<>();
        for(int i = 0; i < 8; ++i)
            arr.add(new Complex(i+1, 0));

        FFT fft = new FFT();
        Complex[] res = fft.fastFourierTransform(arr, false);

        for(int i = 0; i < res.length; ++i)
            System.out.println(res[i].getReal() + " + " + res[i].getImag() + "j");

        System.out.println("\n*************************\n");

        ArrayList<Complex> inv = new ArrayList<>();
        for(int i = 0; i < res.length; ++i)
            inv.add(new Complex(res[i].getReal(), res[i].getImag()));

        Complex[] back = fft.fastFourierTransform(inv, true);
        for(int i = 0; i < back.length; ++i)
            System.out.println(back[i].getReal() + " + " + back[i].getImag() + "j");

    }
}

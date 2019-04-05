package com.company;

import java.util.ArrayList;

public class FFTUtility {

    public boolean isPowerOfTwo(long Number){
        return ((Number & (Number - 1)) == 0);
    }

    public int nextHigherPowerOfTwo(long Number){

        int i = 0;
        while(Number > Math.pow(2, i))
            i++;

        return i;
    }

    public int bitReversal(int arrayIndex, int bits){

        if(arrayIndex == 0)
            return arrayIndex;

        int reversedArrayIndex = 0;
        for(int i = 0; i < bits; ++i) {
            reversedArrayIndex <<= 1;
            if (arrayIndex % 2 != 0)
                reversedArrayIndex++;
            arrayIndex >>= 1;
        }

        return reversedArrayIndex;
    }

    public Complex[] arrayAfterIndexBitReversal(ArrayList<Complex> arr){

        int bits;
        int newArrayLength;
        int arrayListLength = arr.size();

        if(isPowerOfTwo(arrayListLength)){
            newArrayLength = arrayListLength;
            bits = (int)(Math.log(arrayListLength) / Math.log(2));
        }

        else{
            bits = nextHigherPowerOfTwo(arrayListLength);
            newArrayLength = (int)Math.pow(2, bits);

            //Zero padding is required for an array whose length is not a power of 2
            for(int i = 0; i < newArrayLength - arrayListLength; ++i)
                arr.add(new Complex(0,0));

        }

        Complex[] newArray = new Complex[newArrayLength];
        for(int i = 0; i < newArrayLength; ++i)
            newArray[bitReversal(i, bits)] = arr.get(i);

        return newArray;

    }

}

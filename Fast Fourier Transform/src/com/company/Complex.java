package com.company;

public class Complex {

    private double real;
    private double imag;

    public Complex(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }

    public void setReal(double real) {
        this.real = real;
    }

    public void setImag(double imag) {
        this.imag = imag;
    }

    public double getReal() {
        return real;
    }

    public double getImag() {
        return imag;
    }

    public Complex add(Complex a, Complex b){
        return new Complex(a.real + b.real,a.imag + b.imag);
    }

    public Complex subtract(Complex a, Complex b){
        return new Complex(a.real - b.real,a.imag - b.imag);
    }

    public Complex multiply(Complex a, Complex b){
        return new Complex(a.real*b.real - a.imag*b.imag,a.real*b.imag + a.imag*b.real);
    }
}

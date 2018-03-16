// Density and Priority Calculations
int arr[5][6] = {{80,60,30,2,3,1},{90,50,20,1,3,2},{30,20,10,3,2,1},{80,50,10,2,1,3},{90,70,60,3,1,2}};

void setup() {
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(1, OUTPUT);
}

void funk(int ir, int iy, int ig, int r1, int r2, int del)
{
    // REST ARE RED
    digitalWrite(r1, HIGH);
    digitalWrite(r2, HIGH);
    //GREEN
    digitalWrite(ig, HIGH);
    delay(del);
    digitalWrite(ig, LOW);
    delay(10);

    //YELLOW
    digitalWrite(iy, HIGH);
    delay(del);
    digitalWrite(iy, LOW);
    delay(10);
    
    //RED
    digitalWrite(ir, HIGH);
    delay(del);
    digitalWrite(ir, LOW);
    delay(10);

    digitalWrite(r1, LOW);
    digitalWrite(r2, LOW);
}

void toggle()
{
    for(int i = 1; i <= 9; ++i){
        digitalWrite(i, HIGH);
    }
    
    delay(100);

    for(int i = 1; i <= 9; ++i){
        digitalWrite(i, LOW);
    }
    delay(100);
}

// Signal to LED Mapping
// signal 1 = 3,2,1
// signal 2 = 6,5,4
// signal 3 = 9,8,7

void loop() {
  for(int i = 0; i < 5; ++i){
    
    //Priority 1
    if(arr[i][3] == 3){
      funk(9,8,7,6,3,arr[i][0]*100);
    }
    else if(arr[i][3] == 2){
      funk(6,5,4,9,3,arr[i][0]*100);
    }
    else{
      funk(3,2,1,6,9,arr[i][0]*100);
    }
  
    //Priority 2
    if(arr[i][4] == 3){
      funk(9,8,7,6,3,arr[i][1]*100);
    }
    else if(arr[i][4] == 2){
      funk(6,5,4,9,3,arr[i][1]*100);
    }
    else{
      funk(3,2,1,6,9,arr[i][1]*100);
    }    
  
    //Priority 3
    if(arr[i][5] == 3){
      funk(9,8,7,3,6,arr[i][2]*100);
    }
    else if(arr[i][5] == 2){
      funk(6,5,4,9,3,arr[i][2]*100);
    }
    else{
      funk(3,2,1,6,9,arr[i][2]*100);
    }
  }

  for(int i = 0; i < 10; ++i)
    toggle();   
}

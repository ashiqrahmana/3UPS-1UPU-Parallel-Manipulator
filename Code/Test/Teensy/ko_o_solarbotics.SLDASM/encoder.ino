// ENCODER 0
void enAUpdate0(){
  A[0] = !A[0];
  if (A[0] == 1){
    if (A[0] == B[0])
      Counts[0] += 1;
    else if (A[0] != B[0])
      Counts[0] -= 1;
  }
}

void enBUpdate0(){
  B[0] = !B[0];
  if (B[0] == 1){
    if (A[0] != B[0])
      Counts[0] += 1;
    else if (A[0] == B[0])
      Counts[0] -= 1;
  }
}

// ENCODER 1
void enAUpdate1(){
  A[1] = !A[1];
  if (A[1] == 1){
    if (A[1] == B[1])
      Counts[1] += 1;
    else if (A[1] != B[1])
      Counts[1] -= 1;
  }
}

void enBUpdate1(){
  B[1] = !B[1];
  if (B[1] == 1){
    if (A[1] != B[1])
      Counts[1] += 1;
    else if (A[1] == B[1])
      Counts[1] -= 1;
  }
}

// ENCODER 2
void enAUpdate2(){
  A[2] = !A[2];
  if (A[2] == 1){
    if (A[2] == B[2])
      Counts[2] += 1;
    else if (A[2] != B[2])
      Counts[2] -= 1;
  }
}

void enBUpdate2(){
  B[2] = !B[2];
  if (B[2] == 1){
    if (A[2] != B[2])
      Counts[2] += 1;
    else if (A[2] == B[2])
      Counts[2] -= 1;
  }
}

// ENCODER 3
void enAUpdate3(){
  A[3] = !A[3];
  if (A[3] == 1){
    if (A[3] == B[3])
      Counts[3] += 1;
    else if (A[3] != B[3])
      Counts[3] -= 1;
  }
}

void enBUpdate3(){
  B[3] = !B[3];
  if (B[3] == 1){
    if (A[3] != B[3])
      Counts[3] += 1;
    else if (A[3] == B[3])
      Counts[3] -= 1;
  }
}

// ENCODER 4
void enAUpdate4(){
  A[4] = !A[4];
  if (A[4] == 1){
    if (A[4] == B[4])
      Counts[4] += 1;
    else if (A[4] != B[4])
      Counts[4] -= 1;
  }
}

void enBUpdate4(){
  B[4] = !B[4];
  if (B[4] == 1){
    if (A[4] != B[4])
      Counts[4] += 1;
    else if (A[4] == B[4])
      Counts[4] -= 1;
  }
}

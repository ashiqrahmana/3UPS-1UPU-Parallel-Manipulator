void serialInput(){
  if (Serial.available() > 2){
      int index_1 = 0;
      int index_2 = 0;
      int index_3 = 0;
      int index_4 = 0;
      String setpoints = "";
      setpoints = Serial.readStringUntil('f');
      Serial.setTimeout(0.01);
      
      index_1 = setpoints.indexOf(byte('b'));
      index_2 = setpoints.indexOf(byte('c'));
      index_3 = setpoints.indexOf(byte('d'));
      index_4 = setpoints.indexOf(byte('e'));
      
      // Setpoints all assigned 
      l[0] = (setpoints.substring(        0,          index_1)).toFloat();
      l[1] = (setpoints.substring(index_1+1,          index_2)).toFloat();
      l[2] = (setpoints.substring(index_2+1,          index_3)).toFloat();
      l[3] = (setpoints.substring(index_3+1,          index_4)).toFloat();
      l[4] = (setpoints.substring(index_4+1,setpoints.length())).toFloat();
  }
}

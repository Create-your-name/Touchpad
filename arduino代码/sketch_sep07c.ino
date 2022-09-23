#define s0 PE11
#define s1 PE13
#define s2 PE15
#define s3 PB11


void setup() {
  // put your setup code here, to run once:
  Serial1.begin(115200); 
  pinMode(s0, INPUT_PULLUP);
  pinMode(s1, INPUT_PULLUP);
  pinMode(s2, INPUT_PULLUP);
  pinMode(s3, INPUT_PULLUP);
  
}


int last_press_time = 0;
void loop() {
  
  // put your main code here, to run repeatedly:
  if(digitalRead(s0) == 0)
  {
    delay(10);
    if(digitalRead(s0) == 0)
    {
      Serial1.print("1");
      while(digitalRead(s0) == 0);
      last_press_time = millis();
    }
  }
  
  if(digitalRead(s1) == 0)
  {
    delay(10);
    if(digitalRead(s1) == 0)
    {
      Serial1.print("2");
      while(digitalRead(s1) == 0);
      last_press_time = millis();
    }
  }
  
  if(digitalRead(s2) == 0)
  {
    delay(10);
    if(digitalRead(s2) == 0)
    {
      Serial1.print("3");
      while(digitalRead(s2) == 0);
      last_press_time = millis();
    }
  }
  
  if(digitalRead(s3) == 0)
  {
    delay(10);
    if(digitalRead(s3) == 0)
    {
      Serial1.print("4");
      while(digitalRead(s3) == 0);
      last_press_time = millis();
    }
  }

  if(last_press_time != 0 and millis() - last_press_time)
  {
      Serial1.print("o");
      last_press_time = 0;
  }

  
}

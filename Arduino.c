// Instalar biblioteca LiquidCrystal
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); 

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Aguardando...");
}

void loop() {
  if (Serial.available() > 0) {
    char letra = Serial.read();

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Letra detectada:");
    lcd.setCursor(0, 1);
    lcd.print(letra);
  }
}

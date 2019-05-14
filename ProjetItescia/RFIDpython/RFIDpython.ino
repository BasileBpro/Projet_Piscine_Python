    #include <SPI.h>
    #include <MFRC522.h>
    //on défini nos pin
    #define SS_PIN 10
    #define RST_PIN 9
    // definition des pin du RC522
    MFRC522 mfrc522(SS_PIN, RST_PIN); 
    //on defini la bronche pour notre indicateur/témoin
    int lock = 6;
    //on pourrait très bien ajouter quelques chose comme :
    // int serrure = 3 (pour gérer une gache éléctrique)
    char st[20];
    void setup() 
    {
      pinMode(lock, OUTPUT);
      // si nous avions notre gache electrique
      // pinMode (serrure, OUTPUT);
     
      //initialisation serie(pour le relevé d'information via le moniteur série) et initialisation des deux bibliotheque SPI et MFRC522
      Serial.begin(9600);
      SPI.begin();
      mfrc522.PCD_Init(); 
      // Message initial (le message afiché au démarrage dans le moniteur serie de notre programme arduino)
      Serial.println("Test acces via TAG RFID");
      Serial.println();
    }
    void loop() // le corp de notre programme
    {
      if ( ! mfrc522.PICC_IsNewCardPresent()) 
      {
        return;
      }
      if ( ! mfrc522.PICC_ReadCardSerial()) 
      {
        return;
      }
      Serial.print("UID de tag :");
      String tag= "";
      byte caractere;
      for (byte i = 0; i < mfrc522.uid.size; i++) 
      {
         Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
         Serial.print(mfrc522.uid.uidByte[i], HEX);
         tag.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
         tag.concat(String(mfrc522.uid.uidByte[i], HEX));
      }
      Serial.println();
      Serial.print("Message : ");
      tag.toUpperCase();
      
     // ici on va vérifier l'autorisation
      if (tag.substring(1) == "C0 55 18 A4" || tag.substring(1) == "C6 19 55 73") // le numero de tag est visible lorsqu on presente la carte ou le badge via le moniteur serie
      //il suffit d'insérer ci-dessus le tag que l'on souhaite authoriser ici on dit que si le tag = 06 62 20 02 est lu alors on affiche dans le moniteur serie
      // Tag verifie - Acces Autorisé et nous eteignons notre led pendant 3sec
      {
        digitalWrite(lock, HIGH);
        Serial.println("TAG verifie - Acces Autorise !");
        Serial.println();
        delay(3000);
        digitalWrite(lock, LOW);
        //dans le cas de la gache electrique
        //digitalWrite(serrure, LOW) 
        //*ou HIGH selon le mode de fonctionnement de la gache) ce qui nous laisserais 3 secondes pour ouvrir la porte
        }
     
      else
      //sinon si le Tag n'est pas valide
      {
        //on affiche Acces refuse !!!
        Serial.println("TAG inconnu - Acces refuse !!!");
        Serial.println();
        // on repete 5fois
        for (int i= 1; i<5 ; i++)
        {
          //LED clignotte ici rien à ajouter pour la gache puisque son etat ne doit pas changer la porte reste fermee
          digitalWrite(lock, HIGH);
          delay(200);
          digitalWrite(lock, LOW);
          delay(200);
        }
      }
      delay(1000);
    }

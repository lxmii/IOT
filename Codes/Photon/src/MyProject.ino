// Register the pin that the button is
// connected to

void callback(char* topic, byte* payload, unsigned int length);
byte server[] = { 5,196,95,208 }; //5.196.95.208 is ip of Flukso MQTT broker
MQTT client(server, 1883, callback);

int buttonPin = D6;

// Register and Initialise a flag to hold
// current state.

bool pressed = false;

// Register a delay period to slow things
// down if needed.

int period = 100;

// Perform the program setup

void setup()
{
    // Set the button pin as an input

    pinMode(buttonPin, INPUT);

    // Set the pressed flag to false

    bool pressed = false;

    // Set the initial state of subscriber
    // to off just in case.

     Particle.publish("ledToggle", "off");

}

// Loop through the program

void loop()
{
    // Check to see if the button is pressed
    // or not. The use of flags ensures that
    // only a singular event is called for
    // each state.

    if(digitalRead(buttonPin) == LOW)
    {
        // The button is released. Check against the flag
        // to see if it has already been set. If so return.

        if(pressed == false)
            return;

        // The flag has not been set so set it now.

        pressed = false;

        // Publish the off event.

        Particle.publish("topic/moDet", "NoMo");
    }
    else if(digitalRead(buttonPin) == HIGH)
    {
        // The button is pressed. Check against the flag
        // to see if it has already been set. If so return.

         if(pressed == true)
            return;

        // The flag has not been set so set it now.

        pressed = true;

        // Publish the on event.

        Particle.publish("topic/moDet", "moDet");   //photon detects movement and publishes
    }

    // Use a delay to slow down the loop; thus allowing
    // time for operations to complete.

    delay(period);
}

import serial, time 

while True:
    try:
        ser = serial.Serial('COM7', 9600)
        ser.write(b"hello\r\n")
        time.sleep(1)
        i = ser.readline()
        if len(i) > 0:
            print(i)
        else:
            print("waiting...")
        del ser
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Unknown Exception caused by: {e}")

print("completed")
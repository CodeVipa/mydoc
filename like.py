letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = input("Enter word: \n")
numbers = ''

for i in range(len(word)):
    for j in range(len(letters)):
        if(word[i] == letters[j]):
            numbers += f"{j + 1}"

print(numbers)


class SmartHome:
    def __init__(self):
        self.lights = {'status': 'off', 'brightness': 50}
        self.thermostat = {'temperature': 22}
        self.security = {'doors_locked': True, 'cameras_on': True}
        self.entertainment = {'tv_on': False, 'speaker_volume': 50}

    def control_lights(self, status=None, brightness=None):
        if status:
            self.lights['status'] = status
        if brightness is not None:
            self.lights['brightness'] = max(0, min(100, brightness))
        return self.lights

    def set_thermostat(self, temperature):
        self.thermostat['temperature'] = temperature
        return self.thermostat

    def security_control(self, lock_doors=None, cameras=None):
        if lock_doors is not None:
            self.security['doors_locked'] = lock_doors
        if cameras is not None:
            self.security['cameras_on'] = cameras
        return self.security

    def entertainment_control(self, tv_on=None, volume=None):
        if tv_on is not None:
            self.entertainment['tv_on'] = tv_on
        if volume is not None:
            self.entertainment['speaker_volume'] = max(0, min(100, volume))
        return self.entertainment

# Example Usage
home = SmartHome()
print(home.control_lights(status='on', brightness=75))
print(home.set_thermostat(24))
print(home.security_control(lock_doors=False, cameras=True))
print(home.entertainment_control(tv_on=True, volume=30))




#another example

class SmartLight:
    def __init__(self, light_id):
        self.light_id = light_id
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        print(f"Light {self.light_id} is now ON.")
    
    def turn_off(self):
        self.is_on = False
        print(f"Light {self.light_id} is now OFF.")
    
    def set_brightness(self, brightness):
        if self.is_on:
            self.brightness = brightness
            print(f"Light {self.light_id} brightness set to {brightness}.")
        else:
            print(f"Cannot set brightness. Light {self.light_id} is OFF.")

# Example usage
light = SmartLight("Living Room Light")
light.turn_on()
light.set_brightness(70)
light.turn_off()
#simulating thermostat
class SmartThermostat:
    def __init__(self, thermostat_id):
        self.thermostat_id = thermostat_id
        self.temperature = 0

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Thermostat {self.thermostat_id} temperature set to {temperature}°C.")

# Example usage
thermostat = SmartThermostat("Main Thermostat")
thermostat.set_temperature(22)
#locking/unlocking doors
class SmartLock:
    def __init__(self, lock_id):
        self.lock_id = lock_id
        self.is_locked = False

    def lock(self):
        self.is_locked = True
        print(f"Door {self.lock_id} is now LOCKED.")

    def unlock(self):
        self.is_locked = False
        print(f"Door {self.lock_id} is now UNLOCKED.")

# Example usage
lock = SmartLock("Front Door")
lock.lock()
lock.unlock()
#controlling tv/speakers
class SmartTV:
    def __init__(self, tv_id):
        self.tv_id = tv_id
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"TV {self.tv_id} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"TV {self.tv_id} is now OFF.")

# Example usage
tv = SmartTV("Living Room TV")
tv.turn_on()
tv.turn_off()

class SmartSpeaker:
    def __init__(self, speaker_id):
        self.speaker_id = speaker_id
        self.volume = 0

    def set_volume(self, volume):
        self.volume = volume
        print(f"Speaker {self.speaker_id} volume set to {volume}.")

# Example usage
speaker = SmartSpeaker("Kitchen Speaker")
speaker.set_volume(50)
#
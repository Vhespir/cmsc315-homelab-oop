"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Service:
    # Class variable. One value shared by every service in the lab.
    homelab_name = "nexus"

    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        # Go through set_port so bad ports get caught at creation time.
        self.set_port(port)

    # What print() shows for a service.
    def __str__(self):
        return f'{self.name} is running on {self.host}:{self._port}'

    # The _port attribute is internal. Only change it through here so it always gets validated.
    def set_port(self, port):
        # Must be a real int in the valid TCP/UDP range (1-65535), not a string like "8123".
        if isinstance(port, int) and 0 < port < 65536:
            self._port = port
        else:
            raise ValueError("Port must be an integer between 1 and 65535.")

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

# every container is a service, but not every service is a container
class ContainerService(Service):
    # Class variable shared by all containers.
    runtime = "Docker"

    def __init__(self, name, host, port, image, volumes):
        # Let Service handle name, host, and port, so containers get port validation for free.
        super().__init__(name, host, port)
        self.image = image
        # List of "host_path:container_path" mounts, like docker -v.
        self.volumes = volumes

    # Adds a mount to this container's volume list.
    # Extension: rejects duplicates, since Docker won't start a container with the same mount twice.
    def add_volume(self, volume):
        if volume in self.volumes:
            raise ValueError(f"Volume already mounted: {volume}")
        self.volumes.append(volume)

    # Overrides Service.__str__. Reuses the parent's text and adds the image and volumes.
    def __str__(self):
        base = super().__str__()
        return f'{base}, running image {self.image} with volumes {self.volumes}'


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    c1 = ContainerService("Home Assistant", "nexus", 8123, "homeassistant/home-assistant:latest", 
                      ["/home/vhespir/docker/home_assistant:/config:rw", 
                       "/etc/localtime:/etc/localtime:ro",
                       "/run/dbus:/run/dbus:ro"])
    
    c2 = ContainerService("Grafana", "nexus", 3000,
                      "grafana/grafana:latest",
                      ["/home/vhespir/docker/monitoring/grafana/data:/var/lib/grafana:rw",
                       "/home/vhespir/docker/monitoring/grafana/provisioning:/etc/grafana/provisioning:rw"])

    # Same value both ways. The c1 object has no runtime of its own, so Python finds it on the class.
    print("Via class:", ContainerService.runtime)
    print("Via c1:   ", c1.runtime)

    # Added to c1 only, after creation. The c2 object won't have it.
    c1.notes = "host networking + privileged mode (needs USB/Bluetooth access)"

    # Each object's own attributes. Notes only shows up for c1, and runtime shows up for neither.
    print("c1 namespace:", c1.__dict__)
    print("c2 namespace:", c2.__dict__)

    # Methods and class variables live on the class, not on each object.
    print("ContainerService namespace:", list(ContainerService.__dict__.keys()))

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # The volumes list is the nested mutable data that makes the copies behave differently.
    original = ContainerService("Home Assistant", "nexus", 8123, "homeassistant/home-assistant:latest",
                      ["/home/vhespir/docker/home_assistant:/config:rw"])

    # Shallow copy. New object, but it points at the SAME volumes list as the original.
    shallow = copy(original)

    # Deep copy. New object AND its own separate copy of the volumes list.
    deep = deepcopy(original)

    # Only touch the original. The shallow copy changes too, but the deep copy doesn't.
    original.add_volume("/data/backups/home_assistant:/backups:rw")

    print("Original:", original)
    print("Shallow:", shallow)
    print("Deep:", deep)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent object. The tailscaled daemon runs natively, not in Docker, so it's a plain Service.
    tailscale = Service("Tailscale", "nexus", 46620)
    print(tailscale)

    # Edge cases. Bad configs get rejected and reported instead of crashing the program.
    try:
        bad = Service("broken", "nexus", 99999)
    except ValueError as e:
        print(f"Config rejected:", e)

    try:
        bad = Service("broken", "nexus", "46620")
    except ValueError as e:
        print(f"Config rejected:", e)

    print("\n--- Child class test ---")
    immich = ContainerService("Immich", "nexus", 2283,
                              "ghcr.io/immich-app/immich-server:v2.7.5",
                              ["/data/media/immich/library:/data"])

    print(immich)

    # New child method. Mount the Nextcloud photos as an Immich external library.
    immich.add_volume("/data/media/nextcloud/data/Vhespir/files/Pictures:/external/pictures")

    print(immich)
    # Extension test: adding the same volume again gets rejected instead of duplicated.
    try:
        immich.add_volume("/data/media/immich/library:/data")
    except ValueError as e:
        print("Config rejected:", e)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
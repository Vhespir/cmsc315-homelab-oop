# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## My Implementation

I modeled the real services on my homelab server (nexus). `Service` was the parent class, and it validated ports through `set_port`. `ContainerService` inherited from it and added a Docker image and a list of volumes. In the copy demo, the shallow copy shared the original's volume list and the deep copy did not.

For my extension, I made `add_volume` reject a volume that was already mounted, since Docker won't start a container with a duplicate mount. I tested an out-of-range port (99999), a port passed as text ("46620"), and a duplicate volume, and all three were rejected with an error instead of crashing the program.
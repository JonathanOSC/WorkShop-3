# WorkShop 4

This project focuses on vehicle management using different programming models, such as the Facade, Flyweight, Factory design patterns, among others.

## Description

The main objective of this workshop is to provide an efficient and modular solution for vehicle management. Through the implementation of different programming models, we aim to improve code organization and reusability, as well as optimize system performance and scalability.

## Key Features

- **Facade**: We use the Facade design pattern to simplify the interface for accessing different components of the vehicle management system. This allows developers to interact with the system in a simpler and more consistent way.

- **Flyweight**: We implement the Flyweight design pattern to optimize memory usage by sharing objects that have common intrinsic state. This reduces the amount of memory used by the system and improves its performance.

- **Factory**: We use the Factory design pattern to encapsulate object creation and provide a common interface for creating different types of vehicles. This facilitates system extensibility and allows for adding new types of vehicles without modifying existing code.

## Proposed Changes and Improvements

1. Fix the user action logging in the application.
2. Add tests for all modules, not just the engine subsystem.
3. Perform a code review to identify and fix code issues.
4. Improve documentation and code comments.
5. Optimize functionalities with poor performance identified through logs.
6. Add a new feature for users to subscribe to a newsletter using their email address. The administrator will be able to send the newsletter with information about the latest five created vehicles. If there are fewer than five vehicles, the complete catalog will be sent.
7. Implement a cache to store the last three searches made in the system and avoid repeating them. The cache will be updated each time a vehicle is added.
8. Add a recovery option for the last deleted vehicle in case of an error by the administrator.
9. Add a new engine type: hybrid engine. This engine will have a new attribute: electric_power (in Watts). The values for the attributes of this new engine type will be defined by you, but they will be in the middle range of the values of the other engines.
10. Implement a set of validations for created vehicles, including a valid model name (less than 30 characters and only numbers and letters), a valid year (between 1990 and 2025), a valid price (between 20,000,000 COP and 500,000,000 COP), and a valid chassis (A or B).

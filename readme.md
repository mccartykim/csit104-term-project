# Tim McCarty's CSIT 104 Term Project #

This project is an implementation of the arcade game Asteroids, inspired by Daniel Shiffman's [Nature of Code](http://natureofcode.com/), but written in Python. To do this, I used Pyglet, a graphics library for Python that exposes OpenGL and provides some useful helper classes, as well as other multimedia tools. Instead of using sprites or other premade images, I choose to use vector graphics, which is true to the inspiration as well as well-suited to OpenGL.

Things I wrote myself:
* Vect2:
  * This class is a bare-bones vector representation, which mainly just has functions I needed implemented.
* Entity:
  * This is a collection of classes that use inheritance to create representations of objects in the game.
* HUD:
    * A specialized object that manages points and displaying those points.
* Main:
  * This is the program's entry point, and contains the logic that calls functions that serve as the main game loop. 
* State Manager
    * An object that holds all of the game objects' state and handles interactions and the functions in the main game loop.

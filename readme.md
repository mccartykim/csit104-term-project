# Tim McCarty's CSIT 104 Term Project #

As of now, this project is an implementation of the arcade game Asteroids, inspired by Daniel Shiffman's [Nature of Code](http://natureofcode.com/), but written in Python. To do this, I used Pyglet, a graphics library for Python that exposes OpenGL and provides some useful helper classes, as well as other multimedia tools. Instead of using sprites or other premade images, I choose to use vector graphics, which is true to the inspiration as well as well-suited to OpenGL.

Things I wrote myself:
* Vect2:
  * This class is a bare-bones vector representation, which mainly just has functions I needed implemented.
* Entity:
  * This is a collection of classes that use inheritance to create representations of objects in the game.
* Main:
  * This is the program's entry point, and contains the main loop. While I tried to keep most object actions encapsulated in their classes, interactions mainly take place in the loop, as well as the bookkeeping of deleting dead entities

As of now, I'm considering an Asteroids clone, as it has simple controls and geometry.

A few ideas
* Arcade clones
  * Asteroids
  * Pacman
  * Flappy Bird
* Canablat-style one-button jump game
    * Vertical shooter
* More complicated/original
  * Rocket sim (2D kerbals)

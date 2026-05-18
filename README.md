Phase 1: 
The Core Architecture
- Task 1: Build the Game Loop and Delta Time. You need a central Engine class with a run() method. This method will contain your main while loop.
  Inside this loop, you must calculate "Delta Time" (the fraction of a second it took to render the last frame). You will multiply all movement speeds
  by Delta Time so your physics run at the same speed regardless of whether the computer is running at 30 FPS or 144 FPS.
- Task 2: Build an Event Manager. Instead of putting all your keyboard and mouse checks in the main loop, build a dedicated system that reads Pygame events
  (clicks, key presses, window resizing) and passes that information to the rest of the engine.

Phase 2: Organizing the Game World. 
- Task 3: Create a Scene/State Manager. A game is just a series of states (Main Menu, Level 1, Pause Screen, Game Over).
  Build a system that allows you to swap between these "Scenes" cleanly, so only the active Scene is being updated and drawn to the screen.
- Task 4: Implement an Entity System. Create a base Entity or GameObject class. Everything in your game (the player, enemies, bullets) will be built from this.
  It should have, at minimum, an $X$ and $Y$ coordinate, a method to update() its logic, and a method to draw() itself to the screen.

Phase 3: The Physics and Rendering 
- Task 5: Build a Rendering Pipeline. Create a system that takes all the Entities in the current Scene and draws their sprites (images) or basic geometric
  shapes to the screen in the correct order (e.g., drawing the background before the player, so the player appears on top).
- Task 6: Implement AABB Collision Detection. "Axis-Aligned Bounding Box" collision is the foundation of 2D physics. You need to write the math that checks
  if the invisible rectangle surrounding Entity A is overlapping with the invisible rectangle surrounding Entity B.
- Task 7: Create a Physics/Movement Controller. Build a reusable system that applies velocity and gravity to an Entity, checks for collisions against
  solid walls or floors, and stops the Entity from moving through them.

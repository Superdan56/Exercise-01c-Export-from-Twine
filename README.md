# Exercise-01c-Export-from-Twine
Exercise for MSCH-C220, 31 August 2021

A demonstration of this exercise is available at [https://youtu.be/Xf7WOZN-c94](https://youtu.be/Xf7WOZN-c94)

This exercise will set up Twine to be able to export a version of an interactive fiction game that could be used in a Python game engine.

Begin by Forking this repository. Check that it has been forked successfully; the repository should now read [your username]/Exercise-01c-Export-from-Twine

Edit the LICENSE and replace BL-MSCH-C220-F21 with your full name. Commit your changes.

Press the green "Code" button and select "Open in GitHub Desktop". Allow the browser to open (or install) GitHub Desktop. Once GitHub Desktop has loaded, you should see a window labeled "Clone a Repository" asking you for a Local Path on your computer where the project should be copied. Choose a location where you will keep the repositories for this class (a C220 folder off your Desktop would be fine). Make sure the Local Path ends with "Exercise-01c-Export-from-Twine" and then press the "Clone" button. GitHub Desktop will now download a copy of the repository to the location you indicated.

Open Twine. In the right-hand sidebar, select "Formats". You should see a list of possible story formats for Twine. In the bar on the top of that window is a button "Add a New Format". Select that now.

The window should now read "To add a story format, enter its address below." Enter https://jtschoonhoven.github.io/twine-to-json/dist/harlowe-3.js and press the green "Add" button.

Next, press the "Import From File" button. Navigate to the exercise folder on your computer and select Zork.html. If you open the story, you will see our familiar story (from an earlier exercise).

If you press the play button, you will see the (also) familiar representation of your game in a web browser. By default, Twine uses the Harlowe 3.1.0, playable, story format, with its black background and link-based navigation. We will now export the story in a format that we can use in our game engine.

Tap on the Adventure menu button on the bottom bar, and select "Change Story Format". Choose "Harlowe 3 to JSON 0.0.6" as the new story format. If you now press "Play", your browser will now display a single (JSON) file containing your story.

This content needs to be imported into a Python program so it can be included in your game. Copy all the contents of the browser window (ctrl- or command-a to select all) and then open main.py from this repository in VS Code.

On line 5, you should see a statement that reads
```
world = {}
```
This statement initializes a variable (called world) as an empty dictionary. Select the {} and replace it with the contents of the browser window you copied previously. If you are successful, main.py should now be around 230 lines long instead of 15. *Be careful to only select the {}. When you are done, line 5 should still start world = {*.

The rest of main.py is quite simple. It will print out the name of the world, and then go through each of the passages and print out their relevant contents. Confirm you haven't made any mistakes by running main.py; press the green play button in the top right corner of the VS Code window. 

In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel, and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

In GitHub Desktop, you should now see main.py highlighted. Add a Summary message at the bottom of that panel (something like "Adds zork dictionary to game"), and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

If you return to and refresh your GitHub repository page, you should now see that your files have been changed (with a new date).

Now edit the README.md file. When you have finished editing, commit your changes, and then turn in the URL of the main repository page (https://github.com/[username]/Exercise-01c-Export-from-Twine) on Canvas.

The final state of the file should be as follows (replacing my information with yours):
```
# Exercise-01c-Export-from-Twine
Exercise for MSCH-C220, 31 August 2021

A Python dictionary, describing an interactive fiction game, exported from Twine

## Implementation
Created using Twine 2 and exported with [Harlowe 3 to JSON 0.0.6 by Jonathan Schoonhoven](https://github.com/jtschoonhoven/twine-to-json)

## References
[Zork, 1977 by Tim Anderson, Marc Blank, Dave Lebling, and Bruce Daniels](https://en.wikipedia.org/wiki/Zork)

## Future Development
None

## Created by
Daniel Wright
```

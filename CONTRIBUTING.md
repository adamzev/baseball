Thank you for considering contributing to "Baseball Sim"
===================
# Contributing Guidelines #

## About this project ##

We value and encourage the community to provide contributions and feedback on how we can make the simulation more accurate, more aesthetically pleasing or more fun to use.

We value creating a positive place to learn about coding and contributing to open source software.  If you want to contribute but aren’t confident in your abilities to do so, we are more than happy to work with you and won’t get mad if you make mistakes.

The project is based on a baseball simulation written in Python and brought to the web using Flask and React.

We use the GitHub [issue tracker](https://github.com/tutordelphia/baseball/issues) to track our issues. One can see the progress made on a particular issue and the discussion on any issues. All contributions and commits first start out as issues on the tracker.

### How does it work?

The program gathers real player statistics from the most recent complete season. It takes these stats and converts them in a sample space. Pretend a hitter only hit home-runs (40% of the time) and otherwise struck out. Pick a random number between 0 and 1. If that number is between 0 and .4 it is a home-run, if it is between .4 and 1 it is a strikeout. Based on these sample spaces (which are modified based on who is pitching) an outcome is determined for every at bat. These outcomes are accumulated in the sim until a full game has been played and the result is then reported.

  :baseball:  :popcorn:

## Contributing Code ##

If you want to contribute code, we suggest you to fork the repository first, select an issue, make your changes and submit a pull request for that issue. You can suggest new features, fix an existing functionality for performance or readability, work on open issues, etc. If the contribution will take you a significant amount of time, check in with current contributors on the issues page first. We want to be respectful of your time.

For Python code, please run your code through the [Flake8](http://flake8.pycqa.org/en/latest/) linter before creating a pull request. A linter checks the style (spacing, variable names and so on) of the code. Having a consistent style makes the code easier to maintain.

Key areas of code contributions include:
- Adding teams (Entering starting lineups is currently a manual process but will be automated in the near future)
- Writing Copy (writing text for the web page) and branding (such as choosing color schemes or a more memorable name)
- Proving more details regarding each game (a play by play, box score and player game stats)
- New features
- Documentation
- Improving Sim Accuracy
- Styling

When working on an issue, see if the update/fix already has a pending. 

When creating a pull request, if it applies, close or link to the issue it resolves in your comments. See [GitHubs documentation](https://help.github.com/articles/closing-issues-using-keywords/) on how to do this.

## Current Status ##

The project allows you to create simple simulations of baseball games between the two available teams (Philadelphia and Miami) and displays the results. The simulation produces more detailed information that is not yet displayed.


## Links to resources ##

To get you started, some of the following links can be useful:

- [Git](https://www.atlassian.com/git/tutorials)
- [GitHub](https://guides.github.com/activities/hello-world/)
- [Markdown](https://www.markdowntutorial.com)
- [Flake8](http://flake8.pycqa.org/en/latest/)
- [Flask and React Tutorial](https://danidee10.github.io/2016/09/18/flask-by-example-1.html)
- [Flask](http://flask.pocoo.org/)
- [React](https://reactjs.org/)
- [Semantic UI](https://react.semantic-ui.com)


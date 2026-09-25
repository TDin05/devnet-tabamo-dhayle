# Module 1 — Git & GitHub

**Student:** [Dhayle Tabamo]
**Date:** [September 25, 2026]

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Git helps a lot in organization and makes it safe for developers when editing or updating their projects. Although connected Git and Github are different, think of Git as the the engine of a car and Github as the Car it self, you can use the engine without the car but that cannot be said for the car, without engine car cannot move, sure you can use it as shelter but that's all it was good for, the same can be say for git and github git can be used completely without github but github without git is just another social media platform.]

---

## Key vocabulary (in your own words)

- repository: The project folder 
- commit: Savestates or Snapshot
- branch: A separate folder or a separate device it can't interfere with the main branch unless told to
- push / pull: push is when you publish an update for the project and pull is you downloading the update to update your own files 
- pull request: a pull request is if you push a project update from a separate branch instead of the main branch, it tells the project manager to check the update and update the file in the repository 
- merge conflict: git conflict happens when two people submit a update at the same time, it's like going in the door at the same time since you both can't fit someone needs to pull first before pushing again. 

---

## Walking through what I did

[after making a branch using git branch or git switch -c you need to create the file or just open the file you need to edit then after editing do git add . to make sure all files you edited are tracked then you git commit -m "message here" to do a commit, after commiting push the commit to the repo using git push -u origin branchname]

```
# git switch -c br1
# ni proj.py
# git add .
# git commit -m "initial commit"
# git push -u origin br1
```

---

## A mistake I made (or one I want to avoid)

[do not push first make sure you're files that you updated are the most recent ones to avoid merge conflict, git pull is a must if your files are not updated]

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]

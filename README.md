# JPMorgan Chase Software Engineering Virtual Experience - Task 1
Welcome to the JPMorgan Chase Software Engineering Virtual Experience! In this task, you'll be setting up your local development environment, fixing a broken client data feed script, adding unit tests, and generating a patch file for the changes made. This task will introduce you to essential software engineering practices and tools.
<br><br>
## Task Overview
### 1. Setting Up Your Local Development Environment
Before you start working on the project, ensure that you have a properly configured [new virtual development environment](https://www.youtube.com/watch?v=GZbeL5AcTgw). Next, download the necessary dependencies by installing &nbsp; "*python-dateutil==2.8.2*" &nbsp; to meet the project requirements as shown below.
```
python -m pip install python-dateutil==2.8.2
```
See file, `requirements.txt` located in the main root of this repo once cloned.
<br><br>

### 2. Fixing the Client Data Feed Script
You'll be fixing a broken client data feed script in the repository. To run the program, run the server code file first in one terminal `python server3.py`, then the client in another `python client3.py`. <br><br>
Next, analyze the issues, make the required adjustments to the script, and ensure that it functions correctly. This task tests problem-solving skills and the ability to debug and fix code. See the picture shown below as the results of running the scripts and fixing bugs.

![serverNclient](https://github.com/DJRoche509/forage-jpmc-swe-task-1/assets/100164051/8895aa8d-9595-4d2b-af92-f7e54a807699)
<br><br>

### 3. Adding Unit Tests
Implement unit tests for the modified client data feed script. Writing unit tests is crucial for ensuring the reliability and stability of your code. Test different scenarios and edge cases to validate the functionality of the script using assertions per recommendation.
<br><br>

### 4. Generating a Patch File
After making the necessary changes and adding unit tests, generate a patch file of the modifications. A patch file captures the differences between the original code and your changes. It's a standard way of sharing modifications in the software development process. To create a patch file from a terminal (CMD or GitBash), run the following command into the cloned directory:

```
git format-patch -n --stdout > file_name.patch
``` 
**Note:** Make sure to replace
   - *'n'* in `-n` with a number that represents the number of commits you made. 
   - `file_name` with the desired name for the file with the extension `.patch` appended to it. <br/><br/>

Similarly, the image below shows that I ran the same command in a Git Bash terminal inquiring for the last *"3"* commits to be produced on the patch file named *"multi_commit"*

   ![image](https://github.com/DJRoche509/forage-jpmc-swe-task-1/assets/100164051/7a38a015-177c-4479-8d72-4ae3e40e68b7)


<br><br>
## Steps to Complete the Task
1. **Fetch and clone the Repository**: To find out what is or how to fork a repo, click [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo). After fetching this project's task repo, clone the project repository to your local machine using the following command:
   ```
     git clone https://github.com/theforage/forage-jpmc-swe-task-1
   ```

2. **Set Up Your Environment**: Download the required files, tools, and dependencies. Install `python-dateutil==2.8.2` to fulfill the project requirements.

3. **Fix the Client Datafeed Script**: Analyze the issues in the client datafeed script. Make the necessary adjustments to fix the broken functionality. Test the script locally to ensure it works as expected.

4. **Add Unit Tests**: Write comprehensive unit tests for the client data feed script. Cover different scenarios and edge cases to validate the correctness of your modifications.

5. **Generate a Patch File**: After successfully fixing the script and adding unit tests, generate a patch file that captures your changes. This patch file will be used to record your modifications.

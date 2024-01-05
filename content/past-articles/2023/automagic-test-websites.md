Title: Automagic Test Websites
Date: 2022-03-22 18:32
Modified: 2022-03-23 14:49
Tags: youth, 4-h, education, jenkins, nginx, docker, docker-compose, development, ci, ci-cd, self-hosted, gitlab
Category: Youth
Slug: automagic-test-websites
Authors: Joe Stanley
Summary: Over the last few months, I've been working with a 4-H member to develop and build a smart, simple, and elegant web-application for 4-H members to upload photos they take while participating in a youth conference. Since I'm working with a 4-H member to develop the website, everything needs to have a focus on education, and I need to spend as little time as possible fussing with the infrastructure side of things, since that's not what we're focusing on. I decided that we should make a system using my self-hosted GitLab and Jenkins instances to automagically deploy changes so that the youth doesn't have to learn how that's done, and fight with the server all the time!



As you may already know, I've been working on some fun and interesting stuff with some 4-H members over the last few months. We're developing a
[Python-based photo-upload-app](/reactjs-python-pictures-and-4h.html) to allow 4-H youth (delegates) at a youth conference upload photos securely
to participate in competitions during the conference, and to share photos for the end-of-conference-slideshow.

Anyway, I'm not here to talk about the app; I'll be doing plenty more of that, I'm sure.

What I am here to talk about is how I'm making it automatically deploy the application for
[each development branch in my GitLab instance](https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader) automatically with a little Jenkins magic.
You see, since I have a personal Jenkins instance set up to work with my GitLab, it's able to authenticate and pull all of the source-code from any branch
in whichever repository I configure. Better yet, I can make it automatically look for changes to any-and-all branches, and automatically run builds when
those branches change.

What I've just described is nothing new to those who work in CI/CD (Continuous Integration/Continuous Deployment) systems, but it is valuable and, I think,
novel in this context. I'm using this automated build system to abstract the complexity of deploying a containerized application so that I can focus on
development with a youth member, and focus on programming, not deploying servers. Using Jenkins, in this way, the 4-H'er that I'm working with can write
his own code in GitLab's built in editor, so he doesn't need to learn `git` and he can commit his work, and watch it automatically deploy for him!


## How I'm Making the Magic Happen with Jenkins

So... Like I said, Jenkins is doing most of the heavy lifting here. It's looking for changes, then running builds when those changes appear; but Jenkins
isn't the *hosting server*, itself, it's just the CI server. In fact, I'm using a Linode server which is configured and provisioned as a Jenkins agent (as
far as my Jenkins instance is concerned) that has NGINX, Python, Docker, and docker-compose installed to do the heavy lifting. This way, I can make it all
come together quite nicely.

The pipeline, in a nutshell, looks something like this:

<img src="{attach}/images/jenkins_4h_deployment.png" style="width: 100%" alt="Jenkins Pipeline">

So let's walk through those stages...

#### 1) Prep

Pretty much what it sounds like. Pull down the repo source, do any other setup that's necessary.

Notably though, this stage actually URL-ifies the branch name. In other words, it sanitizes the branch-name to make it appropriate for a unique
subdomain-name. This is kinda critical. Each branch will end up getting its own subdomain under the `idaho4h.com` domain that's filed for this server.
The process is pretty simple, really, just replace whitespace and slashes with dashes so that it's a "legal" subdomain.

Here's the function I use to do it:

```groovy
def urlifyBranchName() {
    // "Sanitize" the Branch Name as a Sub-Domain Name
    // i.e., https://<branch-name>.idaho4h.com/
    env.DOCKER_BRANCH_NAME = BRANCH_NAME.replaceAll(" ", "-").replaceAll("/", "-")
    echo env.DOCKER_BRANCH_NAME
}
```


#### 2) Test Python

This one's pretty simple. Since Python is holding up the backend, I want to run some tests. This is pretty much unit-test only (no functional or
integration tests, here - yet), but it allows us to check some of the simple sanitizer functions we're going to count on for the service.

Adittedly, I had a bit of trouble with some of the virtual-environment stuff, and haven't gotten back around to fixing that yet, so for now just ignore
the title of the function. The execution is pretty simple. pip-install the requirements we need, then run `pytest`. Voila!

```groovy
def runPythonTestsInVirtualEnv() {
    stage("Test Python") {
        // Install Requirements
        sh """python3 -m pip install -r ${WORKSPACE}/${requirementsFile}"""
        
        // Run `pytest`
        sh "pytest"
    }
}
```

#### 3) Build the Frontend

This whole project relies on a Python backend, and a React.js frontend. I need to get around to documenting this whole intertie a little better, but for
now, just know that there are two root folders. One for the frontend, the other for the backend. When building the whole thing, we build and export the
frontend and shove it into the static folder of the backend. Python can then serve all of the javascript, html, and css files from there. Pretty simple,
really (took a while to figure out, though).

What this stage does can be summarized as follows: install npm resources, fix what audit warnings can be handled, build the artifacts. Fairly simple!
Again though, I'll note that there is some prior setup required to make the whole npm ecosystem "happy" with the structure of the frontend folder.

```groovy
def buildReactFrontend() {
    stage("React Frontend") {
        dir("frontend") {
            // Ensure all Packages are Installed
            sh "npm install"

            // Attempt to Resolve Reported Vulnerabilities
            sh "npm audit fix || true" // Don't fail on normal warning

            // Use the Build Tooling
            sh "npm run build"
        }
    }
}
```

#### 4) Dockerize

This whole thing runs in a little docker container. Pretty simple!

```Dockerfile
# Dockerfile for Idaho 4-H Photo Upload Service
FROM python:3.9

WORKDIR /server

COPY ./backend /server

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# Run Server on localhost:8383 so Nginx can Hit it without Direct Extern. Access
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--log-config", "log_conf.yml"]
```

Basically, we just dockerize the Python application after pulling all of its backend source contents into one spot. This whole container is then built and
deployed with a little docker-compose magic:

```yaml
version: "3.9"

# Web-UI is Defined by Local "Dockerfile", Must Be Rebuilt Each Time
services:
  webui:
    build:
      context: ./
      dockerfile: ./Dockerfile
    ports:
      - $NEXT_AVAIL_APP_PORT:80
    restart: $RESTART_POLICY
    environment:
      - LYCHEE_API_USER
      - LYCHEE_API_TOKEN
```

Notice the use of a few things, we've got several environment variables in that docker-compose file:

* `NEXT_AVAIL_APP_PORT` Defines the port that should be used on the host system such that NGINX may pass it traffic.
* `RESTART_POLICY` Defines whether or not the container should restart automatically, this is only set for the `main` and `develop` branches.
* `LYCHEE_API_USER` Calls out that a local environment variable should be pulled from Jenkins to declare the username to use for Lychee access.
* `LYCHEE_API_TOKEN` As for the username, calls out reference to what Jenkins provides as the password (token) for the API access to Lychee.

This, of course, is all leveraged in Jenkins:

```groovy
def buildDockerContainer() {
    stage("Docker Container") {
        
        // Check for "Default" Conditions
        // MAIN and DEVELOP Branches Should Have Consistent Ports
        // Their Containers Should Also Restart Automatically
        if (env.DOCKER_BRANCH_NAME == "main") {
            env.NEXT_AVAIL_APP_PORT = "8000"
            env.RESTART_POLICY = "always"
        } else if (env.DOCKER_BRANCH_NAME == "develop") {
            env.NEXT_AVAIL_APP_PORT = "8001"
            env.RESTART_POLICY = "always"
        }
        echo env.NEXT_AVAIL_APP_PORT

        // Provide credentials to the docker-compose script so that
        // container will reference the Lychee API credentials.
        withCredentials([
            usernamePassword(credentialsId: 'idaho4hapi',
            usernameVariable: 'LYCHEE_API_USER',
            passwordVariable: 'LYCHEE_API_TOKEN')
        ]) {
            // Build the Container - Using the Branch-Name as Env Var
            sh "docker-compose up -d --build"
        }
    }
}
```

The Jenkins scripting is responsible for doing a few things. First and foremost, if the branch is one of the "static" branches (`main` or `develop`),
it's given a static port (the same as the *last* time this branch was deployed). If it's not one of the key branches, then it's given the next available
port, one that comes from a file on the host OS and is incremented each time there's a new deployment. Admittedly, this is a bit intense, and it makes
the port move a little more than it probably needs to, but it does ensure somewhat robust port management.

At the same time the port number is being decided, the restart-policy may be updated. You see, the default restart policy is `"no"`, indicating that the
container should NOT restart if it were to fail, or the host OS were to restart; however, that's not the behavior we want for the "static" branches. They
should restart whenever possible! And that's exactly what the `RESTART_POLICY` environmental override does. It updates the restart policy fro `"no"` to
`"always"` for the static branches.

The next piece of the script is to run the docker-compose command, but notice how that's done in the context of a `withCredentials` block. This allows
Jenkins to provision the Lyche credentials to environmental variables that docker-compose can reference and inject into the container at build-time. This
gives us the ability to launch the container with the appropriate credentials, while securing them in Jenkins and avoiding the need to have them stored as
a static file either in GitLab, or on the server, itself. Sweet!


#### 5) Deploy in NGINX

Who likes typing in the specific port for the web-service they want to use... or better yet, besides the nerdier of us who know about it... who would even think of that?

That's exactly where NGINX comes in in this case. NGINX does all of the proxying for me on this server. What's a proxy? you ask. Well, according to
the Merriam-Webster dictionary:

> proxy (noun)
>
> \ ˈpräk-sē  \
>
> the agency, function, or office of a deputy who acts as a substitute for another

In my case, NGINX *proxies* or represents each of the various services and, in turn, passes web requests to them. So for each new branch, I need to create a new proxy for the associated, url-ified branch name to pass to the specific application port that the container is listening on.

That's done pretty simply by running a little Python script to generate the NGINX configuration, then we restart NGINX to accept the new config.

```groovy
def deployContainerInNginx() {
    stage("Deploy in NGINX") {
        // Generate the NGINX Config File
        sh "python3 ./writeNginxConfig.py"

        // Restart NGINX To Apply Config
        sh "sudo /usr/bin/systemctl restart nginx"
    }
}
```

That little Python script helps us out too, it basically sucks in a few of the environmental variables to determine how the configuration should be written
(or if it should be written at all - it's not written for `main` or `develop` branches). After slurping up those environmental variables, it writes out a
new file with the configuration into NGINX's sites-enabled directory.

```python
################################################################################
"""
deployNginx.py

A deployment helper script to automate the addition of new NGINX configuration
files in the /etc/nginx/sites-enabled directory.
"""
################################################################################

import os

PORT_VAR = os.getenv("NEXT_AVAIL_APP_PORT")
BRANCH_VAR = os.getenv("DOCKER_BRANCH_NAME")

NGINX_CONFIG = """
# {BRANCH_NAME} Configuration
server {{
    listen 80;
    server_name {BRANCH_NAME}.idaho4h.com www.{BRANCH_NAME}.idaho4h.com;

    access_log  /home/jenkins/nginx-logs/{BRANCH_NAME}.log;

    location / {{
        proxy_pass http://127.0.0.1:{CONTAINER_PORT};
        proxy_set_header Host $http_host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;

        client_max_body_size 0;
    }}

}}
"""

if __name__ == '__main__':
    print("Branch: ", BRANCH_VAR)
    print("Port: ", PORT_VAR)
    # Validate that this is not one of the "special" cases
    if BRANCH_VAR.lower() in ['main', 'develop']:
        print("Skipping NGINX Redeploy")
        exit(0) # Stop - Don't Change Port Number
    # Write the New Config File
    with open(os.path.join('/etc/nginx/sites-enabled', BRANCH_VAR), 'w') as f:
        f.write(
            # Fill with the Cleaned Branch Variable and the Container's Port
            NGINX_CONFIG.format(
                BRANCH_NAME=BRANCH_VAR,
                CONTAINER_PORT=PORT_VAR
            )
        )

# END
```

#### 6) Wrap Up

Pretty much exactly what it sounds like, this final stage just puts things "away" after the fact. The primary purpose of this operation is just to store
the configuration for the TCP port to use for Docker the next time around. It's all simplified with the use of a Python file.

```python
################################################################################
"""
updatePort.py

A deployment helper script to automate the "bumping" of the container port file
to coordinate cross-branch container deployments.
"""
################################################################################

import os

PORT_VAR = os.getenv("NEXT_AVAIL_APP_PORT")
BRANCH_VAR = os.getenv("DOCKER_BRANCH_NAME")

if __name__ == '__main__':
    print("Branch: ", BRANCH_VAR)
    # Validate that this is not one of the "special" cases
    if BRANCH_VAR.lower() in ['main', 'develop']:
        print("Skipping Automatic Port Update")
        exit(0) # Stop - Don't Change Port Number
    
    # Run Main Operation
    with open("/home/jenkins/app-ports", 'r') as f:
        content = f.read()
    
    # Modify the Port Number
    current_port = int(PORT_VAR)
    next_port = current_port + 1
    content = content.replace(str(current_port), str(next_port))
    print("Current Deployment Port: ", current_port)
    print("Next Deployment Port: ", next_port)

    with open("/home/jenkins/app-ports", 'w') as f:
        f.write(content)

# END
```

## Recapping

This whole automated flow allows me to keep builds going auto-magically so that I can work with a 4-H youth member to develop this simple little
photo-upload app without having to go too deep into the weeds with all of the development nightmares, we can focus on the basics of the code, and then let
the automated system keep it all moving along for us.


<details>
  <summary>Click to expand all the Jenkinsfile goodness!</summary>
```groovy
/*******************************************************************************
 *
 * Jenkinsfile for Idaho 4-H Delegate Photo Upload Interface
 *
 * 2021 - Stanley Solutions
 * Joe Stanley
 ******************************************************************************/
 
// Global Variables
// In Groovy, global variables are not given a type or proceeded by def
requirementsFile = "backend/requirements.txt"

properties([[$class: 'GitLabConnectionProperty', gitLabConnection: 'StanleySolutions GitLab']])

node ('4happserver') {

    // Set Up Environment Variables
    parameters {
        string(name: 'DOCKER_BRANCH_NAME', defaultValue: '')
        string(name: 'NEXT_AVAIL_APP_PORT', defaultValue: '')
        string(name: 'RESTART_POLICY', defaultValue: 'no')
    }
    // Clean Workspace
    cleanWs()
    
    stage('Prep') {

        // Check Out Source Code
        checkout scm

        // Load the Next Available Port as an Env Var
        load "/home/jenkins/app-ports"

        // Clean Branch Name
        urlifyBranchName()
    }

    // Publish Status of All Contained Stages
    gitlabCommitStatus {

        // Test Backend
        runPythonTestsInVirtualEnv()
        
        // Build Frontend
        buildReactFrontend()

        // Stand Up Container
        buildDockerContainer()

        // Deploy Container
        deployContainerInNginx()

        stage("Wrap Up") {
            // Update Port for Next Build
            sh "python3 ./updatePort.py"
        }

    }
}


def urlifyBranchName() {
    // "Sanitize" the Branch Name as a Sub-Domain Name
    // i.e., https://<branch-name>.idaho4h.com/
    env.DOCKER_BRANCH_NAME = BRANCH_NAME.replaceAll(" ", "-").replaceAll("/", "-")
    echo env.DOCKER_BRANCH_NAME
}

def buildReactFrontend() {
    stage("React Frontend") {
        dir("frontend") {
            // Ensure all Packages are Installed
            sh "npm install"

            // Attempt to Resolve Reported Vulnerabilities
            sh "npm audit fix || true" // Don't fail on normal warning

            // Use the Build Tooling
            sh "npm run build"
        }
    }
}

def buildDockerContainer() {
    stage("Docker Container") {
        
        // Check for "Default" Conditions
        // MAIN and DEVELOP Branches Should Have Consistent Ports
        // Their Containers Should Also Restart Automatically
        if (env.DOCKER_BRANCH_NAME == "main") {
            env.NEXT_AVAIL_APP_PORT = "8000"
            env.RESTART_POLICY = "always"
        } else if (env.DOCKER_BRANCH_NAME == "develop") {
            env.NEXT_AVAIL_APP_PORT = "8001"
            env.RESTART_POLICY = "always"
        }
        echo env.NEXT_AVAIL_APP_PORT

        // Provide credentials to the docker-compose script so that
        // container will reference the Lychee API credentials.
        withCredentials([
            usernamePassword(credentialsId: 'idaho4hapi',
            usernameVariable: 'LYCHEE_API_USER',
            passwordVariable: 'LYCHEE_API_TOKEN')
        ]) {
            // Build the Container - Using the Branch-Name as Env Var
            sh "docker-compose up -d --build"
        }
    }
}

def deployContainerInNginx() {
    stage("Deploy in NGINX") {
        // Generate the NGINX Config File
        sh "python3 ./writeNginxConfig.py"

        // Restart NGINX To Apply Config
        sh "sudo /usr/bin/systemctl restart nginx"
    }
}

def runPythonTestsInVirtualEnv() {
    stage("Test Python") {
        // Install Requirements
        sh """python3 -m pip install -r ${WORKSPACE}/${requirementsFile}"""
        
        // Run `pytest`
        sh "pytest"
    }
}
```
</details>

That means we spend MORE time on learning, and LESS time on fighting the system! In theory, at least...


<img src="https://imgs.xkcd.com/comics/automation.png" style="width: 100%" alt="Woes of Automation">

> *image credit: [XKCD comics](https://xkcd.com/1319/)*

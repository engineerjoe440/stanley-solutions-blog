Title: Automagic Test Websites
Date: 2022-03-22 18:32
Modified: 2022-03-22 18:32
Tags: Youth, 4-H, Education, Jenkins, NGINX, Docker, Docker-Compose, Development, CI, CI-CD, Self-Hosted, Gitlab
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
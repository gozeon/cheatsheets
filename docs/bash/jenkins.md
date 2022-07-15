

```bash title="run_jenkins.sh"
#!/bin/bash

export JENKINS_USER=root
export JENKINS_HOME=/usr/local/src/jenkins_home
nohup /usr/local/java/jdk1.8.0_191/bin/java -jar /usr/local/src/jenkins.war --httpPort=8100 &
```
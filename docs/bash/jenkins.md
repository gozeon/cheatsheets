
## 运行jenkins

```bash title="run_jenkins.sh"
#!/bin/bash

export JENKINS_USER=root
export JENKINS_HOME=/usr/local/src/jenkins_home
nohup /usr/local/java/jdk1.8.0_191/bin/java -jar /usr/local/src/jenkins.war --httpPort=8100 &
```

## 编译 java 项目

```bash
export MAVEN_HOME=/usr/local/maven/apache-maven-3.6.3/
export JAVA_HOME=/usr/local/java/jdk1.8.0_191/

/usr/local/maven/apache-maven-3.6.3/bin/mvn clean package -Dmaven.test.skip=true


scp -r ./target/workflow-serve-1.0.0-SNAPSHOT.jar root@0.0.0.0:/home/workflow/
```

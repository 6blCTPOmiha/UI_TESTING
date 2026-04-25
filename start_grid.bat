start cmd /k "java -jar selenium-server.jar hub"
timeout /t 5
start cmd /k "java -jar selenium-server.jar node --hub http://localhost:4444"
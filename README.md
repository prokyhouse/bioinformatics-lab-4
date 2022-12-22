# Домашнее задание 4 Построение пайплайна получения генетических вариантов



## Часть 1 


## Часть 2

Инструкция по развертыванию и установке фреймворка Pachyderm на macOS Ventura:
1) Установить HomeBrew (если не установлен)  
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2) Установить Docker Desktop и включить "Enable Kubernetes"

3) Установить Pachctl CLI через HomeBrew  
```
brew tap pachyderm/tap && brew install pachyderm/tap/pachctl@2.4  
```
4) Установить Helm
```
brew install helm
```
5) Сконфигурировать его
```
helm repo add pachyderm https://helm.pachyderm.com  
helm repo update
```
6) Установить PachD (в нашем случае Community Edition)
```
helm install pachd pachyderm/pachyderm --set deployTarget=LOCAL --set proxy.enabled=true --set proxy.service.type=LoadBalancer 
```
P.S. тут может не запуститься, проверьте правильность выполнения пункта 2.

7) Проверить всё ли установилось командой
```
kubectl get pods
```
```
NAME                                         READY   STATUS              RESTARTS   AGE
console-555dddcf45-mmdqz                     0/1     ContainerCreating   0          44s
etcd-0                                       0/1     ContainerCreating   0          44s
pachd-ddbbbf759-bl7qc                        0/1     ContainerCreating   0          44s
pachd-loki-0                                 0/1     ContainerCreating   0          44s
pachd-promtail-7b5mm                         1/1     Running             0          44s
pachyderm-kube-event-tail-84bdc9977d-v2rwz   1/1     Running             0          44s
pachyderm-proxy-fff6dc868-h94kd              1/1     Running             0          44s
pg-bouncer-746bb45867-569g5                  0/1     ContainerCreating   0          44s
postgres-0                                   0/1     ContainerCreating   0          44s
```
Если вы видите подобное сообщение, то перезапустите команду через пару минут, потому что pachd еще не готов к работе. При успешном кейсе будет отображаться:
```
NAME                                         READY   STATUS    RESTARTS   AGE
console-555dddcf45-mmdqz                     1/1     Running   0          4m46s
etcd-0                                       1/1     Running   0          4m46s
pachd-ddbbbf759-bl7qc                        1/1     Running   0          4m46s
pachd-loki-0                                 1/1     Running   0          4m46s
pachd-promtail-7b5mm                         1/1     Running   0          4m46s
pachyderm-kube-event-tail-84bdc9977d-v2rwz   1/1     Running   0          4m46s
pachyderm-proxy-fff6dc868-h94kd              1/1     Running   0          4m46s
pg-bouncer-746bb45867-569g5                  1/1     Running   0          4m46s
postgres-0                                   1/1     Running   0          4m46s
```
8) Подключение к кластеру:
```
echo '{"pachd_address":"grpc://127.0.0.1:80"}' | pachctl config set context local --overwrite && pachctl config set active-context local
```
9) Чтобы работать через UI-интерфейс введите в браузере:
```
http://localhost
```
10) С помощью Pip (если нет, то устанавливаем и его) устанавливаем python_pachyderm
```
pip3 install python_pachyderm
```
11) Запускаем наш Python скрипт
```
import python_pachyderm

if __name__ == '__main__':
    # Connects to a pachyderm cluster on localhost:30650
    client = python_pachyderm.Client()

    # Create a pachyderm repo called `test`
    client.create_repo("test")

    # Create a file in (repo="test", branch="master") at `/dir_a/data.txt`
    # Similar to `pachctl put file test@master:/dir_a/data.txt`
    with client.commit("test", "master") as commit:
        client.put_file_bytes(commit, "/dir_a/data.txt", b"hello world")

    # Get the file
    f = client.get_file(("test", "master"), "/dir_a/data.txt")
    print(f.read())  # >>> b"hello world"
```

12) Результатом успешного выполнения скрипта является вывод в консоль ```b'hello world'``` и отображение ```Test``` в Localhost-интерфейсе.

## Часть 3

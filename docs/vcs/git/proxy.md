## github + ssh

```ssh title="~/.ssh/config"
Host github.com
	User git
	Port 22
	Hostname github.com
	IdentityFile ~/.ssh/id_rsa
	TCPKeepAlive yes
	ProxyCommand nc -v -x 127.0.0.1:2024 %h %p

Host ssh.github.com
	User git
	Port 443
	Hostname ssh.gtihub.com
	IdentityFile ~/.ssh/id_rsa
	TCPKeepAlive yes
	ProxyCommand nc -v -x 127.0.0.1:2024 %h %p
```

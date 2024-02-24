## npm 包下载

```bash title="npm.bash"
#!/bin/bash
npm_registry="https://registry.npmmirror.com"
output="."

download_package() {
	wget -qO- $npm_registry/$1/-/$1-$2.tgz \
		| tar -xzv \
		&& mv package $output/$1-$2
}

download_package "moment" "2.30.1"
download_package "lodash" "4.17.21"

```

## 其他

- [npm 命令](../js/npm/常用命令.md#tgz)
- [download-package-tarball](https://github.com/kesla/download-package-tarball)

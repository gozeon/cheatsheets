
编译js并保持目录结构，比如:

```txt
index.es6.js
src
    index.es6.js
```

编译后

```txt
index.es6.js
index.es5.js
src
    index.es6.js
    index.es5.js
```

要求用命令行，保持简单

## babel

        see https://babeljs.io/docs/en/babel-cli

```bash
# 不能准确修改名字

npx babel **/*.es6.js -d ./ --relative --out-file-extension .es5.js --presets=@babel/preset-env
```

## esbuild

        see https://esbuild.github.io/

```bash
# 不能 glob 输入 see: https://github.com/evanw/esbuild/issues/381
# 不能准确修改名字

npx esbuild src/index.es6.js index.es6.js --out-extension:.js=.es5.js --outdir=. --target=chrome58
```

## swc

        需要写配置文件，命令行支持不是很友好
        see https://swc.rs/




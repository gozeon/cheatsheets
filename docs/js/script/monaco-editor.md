## cdn 例子

```html title="index.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monaco Editor Demo</title>
    <style>
        html,body{
            margin: 0;
        }
    </style>
</head>
<body>
    <div id="editor" style="width: 100vw; height: 100vh"></div>
    <script src="https://cdn.jsdelivr.net/npm/monaco-editor@0.52.0/min/vs/loader.js"></script>
    <script>
        require.config({ paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.52.0/min/vs' } });

        require(['vs/editor/editor.main'], function () {
            var editor = monaco.editor.create(document.getElementById('editor'), {
                value: ['function x() {', '\tconsole.log("Hello world!");', '}'].join('\n'),
                language: 'javascript'
            });

            window.onresize = function () {
                editor.layout();
            };
        });
    </script>
</body>
</html>
```

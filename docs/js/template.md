
## html 模板

https://johnresig.com/blog/javascript-micro-templating/

```js title="tmpl.js"
// Simple JavaScript Templating
// John Resig - https://johnresig.com/ - MIT Licensed
(function(){
  var cache = {};
   
  this.tmpl = function tmpl(str, data){
    // Figure out if we're getting a template, or if we need to
    // load the template - and be sure to cache the result.
    var fn = !/\W/.test(str) ?
      cache[str] = cache[str] ||
        tmpl(document.getElementById(str).innerHTML) :
       
      // Generate a reusable function that will serve as a template
      // generator (and which will be cached).
      new Function("obj",
        "var p=[],print=function(){p.push.apply(p,arguments);};" +
         
        // Introduce the data as local variables using with(){}
        "with(obj){p.push('" +
         
        // Convert the template into pure JavaScript
        str
          .replace(/[\r\t\n]/g, " ")
          .split("<%").join("\t")
          .replace(/((^|%>)[^\t]*)'/g, "$1\r")
          .replace(/\t=(.*?)%>/g, "',$1,'")
          .split("\t").join("');")
          .split("%>").join("p.push('")
          .split("\r").join("\\'")
      + "');}return p.join('');");
     
    // Provide some basic currying to the user
    return data ? fn( data ) : fn;
  };
})();
```

```html title="demo1.html"
<script type="text/html" id="item_tmpl">
  <div id="<%=id%>" class="<%=(i % 2 == 1 ? " even" : "")%>">
    <div class="grid_1 alpha right">
      <img class="righted" src="<%=profile_image_url%>"/>
    </div>
    <div class="grid_6 omega contents">
      <p><b><a href="/<%=from_user%>"><%=from_user%></a>:</b> <%=text%></p>
    </div>
  </div>
</script>
```

```html title="demo2.html"
<script type="text/html" id="user_tmpl">
  <% for ( var i = 0; i < users.length; i++ ) { %>
    <li><a href="<%=users&#91;i&#93;.url%>"><%=users&#91;i&#93;.name%></a></li>
  <% } %>
</script>
```

```js
var results = document.getElementById("results");
results.innerHTML = tmpl("item_tmpl", dataObject);
```

### 自定义标签

```js title="tmpl1.js"
// Simple JavaScript Templating
// John Resig - https://johnresig.com/ - MIT Licensed
(function(){
  var cache = {};
  var startTag = "{%";
  var endTag = "%}";
  var re1 = new RegExp(`((^|${endTag})[^\t]*)'`,"g");
  var re2 = new RegExp(`\t=(.*?)${endTag}`,"g");
  
  this.tmpl = function tmpl(str, data){
    // Figure out if we're getting a template, or if we need to
    // load the template - and be sure to cache the result.
	var fn = /^[-a-zA-Z0-9]+$/.test(str) ?
      cache[str] = cache[str] ||
        tmpl(document.getElementById(str).innerHTML) :
              
      // Generate a reusable function that will serve as a template
      // generator (and which will be cached).
      new Function("obj",
        "var p=[],print=function(){p.push.apply(p,arguments);};" +
         
        // Introduce the data as local variables using with(){}
        "with(obj){p.push('" +
         
        // Convert the template into pure JavaScript
        str
          .replace(/[\r\t\n]/g, " ")
          .split(startTag).join("\t")
          .replace(re1, "$1\r")
          .replace(re2, "',$1,'")
          .split("\t").join("');")
          .split(endTag).join("p.push('")
          .split("\r").join("\\'")
      + "');}return p.join('');");
    // Provide some basic currying to the user
    return data ? fn( data ) : fn;
  };
})();
```

## 动态字符串模板

https://stackoverflow.com/questions/30003353/can-es6-template-literals-be-substituted-at-runtime-or-reused

```js
let inject = (str, obj) => str.replace(/\${(.*?)}/g, (x,g)=> obj[g]);

// example
/*

// parameters in object
let t1 = 'My name is ${name}, I am ${age}. My brother name is also ${name}.';
let r1 = inject(t1, {name: 'JOHN',age: 23} );
console.log("OBJECT:", r1); 
OBJECT: My name is JOHN, I am 23. My brother name is also JOHN.
*/

// parameters in array
let t2 = "Values ${0} are in ${2} array with ${1} values of ${0}."
let r2 = inject(t2, ['A,B,C', 666, 'BIG'] );
console.log("ARRAY :", r2);
ARRAY : Values A,B,C are in BIG array with 666 values of A,B,C.

```

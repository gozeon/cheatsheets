
## 扁平化node_modules

> 官方不建议这样做，但是针对老项目，不得不这样做

```bash
# new
pnpm install --shamefully-hoist
# old
pnpm install --shamefully-flatten
```

## 覆盖包

> 针对子依赖不同版本造成的问题，统一版本

```json title="package.json"
{
  "pnpm": {
    "overrides": {
      "foo": "^1.0.0",
      "quux": "npm:@myorg/quux@^1.0.0",
      "bar@^2.1.0": "3.0.0",
      "qar@1>zoo": "2"
    }
  }
}
```
